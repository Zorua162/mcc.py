from mcc.command import Command


class ReconnectToTheServerCommand(Command):
    def __init__(self, parameters):
        super().__init__("ReconnectToTheServer", parameters)
