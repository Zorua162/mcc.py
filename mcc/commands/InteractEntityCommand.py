from mcc.command import Command


class InteractEntityCommand(Command):
    def __init__(self, parameters):
        super().__init__("InteractEntity", parameters)
