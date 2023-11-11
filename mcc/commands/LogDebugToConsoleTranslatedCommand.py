from command import Command


class LogDebugToConsoleTranslatedCommand(Command):
    def __init__(self, parameters):
        super().__init__("LogDebugToConsoleTranslated")
        self.parameters = parameters
