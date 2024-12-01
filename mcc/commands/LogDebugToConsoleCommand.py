from mcc.command import Command


class LogDebugToConsoleCommand(Command):
    def __init__(self, parameters):
        super().__init__("LogDebugToConsole", parameters)
