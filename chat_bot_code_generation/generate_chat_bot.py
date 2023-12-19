# Generate the ChatBot.py file and ChatBot class with the latest commands and events
import os
import json

path_to_template = "./chat_bot_template.txt"
path_to_commands = "../mcc/commands"
path_to_events = "./generate_events_output.json"
path_to_chat_bot_file = "../mcc/ChatBot.py"

with open(path_to_template) as f_template:
    chat_bot_class = f_template.read()

# Prepare the list of commands
commands = [
    command[:-3] for command in os.listdir(path_to_commands) if ".py" in command
]

import_commands = "# Import commands\n"
command_methods = "# Command methods\n"
for command in commands:
    import_commands += f"from mcc.commands.{command} import {command}\n"
    command_methods += (
        f"\n    def {command}(self):"
        f"\n        return self.sendCommand({command}())\n"
    )
print(import_commands)


# Prepare the list of events
with open(path_to_events) as f_events:
    events_data = json.load(f_events)

event_method_names = [event["name"] for event in events_data["EventData"]]
event_parameter_names = [
    [parameter["name"] for parameter in event["parameters"]]
    for event in events_data["EventData"]
]

event_methods = "# Event methods\n"
for event, parameters in zip(event_method_names, event_parameter_names):
    print(event)
    print(parameters)

    # Overwrite OnEntityMove to accept list of arguments
    if event == "OnEntityMove":
        parameters = ["*Entity"]

    parameters = [parameter for parameter in parameters if parameter is not None]
    parameters.insert(0, "self")
    parameters_string = ", ".join(parameters)
    event_methods += (
        f"\n    def {event}({parameters_string}):"
        f"\n        # place holder event"
        f"\n        pass\n"
    )


chat_bot_class = chat_bot_class.replace("<<ImportCommands>>", import_commands)

chat_bot_class = chat_bot_class.replace("<<EventMethods>>", event_methods)

chat_bot_class = chat_bot_class.replace("<<CommandMethods>>", command_methods)


with open(path_to_chat_bot_file, "w") as f_out:
    f_out.write(chat_bot_class)
