from command import Command


class UpdateCommandBlockCommand(Command):
    def __init__(self):
        super().__init__("UpdateCommandBlock")
        self.parameters = ['UpdateCommandBlock', 'X', 'Y', 'Z', 'command', 'mode', 'CommandBlockMode', 'flags', 'CommandBlockFlags', 'CloseInventory']
