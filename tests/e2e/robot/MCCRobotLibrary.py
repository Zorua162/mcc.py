import logging

# For instantiating classes
import importlib
from typing import Optional

# from ..mcc.mcc.py import MccPyClient
from mcc.mcc import MccPyClient  # notype
from mcc.command import Command


class MCCRobotLibrary:
    async def create_bot(self):
        print("testing custom library")
        self.client = MccPyClient(
            host="mcc_MCC_1",
            port=8043,
            password="wspass12345",  # pragma: allowlist secret
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

    async def ensure_clean_disconnect(self):
        if self.client is not None:
            logging.info("Fail clean disconnect called")
            await self.disconnect()

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
