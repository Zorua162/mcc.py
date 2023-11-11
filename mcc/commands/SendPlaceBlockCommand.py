from command import Command


class SendPlaceBlockCommand(Command):
    def __init__(self):
        super().__init__("SendPlaceBlock", parameters)
        self.parameters = parameters
