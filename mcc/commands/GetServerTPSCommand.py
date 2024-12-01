from mcc.command import Command


class GetServerTPSCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetServerTPS", parameters)
