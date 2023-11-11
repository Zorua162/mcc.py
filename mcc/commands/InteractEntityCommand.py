from command import Command


class InteractEntityCommand(Command):
    def __init__(self):
        super().__init__("InteractEntity", parameters)
        self.parameters = parameters
