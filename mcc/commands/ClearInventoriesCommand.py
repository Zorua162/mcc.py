from command import Command


class ClearInventoriesCommand(Command):
    def __init__(self, parameters):
        super().__init__("ClearInventories")
        self.parameters = parameters
