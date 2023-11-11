from command import Command


class ChangeSessionIdCommand(Command):
    def __init__(self, parameters):
        super().__init__("ChangeSessionId")
        self.parameters = parameters
