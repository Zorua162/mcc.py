from command import Command


class AuthenticateCommand(Command):
    def __init__(self):
        super().__init__("Authenticate", parameters)
        self.parameters = parameters
