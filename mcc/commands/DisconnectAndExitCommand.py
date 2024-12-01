from mcc.command import Command


class DisconnectAndExitCommand(Command):
    def __init__(self, parameters):
        super().__init__("DisconnectAndExit", parameters)
