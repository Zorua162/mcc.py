from command import Command


class ClientIsMovingCommand(Command):
    def __init__(self):
        super().__init__("ClientIsMoving")
        self.parameters = ['ClientIsMoving', 'LookAtLocation']
