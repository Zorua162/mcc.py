from command import Command


class CreativeGiveCommand(Command):
    def __init__(self):
        super().__init__("CreativeGive", parameters)
        self.parameters = parameters
