from command import Command


class GetEntitiesCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetEntities", parameters)
