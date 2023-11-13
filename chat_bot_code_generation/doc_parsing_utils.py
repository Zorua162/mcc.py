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
        line for line in command_data if "**Description**" not in line and line != ""
    ]
    return command_data[1].strip(" ")


def get_parameters(command_data: list) -> list[str]:
    """Get the command's parameters"""
    parameters = [
        regex_string(backtick_search, line) for line in command_data if "-" in line
    ]
    return [parameter for parameter in parameters if parameter is not None]


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
