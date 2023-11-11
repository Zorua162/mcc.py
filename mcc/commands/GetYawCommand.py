from command import Command


class GetYawCommand(Command):
    def __init__(self):
        super().__init__("GetYaw", parameters)
        self.parameters = parameters
