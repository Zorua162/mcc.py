from command import Command


class GetInventoriesCommand(Command):
    def __init__(self):
        super().__init__("GetInventories")
        self.parameters = ['GetInventories', 'json encoded array of inventory/container objects', 'WindowAction']
