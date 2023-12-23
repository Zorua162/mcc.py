from websockets import connect
from websockets.legacy.protocol import WebSocketCommonProtocol
import os
import logging
import json
import asyncio

from mcc.commands.AuthenticateCommand import AuthenticateCommand
from mcc.commands.ChangeSessionIdCommand import ChangeSessionIdCommand
from mcc.command import Command

from mcc.ChatBot import ChatBot  # type: ignore

from typing import Optional


class MccPyClient:
    def __init__(
        self,
        host: str,
        port: int,
        logger: logging.Logger,
        password: str = "",
        log_level: int = logging.INFO,
        session_name: str = "",
        chat_bot: Optional[ChatBot] = None,
        max_saved_chat_messages: int = 100,
    ):
        # self._socket: Optional[WebSocketCommonProtocol] = None
        self.host: str = host
        self.port: int = port
        self.password: str = password
        self.session_name: str = session_name

        # Message queues
        self.message_queue: list = []
        self.responses: list = []

        # Chat
        self.chat_messages: list = []
        self.max_saved_chat_messages = max_saved_chat_messages

        # Chat bot
        self.chat_bot = chat_bot

        # if base logging library logger set Level, otherwise if robot logger then don't
        if hasattr(logger, "setLevel"):
            logger.setLevel(log_level)
        self.logger = logger
        logger.info("Bot initialization completed successfully")

    async def run_background_tasks(self, socket):
        """Run the consumer and producer tasks"""
        consumer_task = asyncio.create_task(self.consumer_handler(socket))
        producer_task = asyncio.create_task(self.producer_handler(socket))
        _, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()

    async def connect(self) -> None:
        self.logger.info(f"Connecting to {self.host} on port {self.port} ...")
        socket = await connect(
            f"ws://{self.host}:{self.port}/mcc", logger=self.logger, close_timeout=1
        )
        self._socket = socket
        self.logger.info(
            f"Successfully connected to {self.host} on port " f"{self.port} ..."
        )

        # Python websockets doesn't provide callbacks, so implement our own:
        # https://websockets.readthedocs.io/en/stable/faq/misc.html#are-there-onopen-onmessage-onerror-and-onclose-callbacks
        asyncio.create_task(self.run_background_tasks(socket))

        if self.password != "":
            # Send authenticate event
            authenticate_command = AuthenticateCommand([self.password])

            self.logger.info("Sending authenticate command")
            await socket.send(authenticate_command.get_command_json())

            # Wait for authentication to succeed before running loops
            response = await self.wait_for_response(authenticate_command.request_id)
            self.logger.info(f"Auth response was {response}")
            # If the command was successful then break out the waiting loop
            if response is None or response["success"] is False:
                # If the command failed then raise an exception
                raise Exception("Authenticate command failed")
            self.logger.info("Authentication succeeded... Continuing...")

        if self.session_name != "":
            # Send session name command
            change_session_command = ChangeSessionIdCommand([self.session_name])
            self.logger.info("Sending ChangeSessionId command")
            await socket.send(change_session_command.get_command_json())

            # NOTE: This required a fix to MinecraftConsoleClient, so needs the
            # updated binary
            # Wait for response
            response = await self.wait_for_response(change_session_command.request_id)
            self.logger.info(f"Change name response was {response}")
            if response is None or response["success"] is False:
                # If the command failed then raise an exception
                raise Exception("ChangeSessionId command failed")
            self.logger.info("ChangeSessionId succeeded... Continuing...")

        self.logger.info("Client successfully connected")

    async def disconnect(self):
        self.logger.info("Disconnecting")
        await self._socket.close()

    async def keep_alive(self):
        # Wait for background tasks
        await asyncio.gather(*asyncio.all_tasks())

    async def producer_handler(self, socket):
        while socket.open:
            message = await self.producer(socket)
            if message is not None:
                await socket.send(message)
            # Wait 0.1s before getting the next message
            await asyncio.sleep(0.1)
        self.logger.debug("Socket was closed, producer exited")

    async def producer(self, socket: WebSocketCommonProtocol) -> Optional[str]:
        while len(self.message_queue) == 0:
            await asyncio.sleep(0.1)
            # If the socket is closed then return none
            if not socket.open:
                self.logger.debug(
                    "Socket was closed, exiting message queue producer " "wait"
                )
                return None
        self.logger.info(f"Send message queue is currently: {self.message_queue}")
        return self.message_queue.pop()

    def add_message(self, message: str):
        self.message_queue.append(message)

    async def send_message(self, message: str):
        self.logger.info(f"Sending the string {message}")
        self.add_message(message)

    async def run_command(self, command: Command) -> Optional[dict]:
        self.logger.info(f"Adding the command to the message queue {command.name}")
        self.add_message(command.get_command_json())

        response = await self.wait_for_response(command.request_id)
        self.logger.info(f"Response was {response}")
        return response

    async def consumer_handler(self, socket):
        async for message in socket:
            if not socket.open:
                self.logger.debug("Consumer exited, as socket is closed")
                return
            await self.consumer(message)
        self.logger.debug("Consumer exited")

    async def consumer(self, message_data):
        """Send the message to where it needs to go"""
        # Decode it
        message = json.loads(message_data)
        self.logger.debug("Received message %s", message)
        if message["event"] == "OnWsCommandResponse":
            self.responses.append(json.loads(message["data"]))
        if message["event"] == "OnChatRaw":
            self.chat_messages.append(json.loads(message["data"]))
            if len(self.chat_messages) > self.max_saved_chat_messages:
                self.chat_messages = self.chat_messages[1:]
        await self.execute_chat_bot_event(message)

    async def execute_chat_bot_event(self, message: dict):
        """Given the current  chat bot execute the given event"""
        self.logger.debug(f"Message data {message}")
        if self.chat_bot is None:
            self.logger.info(f'Chat bot was None, ignoring event {message["event"]}')
            return
        # Call the method on the bot
        event: str = message["event"]
        attribute = getattr(self.chat_bot, event, None)
        if attribute is None:
            self.logger.error(f"Unsupported event {event}... Please report this error")
        # If the attribute is callable then call the event method
        if not message["data"]:
            data = {}
        else:
            data = json.loads(message["data"])
        self.logger.debug(f"Calling attribute {attribute}, with data {data}")
        if callable(attribute):
            attribute(*data.values())

    def find_chat_message(self, expected_msg: str) -> Optional[dict]:
        for message in self.chat_messages:
            if expected_msg in message["text"]:
                return message
        return None

    async def expect_chat_message(
        self, expected_msg: str, poll_sleep=0.5
    ) -> Optional[dict]:
        """Wait for chat message"""
        timeout = int(os.environ.get("TIMEOUT", "30"))
        total_wait = 0
        self.logger.info(
            f"Waiting for chat message with which contains {expected_msg} "
        )
        self.logger.debug(f"timeout is {timeout}")
        while total_wait < timeout:
            self.logger.debug(f"total_wait is currently {total_wait}")
            message = self.find_chat_message(expected_msg)
            # Wait for the command response to be found
            if message is not None:
                return message
            self.logger.debug(f"After get_response, {poll_sleep}")
            await asyncio.sleep(poll_sleep)
            self.logger.debug("After sleep")
            total_wait += poll_sleep
        return None

    def clear_message_history(self):
        self.chat_messages = []

    async def wait_for_response(self, request_id, poll_sleep=0.5) -> Optional[dict]:
        """Wait for the response to a command to be in the response queue,
        Return None if the maximum wait time is reached, specified by TIMEOUT env var"""
        timeout = int(os.environ.get("TIMEOUT", "30"))
        total_wait = 0
        self.logger.info(
            f"Waiting for Command with requestId {request_id} " "to succeed..."
        )
        self.logger.debug(f"timeout is {timeout}")
        while total_wait < timeout:
            self.logger.debug(f"total_wait is currently {total_wait}")
            message = self.get_response(request_id)
            # Wait for the command response to be found
            if message is not None:
                return message
            self.logger.debug(f"After get_response, {poll_sleep}")
            await asyncio.sleep(poll_sleep)
            self.logger.debug("After sleep")
            total_wait += poll_sleep
        return None

    def get_response(self, request_id: str, expected_msg=None) -> Optional[dict]:
        # If message not found then return None
        out_message: Optional[dict] = None
        self.logger.debug(f"responses is {self.responses}")
        for message in self.responses:
            self.logger.debug(
                f"Checking message {message}, "
                f"requestId is {request_id}, "
                f"message type is {type(message)}"
            )
            if "requestId" not in message.keys():
                raise Exception(
                    "Missing data in event, "
                    '"requestId" was not in the returned message'
                )
            if message["requestId"] == request_id:
                self.logger.debug(
                    f"Command with requestId {request_id} was found, returning"
                )
                out_message = message
        # If the message was found then remove it from the list of current responses
        if out_message is not None:
            self.responses.remove(out_message)
        return out_message
