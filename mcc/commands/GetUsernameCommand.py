from command import Command


class GetUsernameCommand(Command):
    def __init__(self):
        super().__init__("GetUsername", parameters)
        self.parameters = parameters
