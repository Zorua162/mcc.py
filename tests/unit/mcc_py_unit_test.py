import logging
import pytest

from mcc.mcc import MccPyClient
from unittest.mock import patch

import sys

print(sys.path)

logger = logging.getLogger()


@patch("mcc.mcc.websockets.connect")
@pytest.mark.asyncio
async def test_connect_smoke():
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

    await client.disconnect()


@pytest.mark.asyncio
async def test_consumer():
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

    message = {"event": "stuff"}
    await client.execute_chat_bot_event(message)
