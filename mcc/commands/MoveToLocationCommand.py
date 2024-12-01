from mcc.command import Command


class MoveToLocationCommand(Command):
    def __init__(self, parameters):
        super().__init__("MoveToLocation", parameters)
