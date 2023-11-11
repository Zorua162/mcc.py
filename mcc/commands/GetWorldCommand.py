from command import Command


class GetWorldCommand(Command):
    def __init__(self):
        super().__init__("GetWorld")
        self.parameters = ['GetWorld', 'json encoded object with world info', 'GetEntities']
