from mcc.command import Command


class LogToConsoleCommand(Command):
    def __init__(self, parameters):
        super().__init__("LogToConsole", parameters)
