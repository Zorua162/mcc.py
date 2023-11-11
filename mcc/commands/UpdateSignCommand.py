from command import Command


class UpdateSignCommand(Command):
    def __init__(self):
        super().__init__("UpdateSign", parameters)
        self.parameters = parameters
