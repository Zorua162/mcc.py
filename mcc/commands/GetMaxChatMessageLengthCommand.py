from command import Command


class GetMaxChatMessageLengthCommand(Command):
    def __init__(self):
        super().__init__("GetMaxChatMessageLength", parameters)
        self.parameters = parameters
