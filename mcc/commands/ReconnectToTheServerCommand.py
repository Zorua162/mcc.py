from command import Command


class ReconnectToTheServerCommand(Command):
    def __init__(self):
        super().__init__("ReconnectToTheServer", parameters)
        self.parameters = parameters
