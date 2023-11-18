from mcc.command import Command


class DigBlockCommand(Command):
    def __init__(self, parameters):
        super().__init__("DigBlock", parameters)
