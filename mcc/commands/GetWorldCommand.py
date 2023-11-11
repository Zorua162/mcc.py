from command import Command


class GetWorldCommand(Command):
    def __init__(self):
        super().__init__("GetWorld", parameters)
        self.parameters = parameters
