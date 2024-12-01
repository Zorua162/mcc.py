from mcc.command import Command


class SelectTradeCommand(Command):
    def __init__(self, parameters):
        super().__init__("SelectTrade", parameters)
