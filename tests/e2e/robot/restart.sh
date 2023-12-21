#!/bin/bash -x
start=$(date +%s)
set -e
set -o pipefail
podman-compose down
# podman-compose build
# podman build . -t localhost/robot_mcc_tests:latest
podman-compose up


end=$(date +%s)
runtime=$((end-start))
runtime_out=$(date -d@$runtime -u +%H:%M:%S)
echo Total runtime was "$runtime_out" seconds
