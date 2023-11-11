from command import Command


class UseItemInHandCommand(Command):
    def __init__(self):
        super().__init__("UseItemInHand", parameters)
        self.parameters = parameters
