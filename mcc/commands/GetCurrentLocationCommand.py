from command import Command


class GetCurrentLocationCommand(Command):
    def __init__(self):
        super().__init__("GetCurrentLocation")
        self.parameters = ['GetCurrentLocation', 'json encoded Location object', 'MoveToLocation']
