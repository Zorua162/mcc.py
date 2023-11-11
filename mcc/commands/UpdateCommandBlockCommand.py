from command import Command


class UpdateCommandBlockCommand(Command):
    def __init__(self, parameters):
        super().__init__("UpdateCommandBlock")
        self.parameters = parameters
