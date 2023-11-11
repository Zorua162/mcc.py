from command import Command


class ChangeSlotCommand(Command):
    def __init__(self, parameters):
        super().__init__("ChangeSlot")
        self.parameters = parameters
