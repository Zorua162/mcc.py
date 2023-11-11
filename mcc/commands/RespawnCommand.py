from command import Command


class RespawnCommand(Command):
    def __init__(self):
        super().__init__("Respawn")
        self.parameters = ['Respawn', 'GetProtocolVersion']
