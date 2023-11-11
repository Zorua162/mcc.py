import uuid
import logging
logger = logging.getLogger()


class Command:
    name: str
    request_id: str
    parameters: list[str]

    def __init__(self, name, parameters):
        self.name = name
        self.request_id = random_request_id()
        self.parameters = parameters

    def get_command_json(self) -> str:
        # We convert this to the names that MCC expects, such as requestId
        command_json = str({
            "command": self.name,
            "requestId": self.request_id,
            "parameters": self.parameters,
        })
        logger.info("Sending command JSON: %s", command_json)
        return command_json


def random_request_id() -> str:
    return str(uuid.uuid1())
