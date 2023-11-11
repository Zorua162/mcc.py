from command import Command


class GetPlayerInventoryCommand(Command):
    def __init__(self):
        super().__init__("GetPlayerInventory")
        self.parameters = ['GetPlayerInventory', 'json encoded inventory/container object', 'GetInventories']
