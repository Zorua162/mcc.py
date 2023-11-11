from command import Command


class GetInventoryEnabledCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetInventoryEnabled")
        self.parameters = parameters
