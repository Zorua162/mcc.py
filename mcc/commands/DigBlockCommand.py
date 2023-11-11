from command import Command


class DigBlockCommand(Command):
    def __init__(self):
        super().__init__("DigBlock")
        self.parameters = ['DigBlock', 'X', 'Y', 'Z', 'swingArms', 'lookAtBlock', 'SetSlot']
