from command import Command


class GetServerHostCommand(Command):
    def __init__(self):
        super().__init__("GetServerHost", parameters)
        self.parameters = parameters
