from command import Command


class SetSlotCommand(Command):
    def __init__(self):
        super().__init__("SetSlot", parameters)
        self.parameters = parameters
