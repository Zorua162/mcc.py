from command import Command


class SetTerrainEnabledCommand(Command):
    def __init__(self):
        super().__init__("SetTerrainEnabled")
        self.parameters = ['SetTerrainEnabled', 'enabled', 'GetEntityHandlingEnabled']
