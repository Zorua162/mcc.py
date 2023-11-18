from mcc.command import Command


class GetServerPortCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetServerPort", parameters)
