from command import Command


class GetServerPortCommand(Command):
    def __init__(self):
        super().__init__("GetServerPort", parameters)
        self.parameters = parameters
