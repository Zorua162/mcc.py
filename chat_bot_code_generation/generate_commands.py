# Generate the classes for commands based on the Minecraft-Console-Client source code

# The docs are used as the main source, but we also extract command names
# from the source code and output any that are missing from the docs

import json
import os
from doc_parsing_utils import CommandData, parse_doc_commands


# Paths
commands_folder = "../mcc/commands"
path_to_source: str = (
    "../minecraft-console-client-source/MinecraftClient/ChatBots/WebSocketBot.cs"
)
path_to_docs: str = (
    "../minecraft-console-client-source/docs/guide/websocket/Commands.md"
)

command_template_path: str = "./command_template.txt"
json_out_path = "./generate_commands_output.json"


def tidy_line(line: str) -> str:
    line = line.strip(" ").replace(":", "").replace('"', "").replace("case ", "")
    return line


print("Collecting all the commands from the WebSocketBot.cs file...")

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
with open(path_to_docs) as f_obj:
    data = f_obj.read().split("\n")
    docs_commands: list[CommandData] = parse_doc_commands(data)


print(f"Found {len(docs_commands)} commands in the docs")

doc_data: dict = {"CommandData": [command.as_dict() for command in docs_commands]}

with open(json_out_path, "w") as f_obj:
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
        # Skip over folders or any non Command.py files
        if "Command.py" not in file_name:
            continue
        os.remove(f"{commands_folder}/{file_name}")

    with open(command_template_path, "r") as f_obj:
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
