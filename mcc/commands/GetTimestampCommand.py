from command import Command


class GetTimestampCommand(Command):
    def __init__(self):
        super().__init__("GetTimestamp")
        self.parameters = ['GetTimestamp', 'yyyy-MM-dd HH:mm:ss', 'GetServerPort']
