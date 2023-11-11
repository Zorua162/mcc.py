from command import Command


class GetPitchCommand(Command):
    def __init__(self):
        super().__init__("GetPitch")
        self.parameters = ['GetPitch', 'double', 'GetUserUUID']
