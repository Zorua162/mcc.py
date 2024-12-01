from mcc.command import Command


class GetCurrentSlotCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetCurrentSlot", parameters)
