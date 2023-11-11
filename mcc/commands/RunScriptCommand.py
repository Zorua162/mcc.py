from command import Command


class RunScriptCommand(Command):
    def __init__(self):
        super().__init__("RunScript")
        self.parameters = ['RunScript', 'scriptName', 'GetTerrainEnabled']
