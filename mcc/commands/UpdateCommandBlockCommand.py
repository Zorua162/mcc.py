from command import Command


class UpdateCommandBlockCommand(Command):
    def __init__(self):
        super().__init__("UpdateCommandBlock", parameters)
        self.parameters = parameters
