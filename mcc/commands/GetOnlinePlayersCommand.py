from command import Command


class GetOnlinePlayersCommand(Command):
    def __init__(self):
        super().__init__("GetOnlinePlayers")
        self.parameters = ['GetOnlinePlayers', 'GetOnlinePlayersWithUUID']
