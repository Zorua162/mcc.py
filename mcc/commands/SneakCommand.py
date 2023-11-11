from command import Command


class SneakCommand(Command):
    def __init__(self):
        super().__init__("Sneak", parameters)
        self.parameters = parameters
