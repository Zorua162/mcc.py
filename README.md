
# mcc.py

A Python module for controlling Minecraft Console Client Webhook bots

## Getting started

Currently an example script is provided as "example.py", it has very limited usage
currently and is only able to send commands and receive their responses

## Design

Interface roughly based on [MCC.JS](https://github.com/milutinke/MCC.js)

### Dealing with concurrency

There are effectively two queues, one for sending messages and one for receiving them
They are not designed to be directly accessed, and have methods to allow for
interacting with them in a way that is easier to use.

## EXPERIMENTAL

This library is currently purely experimental, as it relies on experimental
features of Minecraft Console Client. It may break with no warning due to
changes that are not under the control of the maintainer.

My main goal is to play with the technologies and ideas, so this repo may not
be maintained in the future.

## Commands

To save time the command are auto generated from the Minecraft-Console-Client docs,
using `generate_commands.py`.

## Useful links

Documentation that proved useful:
[https://websockets.readthedocs.io/en/stable/index.html](https://websockets.readthedocs.io/en/stable/index.html)
