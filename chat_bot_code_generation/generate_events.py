# Generate a lists of events and save to events.json
# This is reused by generate_chatbot.py to create the base chat bot class
import re
import json
from doc_parsing_utils import EventData, parse_doc_events
from typing import Optional

quote_search = r'"(.*?)"'
curly_search = r"{(.*?)}"
# Paths
path_out = "events.json"
path_to_source = (
    "../minecraft-console-client-source/MinecraftClient/ChatBots/WebSocketBot.cs"
)
path_to_docs = "../minecraft-console-client-source/docs/guide/websocket/Events.md"
json_out_path = "./generate_events_output.json"


def find_heading_line(heading: str, data: list) -> Optional[int]:
    for i, line in enumerate(data):
        if heading in line:
            return i
    return None


# Get events from source code
with open(path_to_source) as f_obj:
    data = f_obj.read().split("\n")
    # We want everything between Bot Events and Helper methods
    bot_events_heading_line = find_heading_line("Bot Events", data)
    helper_methods_heading_line = find_heading_line("Helper methods", data)
    # print(f"Bot Events line: {bot_events_heading_line} \n"
    #       f"Helper Methods line {helper_methods_heading_line}")
    truncated_data = data[bot_events_heading_line:helper_methods_heading_line]
    # print(f"Truncated data: {truncated_data}")
    # Get every line that has "SendEvent"
    send_event_lines = [line for line in truncated_data if "SendEvent" in line]
    # print(f"Send Event Lines: {send_event_lines}")
    event_names = [
        next(re.finditer(quote_search, lines)).group()[1:-1]
        for lines in send_event_lines
    ]
    event_names.append("OnGameJoined")
    # print(f"Event Names: {event_names}")
    # Cut them out of the js code
    # event_parameters_raw = [
    #     "".join(param.group()[2:-2] for param in re.finditer(curly_search, lines))
    #     for lines in send_event_lines
    # ]

    # event_parameters: list[list[str]] = [
    #     params.split(", ") for params in event_parameters_raw
    # ]

    # print(f"Event Parameters {event_parameters}")

# Get events from docs, used as main source
with open(path_to_docs) as f_obj:
    data = f_obj.read().split("\n")
docs_events: list[EventData] = parse_doc_events(data)

doc_event_data: dict = {"EventData": [event.as_dict() for event in docs_events]}

with open(json_out_path, "w") as f_out:
    json.dump(doc_event_data, f_out, indent=4)


# Compare the two to find events which aren't in the docs
doc_event_names = [event["name"] for event in doc_event_data["EventData"]]

not_in_doc = [
    event_name for event_name in event_names if event_name not in doc_event_names
]

print(f'Events which are not documented currently: {", ".join(not_in_doc)}')
# Generated events will be created in ChatBot.py, so this is handled by
# generate_chat_bot.py script, which also adds the command methods
