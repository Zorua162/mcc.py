from command import Command


class GetOnlinePlayersWithUUIDCommand(Command):
    def __init__(self):
        super().__init__("GetOnlinePlayersWithUUID", parameters)
        self.parameters = parameters
