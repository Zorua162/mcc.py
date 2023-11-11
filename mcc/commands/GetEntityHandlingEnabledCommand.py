from command import Command


class GetEntityHandlingEnabledCommand(Command):
    def __init__(self):
        super().__init__("GetEntityHandlingEnabled")
        self.parameters = ['GetEntityHandlingEnabled', 'Sneak']
