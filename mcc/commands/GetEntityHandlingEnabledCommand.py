from mcc.command import Command


class GetEntityHandlingEnabledCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetEntityHandlingEnabled", parameters)
