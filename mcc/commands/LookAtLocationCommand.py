from command import Command


class LookAtLocationCommand(Command):
    def __init__(self, parameters):
        super().__init__("LookAtLocation")
        self.parameters = parameters
