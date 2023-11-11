from command import Command


class GetPlayersLatencyCommand(Command):
    def __init__(self):
        super().__init__("GetPlayersLatency", parameters)
        self.parameters = parameters
