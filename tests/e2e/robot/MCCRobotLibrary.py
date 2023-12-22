import logging
from logging import FileHandler

# For instantiating classes
import importlib
from typing import Optional

# from robot.api import logger  # notype

# from ..mcc.mcc.py import MccPyClient
from mcc.mcc import MccPyClient
from mcc.ChatBot import ChatBot
from mcc.command import Command

# logging.basicConfig(filename='/output/MCCRobotLibrary.log')

logger = logging.getLogger("MCCRobotLibrary")

logger.addHandler(FileHandler("/output/MCCRobotLibrary.log"))


class RobotChatBot(ChatBot):
    def OnChatRaw(self, text, json):
        logger.info(f"Raw message received\n    text: {text}\n   json {json}")

    def OnMccCommandResponse(self, response):
        logger.info(f"MCCCommandResponse received\n    response: {response}")


class MCCRobotLibrary:
    client: Optional[MccPyClient] = None

    def create_bot(self):
        self.client = MccPyClient(
            host="mcc_mcc_1",
            port=8043,
            password="wspass12345",  # pragma: allowlist secret
            logger=logger,
            # loggingEnabled="todo",
            # LogLevels="todo",
            log_level=logging.DEBUG,
            session_name="Test Chat Bot",
            chat_bot=RobotChatBot(),
            # reconnect="todo",
            # reconnectTimeout="todo",
            # reconnectAttempts="todo",
        )

    async def connect(self):
        logger.info("Connecting to the MCC Websocket server with the client")
        await self.client.connect()

    async def disconnect(self):
        logger.info("Disconnecting from the MCC Websocket")
        if self.client is None:
            logger.info("Client is None, skipping disconnect")
            return

        await self.client.disconnect()
        # Set the client to None, so that we know it was disconnected
        self.client = None

    async def run_command(self, command_name: str, parameters: list) -> Optional[dict]:
        if self.client is None:
            raise Exception("MCC Client not created")
        if command_name == "None":
            return {}
        if command_name == "SendMessage":
            for message in parameters:
                await self.client.send_message(message, None)
            return {"success": True, "result": "Command was run"}
        module = importlib.import_module("mcc.commands")
        file_ = getattr(module, command_name)
        class_ = getattr(file_, command_name)
        command: Command = class_(parameters)

        return await self.client.run_command(command)
