import logging

# For instantiating classes
import importlib
from typing import Optional

# from robot.api import logger  # notype

# from ..mcc.mcc.py import MccPyClient
from mcc.mcc import MccPyClient
from mcc.command import Command

logger = logging.getLogger("MCCRobotLibrary")


class MCCRobotLibrary:
    def create_bot(self):
        self.client = MccPyClient(
            host="mcc_MCC_1",
            port=8043,
            password="wspass12345",  # pragma: allowlist secret
            logger=logger,
            # loggingEnabled="todo",
            # LogLevels="todo",
            log_level=logging.DEBUG,
            session_name="Test Chat Bot",
            # reconnect="todo",
            # reconnectTimeout="todo",
            # reconnectAttempts="todo",
        )

    async def connect(self):
        await self.client.connect()

    async def disconnect(self):
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
                await self.client.send_message(message)
            return None
        module = importlib.import_module("mcc.commands")
        file_ = getattr(module, command_name)
        class_ = getattr(file_, command_name)
        command: Command = class_(parameters)

        return await self.client.run_command(command)
