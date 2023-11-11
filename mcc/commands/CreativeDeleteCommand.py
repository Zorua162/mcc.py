from command import Command


class CreativeDeleteCommand(Command):
    def __init__(self):
        super().__init__("CreativeDelete")
        self.parameters = ['CreativeDelete', 'slot', 'SendAnimation']
