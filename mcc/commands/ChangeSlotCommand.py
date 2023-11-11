from command import Command


class ChangeSlotCommand(Command):
    def __init__(self):
        super().__init__("ChangeSlot")
        self.parameters = ['ChangeSlot', 'slotId', 'GetCurrentSlot']
