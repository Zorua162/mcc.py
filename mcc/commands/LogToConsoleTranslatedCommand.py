from command import Command


class LogToConsoleTranslatedCommand(Command):
    def __init__(self):
        super().__init__("LogToConsoleTranslated")
        self.parameters = ['LogToConsoleTranslated', 'message', 'LogDebugToConsoleTranslated']
