from command import Command


class GetInventoryEnabledCommand(Command):
    def __init__(self):
        super().__init__("GetInventoryEnabled")
        self.parameters = ['GetInventoryEnabled', 'GetPlayerInventory']
