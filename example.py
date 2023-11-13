from mcc.mcc import MccPyClient
from mcc.commands.GetWorldCommand import GetWorldCommand
from mcc.ChatBot import ChatBot
import asyncio
import logging


class TestChatBot(ChatBot):
    """An example of implementing the ChatBot"""


client = MccPyClient(
    host="127.0.0.1",
    port=8043,
    password="wspass12345",
    # loggingEnabled="todo",
    log_level=logging.INFO,
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
    await client.keep_alive()


if __name__ == "__main__":
    asyncio.run(main())
