# Generate the classes for commands based on the Minecraft-Console-Client source code

# Need to choose between source code and docs
# Source code:
# Pros:
# - Will always be up to date, don't need to rely on someone else's documentation
# Cons:
# - Will be much harder to get the needed data
# Docs
# - Much easier to get the needed data
# Cons:
# - Might not always be up to date

# The list of commands is easy to get from the source code, so maybe we cross
# reference that with the docs (and then we update the docs using this knowledge)

import re
import json
import os
from typing import Optional

backtick_search = r"`(.*?)`"
# Paths
commands_folder = "../mcc/commands"
path_to_source: str = (
    "../minecraft-console-client-source/MinecraftClient/ChatBots/" "WebSocketBot.cs"
)
path_to_docs: str = (
    "../minecraft-console-client-source/docs/guide/websocket/" "Commands.md"
)


def tidy_line(line: str) -> str:
    line = line.strip(" ").replace(":", "").replace('"', "").replace("case ", "")
    return line


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


print("Collecting all the commands form the WebSocketBot.cs file...")

# Get all commands from source
source_commands: list[str] = []
with open(path_to_source) as f_obj:
    data = f_obj.read().split("\n")
# All case statements below line 484 are commands
lines_with_case_in = [line for line in data if "case" in line]
cleaned_lines = [tidy_line(line) for line in lines_with_case_in]
source_commands = cleaned_lines[3:]

source_commands.append("ChangeSessionId")
source_commands.append("Authenticate")
print(f"Found {len(source_commands)} source commands")

# Get all the commands from the docs, used as main source
print("Collecting all the commands from the docs...")


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


commands: list[CommandData] = []
with open(path_to_docs) as f_obj:
    data = f_obj.read().split("\n")
    # print(data)
    docs_commands: list[CommandData] = []
    # Create initial command (line there for completeness, but gets discarded later)
    current_command: list[str] = [data[0]]
    for line in data:
        # If the line starts with ### then save that command, otherwise current command
        # print(line[0:3])
        current_command.append(line)
        if line[0:3] == "###":
            if current_command[0][0:3] != "# W":
                docs_commands.append(parse_doc_command_data(current_command))
            current_command = [line]


print(f"Found {len(docs_commands)} commands in the docs")

doc_data: dict = {"CommandData": []}

for docs_command in docs_commands:
    doc_data["CommandData"].append(docs_command.as_dict())

with open("./generate_commands_output.json", "w") as f_obj:
    # f_obj.writelines(str(doc_data))
    json.dump(doc_data, f_obj, indent=4)

# Compare source_commands and doc_command names, check if any are missing from the docs
doc_command_names = [command["name"] for command in doc_data["CommandData"]]

not_in_doc = [
    command_name
    for command_name in source_commands
    if command_name not in doc_command_names
]

print(f'Commands which are not documented currently: {", ".join(not_in_doc)}')


def create_command_classes(docs_data: dict):
    """Create the Command classes"""
    # Delete the old classes
    for file_name in os.listdir(commands_folder):
        os.remove(f"{commands_folder}/{file_name}")

    with open("./command_template.txt", "r") as f_obj:
        template = f_obj.read()

    for command in docs_data["CommandData"]:
        current_template = template
        current_template = current_template.replace("<<command_name>>", command["name"])

        # Add parameters if they are present
        current_template = current_template.replace(
            "<<parameters>>", str(command["parameters"])
        )
        with open(f'{commands_folder}/{command["name"]}Command.py', "w") as f_obj:
            f_obj.write(current_template)


# Create the command classes
create_command_classes(doc_data)
