from command import Command


class LogToConsoleTranslatedCommand(Command):
    def __init__(self):
        super().__init__("LogToConsoleTranslated", parameters)
        self.parameters = parameters
