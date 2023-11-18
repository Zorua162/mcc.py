from mcc.command import Command


class GetOnlinePlayersCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetOnlinePlayers", parameters)
