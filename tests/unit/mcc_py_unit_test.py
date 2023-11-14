import logging
import pytest

from mcc.mcc import MccPyClient
from unittest.mock import patch

logger = logging.getLogger()


class FakeWebSocketCommonProtocol:
    async def send(message):
        logger.info(f"Send called with message {message}")

    async def disconnect(self):
        pass


def fake_websocket_connect():
    return FakeWebSocketCommonProtocol()


@pytest.mark.asyncio
async def test_connect_smoke():
    with patch("websockets.connect", new=fake_websocket_connect):
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
