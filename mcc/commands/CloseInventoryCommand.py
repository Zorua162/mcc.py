from mcc.command import Command


class CloseInventoryCommand(Command):
    def __init__(self, parameters):
        super().__init__("CloseInventory", parameters)
