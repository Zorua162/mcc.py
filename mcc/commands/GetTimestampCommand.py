from command import Command


class GetTimestampCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetTimestamp")
        self.parameters = parameters
