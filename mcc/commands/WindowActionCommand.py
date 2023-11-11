from command import Command


class WindowActionCommand(Command):
    def __init__(self):
        super().__init__("WindowAction")
        self.parameters = ['WindowAction', 'windowId', 'slotId', 'windowActionType', 'WindowActionType', 'ChangeSlot']
