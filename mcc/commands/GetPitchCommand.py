from mcc.command import Command


class GetPitchCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetPitch", parameters)
