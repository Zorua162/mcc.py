from mcc.command import Command


class GetCurrentLocationCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetCurrentLocation", parameters)
