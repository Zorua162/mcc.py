from command import Command


class GetEntityHandlingEnabledCommand(Command):
    def __init__(self):
        super().__init__("GetEntityHandlingEnabled", parameters)
        self.parameters = parameters
