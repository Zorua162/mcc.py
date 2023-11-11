from command import Command


class GetServerTPSCommand(Command):
    def __init__(self):
        super().__init__("GetServerTPS")
        self.parameters = ['GetServerTPS', 'InteractEntity']
