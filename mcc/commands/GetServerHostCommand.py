from mcc.command import Command


class GetServerHostCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetServerHost", parameters)
