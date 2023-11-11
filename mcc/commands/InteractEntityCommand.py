from command import Command


class InteractEntityCommand(Command):
    def __init__(self):
        super().__init__("InteractEntity")
        self.parameters = ['InteractEntity', 'entityId', 'interactionType', 'InteractType', 'hand', 'Hand', 'CreativeGive']
