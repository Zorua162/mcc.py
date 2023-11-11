from command import Command


class SendPlaceBlockCommand(Command):
    def __init__(self):
        super().__init__("SendPlaceBlock")
        self.parameters = ['SendPlaceBlock', 'X', 'Y', 'Z', 'direction', 'Direction', 'hand', 'Hand', 'UseItemInHand']
