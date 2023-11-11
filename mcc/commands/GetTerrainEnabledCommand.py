from command import Command


class GetTerrainEnabledCommand(Command):
    def __init__(self):
        super().__init__("GetTerrainEnabled", parameters)
        self.parameters = parameters
