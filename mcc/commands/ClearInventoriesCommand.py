from command import Command


class ClearInventoriesCommand(Command):
    def __init__(self):
        super().__init__("ClearInventories")
        self.parameters = ['ClearInventories', 'UpdateSign']
