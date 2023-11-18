#!/bin/bash
set -e
set -o pipefail
podman-compose down
# podman-compose build
podman build . -t localhost/robot_mcc_tests:latest
podman-compose up
