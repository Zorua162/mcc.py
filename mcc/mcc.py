from websockets import connect
from websockets.legacy.protocol import WebSocketCommonProtocol
import logging
import json
import asyncio

from mcc.commands.AuthenticateCommand import AuthenticateCommand
from mcc.commands.ChangeSessionIdCommand import ChangeSessionIdCommand
from command import Command

from ChatBot import ChatBot  # type: ignore

from typing import Optional

logging.basicConfig()
logger = logging.getLogger(__name__)


class MccPyClient:
    def __init__(
        self,
        host: str,
        port: int,
        password: str = "",
        log_level: int = logging.INFO,
        session_name: str = "",
        chat_bot: Optional[ChatBot] = None,
    ):
        # self._socket: Optional[WebSocketCommonProtocol] = None
        self.host: str = host
        self.port: int = port
        self.password: str = password
        self.session_name: str = session_name

        # Message queue
        self.message_queue: list = []
        self.responses: list = []

        # Chat bot
        self.chat_bot = chat_bot

        # Logging
        logger.setLevel(log_level)

    async def run_background_tasks(self, socket):
        """Run the consumer and producer tasks"""
        consumer_task = asyncio.create_task(self.consumer_handler(socket))
        producer_task = asyncio.create_task(self.producer_handler(socket))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()

    async def connect(self) -> None:
        logger.info("Connecting to {self.host} on port {self.port} ...")
        socket = await connect("ws://127.0.0.1:8043/mcc", logger=logger)
        self._socket = socket
        logger.info(f"Successfully connected to {self.host} on port {self.port} ...")

        # Python websockets doesn't provide callbacks, so implement our own:
        # https://websockets.readthedocs.io/en/stable/faq/misc.html#are-there-onopen-onmessage-onerror-and-onclose-callbacks
        asyncio.create_task(self.run_background_tasks(socket))

        if self.password != "":
            # Send authenticate event
            command = AuthenticateCommand([self.password])

            logger.info("Sending authenticate command")
            await socket.send(command.get_command_json())

            # Wait for authentication to succeed before running loops
            response = await self.wait_for_response(command.request_id)
            logger.info(f"Auth response was {response}")
            # If the command was successful then break out the waiting loop
            if response is None or response["success"] is False:
                # If the command failed then raise an exception
                raise Exception("Authenticate command failed")
            logger.info("Authentication succeeded... Continuing...")

        if self.session_name != "":
            # Send session name command
            await socket.send(
                ChangeSessionIdCommand([self.session_name]).get_command_json()
            )
        logger.info("Client successfully connected")

    async def disconnect(self):
        await self._socket.close()

    async def keep_alive(self):
        # Wait for background tasks
        await asyncio.gather(*asyncio.all_tasks())

    async def producer_handler(self, socket):
        while socket.open:
            message = await self.producer(socket)
            if message is not None:
                await socket.send(message)

    async def producer(self, socket: WebSocketCommonProtocol) -> Optional[str]:
        while len(self.message_queue) == 0:
            await asyncio.sleep(0.1)
            # If the socket is closed then return none
            if not socket.open:
                logger.debug("Socket was closed, exiting message queue producer wait")
                return None
        logger.info(f"Send message queue is currently: {self.message_queue}")
        return self.message_queue.pop()

    def add_message(self, message: str):
        self.message_queue.append(message)

    async def run_command(self, command: Command) -> Optional[dict]:
        logger.info(f"Adding the command to the message queue {command.name}")
        self.add_message(command.get_command_json())

        response = await self.wait_for_response(command.request_id)
        logger.info(f"Response was {response}")
        return response

    async def consumer_handler(self, socket):
        async for message in socket:
            await self.consumer(message)

    async def execute_chat_bot_event(self, message: dict):
        """Given the current  chat bot execute the given event"""
        if self.chat_bot is None:
            logger.debug('Chat bot was none, ignoring event {message["event"]}')
            return
        # Call the method on the bot
        event: str = message["event"]
        attribute = getattr(self.chat_bot, event, None)
        if attribute is None:
            logger.error(f"Unsupported event {event}... Please report this error")
        # If the attribute is callable then call the event method
        if callable(attribute):
            attribute(message)

    async def consumer(self, message_data):
        """Send the message to where it needs to go"""
        # Decode it
        message = json.loads(message_data)
        logger.debug("Received message %s", message)
        if message["event"] == "OnWsCommandResponse":
            self.responses.append(json.loads(message["data"]))
        self.execute_chat_bot_event(message)

    async def wait_for_response(
        self, request_id, timeout=30, poll_sleep=0.5
    ) -> Optional[dict]:
        """Wait for command authenticate to be in the response queue,
        Raise an error if it failed"""
        total_wait = 0
        logger.info("Waiting for authentication to succeed...")
        while total_wait < timeout:
            logger.debug(f"total_wait is currently {total_wait}")
            message = self.get_response(request_id)
            # Wait for the command response to be found
            if message is not None:
                return message

            await asyncio.sleep(poll_sleep)
            total_wait += poll_sleep
        return None

    def get_response(self, request_id: str) -> Optional[dict]:
        for message in self.responses:
            logger.debug(
                f"Checking success of message {message}, "
                f"requestId is {request_id}, "
                f"message type is {type(message)}"
            )
            if message["requestId"] == request_id:
                logger.debug(
                    f"Command with requestId {request_id} was found, returning"
                )
                return message
        # Message was not found, return None to signify this
        return None
