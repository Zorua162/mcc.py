from command import Command


class GetInventoriesCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetInventories")
        self.parameters = parameters
