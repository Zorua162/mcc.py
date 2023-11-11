import uuid


class Command:
    name: str
    request_id: str

    def __init__(self, name):
        self.name = name
        self.request_id = random_request_id()

    def get_command_json(self) -> str:
        # We convert this to the names that MCC expects, such as requestId
        return {
            "command": self.name,
            "requestId": self.request_id,
            "parameters": self.get_parameters(),
        }


def random_request_id():
    return uuid.uuid1()
