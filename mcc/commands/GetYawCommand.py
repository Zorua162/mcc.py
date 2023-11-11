from command import Command


class GetYawCommand(Command):
    def __init__(self):
        super().__init__("GetYaw")
        self.parameters = ['GetYaw', 'GetPitch']
