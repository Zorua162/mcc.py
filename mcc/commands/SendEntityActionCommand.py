from mcc.command import Command


class SendEntityActionCommand(Command):
    def __init__(self, parameters):
        super().__init__("SendEntityAction", parameters)
