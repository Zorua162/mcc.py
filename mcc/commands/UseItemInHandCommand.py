from command import Command


class UseItemInHandCommand(Command):
    def __init__(self, parameters):
        super().__init__("UseItemInHand")
        self.parameters = parameters
