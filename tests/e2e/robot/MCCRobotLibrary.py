# from ..mcc.mcc.py import MccPyClient
from mcc.mcc import MccPyClient  # notype
from mcc.command import Command
from mcc.commands.GetWorldCommand import GetWorldCommand

# For instantiating classes
import importlib


class MCCRobotLibrary:
    async def create_bot(self):
        print("testing custom library")
        self.client = MccPyClient(
            host="mcc_MCC_1",
            port=8043,
            password="wspass12345",  # pragma: allowlist secret
            # loggingEnabled="todo",
            # LogLevels="todo",
            session_name="Test Chat Bot",
            # reconnect="todo",
            # reconnectTimeout="todo",
            # reconnectAttempts="todo",
        )
        await self.client.connect()
        command = GetWorldCommand([])
        await self.client.run_command(command)

    async def disconnect(self):
        await self.client.disconnect()

    async def run_command(self, command_name: str, parameters: list):
        module = importlib.import_module("mcc.commands")
        file_ = getattr(module, command_name)
        class_ = getattr(file_, command_name)
        command: Command = class_(parameters)

        await self.client.run_command(command)
