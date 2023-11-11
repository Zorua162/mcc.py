from command import Command


class GetPlayerInventoryCommand(Command):
    def __init__(self):
        super().__init__("GetPlayerInventory", parameters)
        self.parameters = parameters
