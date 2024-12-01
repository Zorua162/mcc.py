from mcc.command import Command


class SendPlaceBlockCommand(Command):
    def __init__(self, parameters):
        super().__init__("SendPlaceBlock", parameters)
