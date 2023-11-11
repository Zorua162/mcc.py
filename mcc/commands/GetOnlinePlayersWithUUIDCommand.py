from command import Command


class GetOnlinePlayersWithUUIDCommand(Command):
    def __init__(self):
        super().__init__("GetOnlinePlayersWithUUID")
        self.parameters = ['GetOnlinePlayersWithUUID', 'GetServerTPS']
