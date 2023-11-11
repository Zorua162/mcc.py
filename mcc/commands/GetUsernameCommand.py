from command import Command


class GetUsernameCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetUsername")
        self.parameters = parameters
