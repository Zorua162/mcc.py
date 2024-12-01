from mcc.command import Command


class RunScriptCommand(Command):
    def __init__(self, parameters):
        super().__init__("RunScript", parameters)
