from mcc.command import Command


class GetGamemodeCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetGamemode", parameters)
