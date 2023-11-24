# End to end tests

## Setup

Ensure your container runtime supports health-check. On WSL2 Ubuntu, I had to
enable systemd to ensure this would work.

As a pre-requisite, the main distribution container needs to be build. The
script to do this can be found at `mcc.py/build_container.sh`. Currently it
uses podman, as that is my preference, but you can change this out to be
docker if that is what you use and everything should work the same.

## Running

Change directory to `mcc.py/tests/e2e`

Run the file `run_tests.sh` from this folder

Wait for the tests to run

If you are running the tests after a previous test run, or just wish to cleanup the
resources that are created to run the tests then use the command
`./cleanup_resources.sh`.

## Process

Within `mcc.py/tests/e2e` are three container compose files, which orchestrate
setting up a full end to end environment for testing this MCC bot. Therefore
these tests are run in the exact same type of environment that they are
recommended to be used for.

The script starts by creating a minecraft server, this uses the
docker-minecraft-server image, more can be found out about this image
[here](https://docker-minecraft-server.readthedocs.io/en/latest/).

A script then checks the health of the server container and waits for it to
be "healthy" (or untill it times out waiting).

Once the server is ready the MCC image is launched, as we are using a custom
edited binary with some fixes to the WebHook bot in we have this setup to not
re-download the binary currently. Hopefully, once the fixes are accepted, we
can disable this in the future.

The script waits 5 seconds for the MCC client to be loaded (this is overkill,
but better to be safe).

Then it builds a custom Python container where RobotFramework is installed,
this container is based off of the container that is planned to be
distributed as part of this repo.

The container is then run, which runs the Robot tests and the outputs are
sent to the folder `mcc.py/tests/e2e/outputs`.
