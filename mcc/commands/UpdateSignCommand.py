from mcc.command import Command


class UpdateSignCommand(Command):
    def __init__(self, parameters):
        super().__init__("UpdateSign", parameters)
