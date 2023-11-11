from command import Command


class MoveToLocationCommand(Command):
    def __init__(self):
        super().__init__("MoveToLocation")
        self.parameters = ['MoveToLocation', 'X', 'Y', 'Z', 'allowUnsafe', 'allowDirectTeleport', 'maxOffset', 'minOfset', 'ClientIsMoving']
