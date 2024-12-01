from mcc.command import Command


class GetWorldCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetWorld", parameters)
