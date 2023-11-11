from command import Command


class RunScriptCommand(Command):
    def __init__(self, parameters):
        super().__init__("RunScript")
        self.parameters = parameters
