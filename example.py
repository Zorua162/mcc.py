# Experiment with printing the python path

# from mcc import ChatBot
from mcc.mcc import MccPyClient
import asyncio

# class TestChatBot(ChatBot):
#     """An example of implementing the ChatBot"""


client = MccPyClient(
    host="127.0.0.1",
    port=8043,
    password="wspass12345",
    # loggingEnabled="todo",
    # LogLevels="todo",
    session_name="Test Chat Bot",
    # reconnect="todo",
    # reconnectTimeout="todo",
    # reconnectAttempts="todo",
)

asyncio.run(client.connect())
