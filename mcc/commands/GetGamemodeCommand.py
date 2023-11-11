from command import Command


class GetGamemodeCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetGamemode")
        self.parameters = parameters
