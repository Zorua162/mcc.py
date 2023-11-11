from command import Command


class GetMaxChatMessageLengthCommand(Command):
    def __init__(self, parameters):
        super().__init__("GetMaxChatMessageLength")
        self.parameters = parameters
