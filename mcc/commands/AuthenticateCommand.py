from mcc.command import Command


class AuthenticateCommand(Command):
    def __init__(self, parameters):
        super().__init__("Authenticate", parameters)
