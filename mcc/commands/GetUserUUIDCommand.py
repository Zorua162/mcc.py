from command import Command


class GetUserUUIDCommand(Command):
    def __init__(self):
        super().__init__("GetUserUUID", parameters)
        self.parameters = parameters
