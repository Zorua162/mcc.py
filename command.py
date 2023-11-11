import uuid


class Command:
    name: str
    request_id: str
    parameters: list[str]

    def __init__(self, name, parameters):
        self.name = name
        self.request_id = random_request_id()
        self.parameters = parameters

    def get_command_json(self) -> dict:
        # We convert this to the names that MCC expects, such as requestId
        return {
            "command": self.name,
            "requestId": self.request_id,
            "parameters": self.parameters,
        }


def random_request_id():
    return uuid.uuid1()
