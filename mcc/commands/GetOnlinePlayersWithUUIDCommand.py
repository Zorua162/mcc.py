from mcc.command import Command


class GetOnlinePlayersWithUUIDCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetOnlinePlayersWithUUID", parameters)
