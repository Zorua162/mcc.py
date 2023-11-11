from command import Command


class DigBlockCommand(Command):
    def __init__(self):
        super().__init__("DigBlock", parameters)
        self.parameters = parameters
