
# mcc.py

A Python module for controlling Minecraft Console Client Webhook bots

## Getting started

Beforehand note that this library only provides bindings/ for the Minecraft Console
Client WebSocket bot, it does not provide the functionality to connect to a minecraft
server on its own.

You will need to have Minecraft Console Client setup with the "Websocket" bot enabled.
[Installation](https://mccteam.github.io/guide/installation.html)
[Usage](https://mccteam.github.io/guide/usage.html)
It is recommended to run MCC without config, so that the default config file gets
created where you can then set the server ip that you want, and enable the Websocket bot
(at the bottom of the config).

Install this module via pip: `pip install mcc.py`

An example of the usage of this library can be found in the file `example.py`.

For more advanced usage, there are a number of scenarios in the `tests` folder,
including end to end tests which show server, Minecraft Console Client and a Robot
Framework library, which uses mcc.py to control a player on the server that is hosted.
These are run on Github Actions.

## Design

Interface roughly based on [MCC.JS](https://github.com/milutinke/MCC.js)

### Additions to the base design

There are effectively two queues, one for sending messages and one for receiving them
They are not designed to be directly accessed, and have methods to allow for
interacting with them in a way that is easier to use.

## EXPERIMENTAL

This library is currently purely experimental, as it relies on experimental
features of Minecraft Console Client. It may break with no warning due to
changes that are not under the control of the maintainer.

## Useful links

Documentation that proved useful:
[https://websockets.readthedocs.io/en/stable/index.html](https://websockets.readthedocs.io/en/stable/index.html)
