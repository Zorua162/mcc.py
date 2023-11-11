from command import Command


class DisconnectAndExitCommand(Command):
    def __init__(self):
        super().__init__("DisconnectAndExit")
        self.parameters = ['DisconnectAndExit', 'RunScript']
