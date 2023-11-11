from command import Command


class SendAnimationCommand(Command):
    def __init__(self):
        super().__init__("SendAnimation")
        self.parameters = ['SendAnimation', 'hand', 'Hand', 'SendPlaceBlock']
