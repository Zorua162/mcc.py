from command import Command


class ClientIsMovingCommand(Command):
    def __init__(self):
        super().__init__("ClientIsMoving", parameters)
        self.parameters = parameters
