from mcc.command import Command


class SendAnimationCommand(Command):
    def __init__(self, parameters):
        super().__init__("SendAnimation", parameters)
