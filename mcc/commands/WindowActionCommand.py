from mcc.command import Command


class WindowActionCommand(Command):
    def __init__(self, parameters):
        super().__init__("WindowAction", parameters)
