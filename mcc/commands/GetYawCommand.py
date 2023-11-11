from command import Command


class GetYawCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetYaw")
        self.parameters = parameters
