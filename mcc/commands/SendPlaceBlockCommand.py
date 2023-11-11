from command import Command


class SendPlaceBlockCommand(Command):
    def __init__(self, parameters):
        super().__init__("SendPlaceBlock")
        self.parameters = parameters
