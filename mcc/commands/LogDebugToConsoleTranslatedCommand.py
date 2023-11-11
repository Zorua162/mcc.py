from command import Command


class LogDebugToConsoleTranslatedCommand(Command):
    def __init__(self):
        super().__init__("LogDebugToConsoleTranslated", parameters)
        self.parameters = parameters
