from command import Command


class SetTerrainEnabledCommand(Command):
    def __init__(self, parameters):
        super().__init__("SetTerrainEnabled")
        self.parameters = parameters
