from command import Command


class CreativeGiveCommand(Command):
    def __init__(self, parameters):
        super().__init__("CreativeGive")
        self.parameters = parameters
