from command import Command


class ClearInventoriesCommand(Command):
    def __init__(self):
        super().__init__("ClearInventories", parameters)
        self.parameters = parameters
