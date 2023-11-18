from mcc.command import Command


class SneakCommand(Command):
    def __init__(self, parameters):
        super().__init__("Sneak", parameters)
