from command import Command


class ChangeSessionIdCommand(Command):
    def __init__(self):
        super().__init__("ChangeSessionId")
        self.parameters = ['LogToConsole']
