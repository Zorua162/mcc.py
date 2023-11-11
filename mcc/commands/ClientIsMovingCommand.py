from command import Command


class ClientIsMovingCommand(Command):
    def __init__(self, parameters):
        super().__init__("ClientIsMoving")
        self.parameters = parameters
