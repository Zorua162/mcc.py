from command import Command


class LogToConsoleCommand(Command):
    def __init__(self):
        super().__init__("LogToConsole", parameters)
        self.parameters = parameters
