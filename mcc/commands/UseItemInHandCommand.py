from mcc.command import Command


class UseItemInHandCommand(Command):
    def __init__(self, parameters):
        super().__init__("UseItemInHand", parameters)
