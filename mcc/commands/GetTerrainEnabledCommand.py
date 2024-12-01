from mcc.command import Command


class GetTerrainEnabledCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetTerrainEnabled", parameters)
