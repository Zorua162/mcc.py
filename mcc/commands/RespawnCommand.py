from mcc.command import Command


class RespawnCommand(Command):
    def __init__(self, parameters):
        super().__init__("Respawn", parameters)
