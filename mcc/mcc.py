from websockets.sync.client import connect
import logging

# import asyncio
from mcc.commands.AuthenticateCommand import AuthenticateCommand
from mcc.commands.ChangeSessionIdCommand import ChangeSessionIdCommand

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class MccPyClient:
    def __init__(
        self, host: str, port: int, password: str = "", session_name: str = ""
    ):
        self.host: str = host
        self.port: int = port
        self.password: str = password
        self.session_name: str = session_name

    async def connect(self) -> None:
        logger.info("Connecting to {self.host} on port {self.port} ...")
        with connect("ws://127.0.0.1:8043/mcc", logger=logger) as socket:
            logger.info(f"Successfully connected to {self.host} on port {self.port} ...")

            if self.password != "":
                # Send authenticate event
                socket.send(AuthenticateCommand([self.password]).get_command_json())

            if self.session_name != "":
                # Send session name command
                socket.send(
                    ChangeSessionIdCommand([self.session_name]).get_command_json()
                )

            # Python websockets doesn't provide callbacks, so implement our own:
            # https://websockets.readthedocs.io/en/stable/faq/misc.html#are-there-onopen-onmessage-onerror-and-onclose-callbacks
            # await asyncio.gather(
            #     consumer_handler(socket),
            #     producer_handler(socket),
            # )


# async def producer_handler(websocket):
#     while True:
#         message = await producer()
#         await websocket.send(message)
#
#
# async def consumer_handler(websocket):
#     async for message in websocket:
#         await consumer(message)
