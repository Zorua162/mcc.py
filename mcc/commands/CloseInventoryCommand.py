from command import Command


class CloseInventoryCommand(Command):
    def __init__(self):
        super().__init__("CloseInventory")
        self.parameters = ['CloseInventory', 'windowId', 'GetMaxChatMessageLength']
