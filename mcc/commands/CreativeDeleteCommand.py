from command import Command


class CreativeDeleteCommand(Command):
    def __init__(self, parameters):
        super().__init__("CreativeDelete")
        self.parameters = parameters
