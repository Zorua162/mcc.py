from mcc.command import Command


class GetPlayersLatencyCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetPlayersLatency", parameters)
