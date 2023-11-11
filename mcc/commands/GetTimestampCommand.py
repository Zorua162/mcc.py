from command import Command


class GetTimestampCommand(Command):
    def __init__(self):
        super().__init__("GetTimestamp", parameters)
        self.parameters = parameters
