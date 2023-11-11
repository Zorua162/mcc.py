from command import Command


class SelectTradeCommand(Command):
    def __init__(self):
        super().__init__("SelectTrade")
        self.parameters = ['SelectTrade', 'selectedSlot', 'UpdateCommandBlock']
