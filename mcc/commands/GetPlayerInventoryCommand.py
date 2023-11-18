from mcc.command import Command


class GetPlayerInventoryCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetPlayerInventory", parameters)
