from command import Command


class LogToConsoleCommand(Command):
    def __init__(self):
        super().__init__("LogToConsole")
        self.parameters = ['LogToConsole', 'message', 'LogDebugToConsole']
