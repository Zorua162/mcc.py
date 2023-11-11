from command import Command


class GetCurrentSlotCommand(Command):
    def __init__(self):
        super().__init__("GetCurrentSlot")
        self.parameters = ['GetCurrentSlot', 'ClearInventories']
