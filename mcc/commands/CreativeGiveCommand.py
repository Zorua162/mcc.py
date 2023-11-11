from command import Command


class CreativeGiveCommand(Command):
    def __init__(self):
        super().__init__("CreativeGive")
        self.parameters = ['CreativeGive', 'slot', 'itemType', 'ItemType', 'count', 'nbt', 'CreativeDelete']
