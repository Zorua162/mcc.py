from command import Command


class GetInventoryEnabledCommand(Command):
    def __init__(self):
        super().__init__("GetInventoryEnabled", parameters)
        self.parameters = parameters
