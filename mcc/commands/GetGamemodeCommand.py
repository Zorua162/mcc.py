from command import Command


class GetGamemodeCommand(Command):
    def __init__(self):
        super().__init__("GetGamemode", parameters)
        self.parameters = parameters
