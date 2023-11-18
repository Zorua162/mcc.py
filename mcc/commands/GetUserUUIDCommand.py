from mcc.command import Command


class GetUserUUIDCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetUserUUID", parameters)
