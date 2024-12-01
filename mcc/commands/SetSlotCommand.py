from mcc.command import Command


class SetSlotCommand(Command):
    def __init__(self, parameters):
        super().__init__("SetSlot", parameters)
