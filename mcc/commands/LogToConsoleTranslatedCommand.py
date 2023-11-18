from mcc.command import Command


class LogToConsoleTranslatedCommand(Command):
    def __init__(self, parameters):
        super().__init__("LogToConsoleTranslated", parameters)
