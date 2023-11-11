from command import Command


class GetInventoriesCommand(Command):
    def __init__(self):
        super().__init__("GetInventories", parameters)
        self.parameters = parameters
