from mcc.command import Command


class GetUsernameCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetUsername", parameters)
