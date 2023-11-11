from command import Command


class ChangeSlotCommand(Command):
    def __init__(self):
        super().__init__("ChangeSlot", parameters)
        self.parameters = parameters
