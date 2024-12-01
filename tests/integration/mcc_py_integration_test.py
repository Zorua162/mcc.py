import logging
import pytest
import asyncio

from websockets.server import serve

from mcc.mcc import MccPyClient

HOST = "127.0.0.1"

logger = logging.getLogger()


@pytest.fixture()
def websocket_server(event_loop, unused_tcp_port):
    logger.info("Running WebSocket Server")
    cancel_handle = asyncio.ensure_future(main(unused_tcp_port), loop=event_loop)
    event_loop.run_until_complete(asyncio.sleep(0.1))

    try:
        yield unused_tcp_port
    finally:
        cancel_handle.cancel()


async def echo(websocket):
    async for message in websocket:
        logger.info(f"Returning message {message}")
        await websocket.send(message)


async def main(port):
    logger.info("WebSocket server: Starting")
    async with serve(echo, HOST, port):
        await asyncio.Future()  # run forever


@pytest.mark.skip(reason="Current can't get the server to run correctly")
@pytest.mark.asyncio
async def test_connect_smoke():
    websocket_server = 8756
    logger.info(f"Port is {websocket_server}")
    client = MccPyClient(
        host=HOST,
        port=websocket_server,
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
