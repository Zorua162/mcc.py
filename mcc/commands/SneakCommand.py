from command import Command


class SneakCommand(Command):
    def __init__(self):
        super().__init__("Sneak")
        self.parameters = ['Sneak', 'toggle', 'SendEntityAction']
