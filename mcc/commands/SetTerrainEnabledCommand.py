from mcc.command import Command


class SetTerrainEnabledCommand(Command):
    def __init__(self, parameters):
        super().__init__("SetTerrainEnabled", parameters)
