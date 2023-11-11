from command import Command


class LookAtLocationCommand(Command):
    def __init__(self):
        super().__init__("LookAtLocation", parameters)
        self.parameters = parameters
