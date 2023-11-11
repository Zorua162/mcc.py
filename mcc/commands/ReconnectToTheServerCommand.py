from command import Command


class ReconnectToTheServerCommand(Command):
    def __init__(self):
        super().__init__("ReconnectToTheServer")
        self.parameters = ['ReconnectToTheServer', 'extraAttempts', 'delaySeconds', 'DisconnectAndExit']
