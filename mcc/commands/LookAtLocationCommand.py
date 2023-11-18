from mcc.command import Command


class LookAtLocationCommand(Command):
    def __init__(self, parameters):
        super().__init__("LookAtLocation", parameters)
