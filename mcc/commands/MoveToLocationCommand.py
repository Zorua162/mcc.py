from command import Command


class MoveToLocationCommand(Command):
    def __init__(self):
        super().__init__("MoveToLocation", parameters)
        self.parameters = parameters
