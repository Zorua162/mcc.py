from command import Command


class RunScriptCommand(Command):
    def __init__(self):
        super().__init__("RunScript", parameters)
        self.parameters = parameters
