from mcc.mcc import MccPyClient

from mcc.commands.GetWorldCommand import GetWorldCommand
from mcc.ChatBot import ChatBot
import asyncio
import logging

logging.basicConfig()

logger = logging.getLogger("example_client")


class TestChatBot(ChatBot):
    """An example of implementing the ChatBot"""


client = MccPyClient(
    host="127.0.0.1",
    # host="localhost",
    port=8043,
    password="wspass12345",  # pragma: allowlist secret
    logger=logger,
    # loggingEnabled="todo",
    log_level=logging.INFO,
    # log_level=logging.DEBUG,
    session_name="Test Chat Bot",
    chat_bot=TestChatBot()
    # reconnect="todo",
    # reconnectTimeout="todo",
    # reconnectAttempts="todo",
)


async def main():
    await client.connect()
    command = GetWorldCommand([])
    await client.run_command(command)
    await client.send_message("/send /tp @s 0 0 0")
    # await client.keep_alive()

    # Give the send_message and command that was run enough time to be sent
    await asyncio.sleep(3)
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
