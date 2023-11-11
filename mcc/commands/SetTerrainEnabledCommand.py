from command import Command


class SetTerrainEnabledCommand(Command):
    def __init__(self):
        super().__init__("SetTerrainEnabled", parameters)
        self.parameters = parameters
