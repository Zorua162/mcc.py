import re
from typing import Optional

backtick_search = r"`(.*?)`"


class CommandData:
    name: str
    description: str
    parameters: list[str]
    return_type: Optional[str]

    def __init__(
        self,
        name: str,
        description: str,
        parameters: list[str],
        return_type: Optional[str],
    ):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.return_type = return_type

    def as_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters,
            "return_type": self.return_type,
        }


class EventParameter:
    name: str
    parameter_type: str

    def __init__(self, name, parameter_type):
        self.name = name
        self.parameter_type = parameter_type

    def as_dict(self):
        return {"name": self.name, "type": self.parameter_type}


class EventData:
    name: str
    description: str
    parameters: list[EventParameter]

    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters

    def as_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": [parameter.as_dict() for parameter in self.parameters],
        }


def regex_string(pattern: str, data: str) -> Optional[str]:
    """Regex's a string, errors if nothing was found"""
    results = re.finditer(pattern, data)
    # Only return the first result
    for result in results:
        return result.group()[1:-1]
    return None


def get_name(command_data: list) -> str:
    """Get the command name from the command data"""
    name = regex_string(backtick_search, command_data[0])
    if name is None:
        raise Exception("Name was none")
    return name


def get_description(command_data: list) -> str:
    """Get the command's description"""
    command_data = [
        line
        for line in command_data
        if "**Description**" not in line
        and "**Description:**" not in line
        and line != "  "
        and line != ""
    ]
    return command_data[1].strip(" ")


def get_parameters(command_data: list) -> list[str]:
    """Get the command's parameters"""
    parameters = [
        regex_string(backtick_search, line) for line in command_data if "-" in line
    ]
    return [parameter for parameter in parameters if parameter is not None]


def get_event_parameters(event_data: list[str]) -> list[EventParameter]:
    """Event parameter names and types are in backticks"""
    parameter_names = [
        regex_string(backtick_search, line) for line in event_data if "-" in line
    ]

    parameter_types = [
        regex_string(backtick_search, line)
        for line in event_data
        if "**Type:**" in line
    ]
    event_parameters = [
        EventParameter(name, types)
        for name, types in zip(parameter_names, parameter_types)
    ]
    return event_parameters


def get_return_type(command_data: list) -> Optional[str]:
    """Get the command's return type"""
    possible_values = [
        regex_string(backtick_search, line)
        for line in command_data
        if "Return type" in line
    ]
    return_value: Optional[str] = None
    if len(possible_values) > 0:
        return_value = possible_values[0]
    return return_value


def parse_doc_command_data(command_data: list[str]) -> CommandData:
    """Parse out the data from the list of command data"""
    # Remove lines that have **Description** for consistency
    name: str = get_name(command_data)
    description: str = get_description(command_data)
    parameters: list[str] = get_parameters(command_data)
    return_type: Optional[str] = get_return_type(command_data)
    return CommandData(name, description, parameters, return_type)


def parse_doc_event_data(event_data: list[str]) -> EventData:
    name: str = get_name(event_data)
    description: str = get_description(event_data)
    parameters: list[EventParameter] = get_event_parameters(event_data)
    return EventData(name, description, parameters)


def parse_doc_commands(data: list[str]) -> list[CommandData]:
    # print(data)
    # Create initial command (line there for completeness, but gets discarded later)
    docs_commands: list[CommandData] = []
    current_command: list[str] = [data[0]]
    for line in data:
        # If the line starts with ### then save that command, otherwise current command
        # print(line[0:3])
        current_command.append(line)
        if line[0:3] == "###":
            if current_command[0][0:3] != "# W":
                docs_commands.append(parse_doc_command_data(current_command))
            current_command = [line]
    return docs_commands


def parse_doc_events(data: list[str]) -> list[EventData]:
    docs_events: list[EventData] = []
    current_event: list[str] = [data[0]]
    for line in data:
        current_event.append(line)
        if line[0:2] == "##":
            if current_event[0][0:3] != "# W":
                docs_events.append(parse_doc_event_data(current_event))
            current_event = [line]

    return docs_events
