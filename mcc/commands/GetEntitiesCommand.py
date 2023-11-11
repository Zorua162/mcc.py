from command import Command


class GetEntitiesCommand(Command):
    def __init__(self):
        super().__init__("GetEntities")
        self.parameters = ['GetEntities', 'GetPlayersLatency']
