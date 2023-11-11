from command import Command


class LogDebugToConsoleCommand(Command):
    def __init__(self):
        super().__init__("LogDebugToConsole", parameters)
        self.parameters = parameters
