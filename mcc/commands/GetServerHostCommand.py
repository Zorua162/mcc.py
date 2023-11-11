from command import Command


class GetServerHostCommand(Command):
    def __init__(self):
        super().__init__("GetServerHost")
        self.parameters = ['GetServerHost', 'GetUsername']
