# from ..mcc.mcc.py import MccPyClient
from mcc.mcc import MccPyClient  # notype
from mcc.commands.GetWorldCommand import GetWorldCommand


class MCCRobotLibrary:
    async def create_bot(self):
        print("testing custom library")
        client = MccPyClient(
            host="127.0.0.1",
            port=8043,
            password="wspass12345",  # pragma: allowlist secret
            # loggingEnabled="todo",
            # LogLevels="todo",
            session_name="Test Chat Bot",
            # reconnect="todo",
            # reconnectTimeout="todo",
            # reconnectAttempts="todo",
        )
        await client.connect()
        command = GetWorldCommand([])
        await client.run_command(command)

        await client.disconnect()
