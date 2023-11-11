from command import Command


class SetSlotCommand(Command):
    def __init__(self):
        super().__init__("SetSlot")
        self.parameters = ['SetSlot', 'slotId', 'GetWorld']
