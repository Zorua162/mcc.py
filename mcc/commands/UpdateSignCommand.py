from command import Command


class UpdateSignCommand(Command):
    def __init__(self):
        super().__init__("UpdateSign")
        self.parameters = ['UpdateSign', 'X', 'Y', 'Z', 'line1', 'line2', 'line3', 'line4', 'SelectTrade']
