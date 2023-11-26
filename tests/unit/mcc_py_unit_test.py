import asyncio
import os
import logging
import pytest
import json

from mcc.mcc import MccPyClient
from mcc.ChatBot import ChatBot
from unittest.mock import patch

import sys

print(sys.path)

# Set the timeout time for commands to fail
os.environ["TIMEOUT"] = "5"
logging.basicConfig()
logger = logging.getLogger()


class FakeBackend:
    open = True

    def __init__(self):
        self.received_messages = []
        logger.debug("Started fake backend")

    async def send(self, message):
        self.received_messages.append(message)
        return "aaa"

    def __aiter__(self):
        return self

    async def __anext__(self):
        # Wait for there to be an item in the list
        while len(self.received_messages) == 0:
            await asyncio.sleep(0.5)
        # Reply to the next item in the received_messages list
        message_data = self.received_messages.pop(0)
        logger.info(f"__anext__ message_data: {repr(message_data)}")
        message = json.loads(message_data)
        # Default value for data
        data = {"success": False, "requestId": message["requestId"]}
        logger.info(f"__anext__ message: {message}, type {type(message)}")
        match message["command"]:
            case "Authenticate":
                data = {
                    "success": True,
                    "requestId": message["requestId"],
                    "command": "Authenticate",
                    "result": "Successfully authenticated!",
                }
            case "ChangeSessionId":
                data = {
                    "success": True,
                    "requestId": message["requestId"],
                    "command": "ChangeSessionId",
                    "result": "The session ID was successfully changed to: "
                    f'{message["parameters"][0]}',
                }

        event = {"event": "OnWsCommandResponse", "data": json.dumps(data)}
        event_data = json.dumps(event)
        logger.info(f"__anext__ event_data {repr(event_data)}")
        return event_data

    async def close(self):
        self.open = False
        logging.info("Closed fake connection")


async def fake_connection(uri, logger=None):
    print(f"Creating fake connection with uri {uri} and logger {logger}")
    return FakeBackend()


@pytest.fixture()
def client():
    client = MccPyClient(
        host="127.0.0.1",
        port=8043,
        password="wspass12345",  # pragma: allowlist secret
        logger=logger,
        # loggingEnabled="todo",
        # LogLevels="todo",
        session_name="Test Chat Bot",
        # reconnect="todo",
        # reconnectTimeout="todo",
        # reconnectAttempts="todo",
    )
    return client


@patch("mcc.mcc.connect", new=fake_connection)
@pytest.mark.asyncio
async def test_unit_connect_smoke(client):
    await client.connect()

    await client.disconnect()


@pytest.mark.asyncio
async def test_unit_consumer_chat_bot_none(client, caplog):
    message = {"event": "OnServerTpsUpdate", "data": '{"tps":19.97199526823488}'}
    await client.execute_chat_bot_event(message)
    assert "Chat bot was None, ignoring event" in caplog.text


class TestChatBot(ChatBot):
    """An empty ChatBot"""

    def OnTimeUpdate(self, worldAge, timeOfDay):
        # place holder event
        logger.info("On time update called")


@pytest.mark.asyncio
async def test_unit_consumer_event_called_on_time_update(client, caplog):
    # message = {'event': 'OnServerTpsUpdate', 'data': '{"tps":19.97199526823488}'}
    message = {
        "event": "OnTimeUpdate",
        "data": '{"worldAge":1181337,"timeOfDay":1181337}',
    }
    await client.execute_chat_bot_event(message)
    assert "On time update called" in caplog.text
