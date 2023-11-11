from command import Command


class SendEntityActionCommand(Command):
    def __init__(self):
        super().__init__("SendEntityAction")
        self.parameters = ['SendEntityAction', 'actionType', 'EntityActionType', 'DigBlock']
