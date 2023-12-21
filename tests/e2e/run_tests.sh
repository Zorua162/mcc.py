#!/bin/bash -x
# Run the RobotFramework tests against a live server and client
start=$(date +%s)

# Cleanup old tests
# (Comment out if speed needed, but could cause some settings to not be updated)
podman-compose -f ./server/compose.yml down
podman-compose -f ./mcc/compose.yml down
podman-compose -f ./robot/compose.yml down


# Startup the server
podman-compose -f ./server/compose.yml up -d

# Wait for the server to be ready to join
waiting=true
# Number of times attempted to check server
count=0
# Max number of attempts
timeout=20
# Wait in seconds for each attempt
time_wait=10
# Container name to check
container_name=server_mc_1
echo "Started wait for mc server to be ready"
# Waiting set to false when server is ready
while [[ $waiting == true ]]; do
    count=$((count + 1))

    echo "Checking container health $count/$timeout"

    # Check container health
    server_status=$(podman container inspect -f "{{.State.Health.Status}}" \
                    $container_name)
    container_status=$(podman container inspect -f "{{.State.Status}}" \
                    $container_name)

    # Exit out with error if the status is empty
    if [[ $server_status == "" ]]; then
        echo "Server failed to start"
        exit 1
    fi

    # Exit out with error if the status is empty
    if [[ $container_status == "exited" ]]; then
        echo "Container exited"
	podman logs $container_name
        exit 1
    fi

    # Exit out if the timeout is reached
    if [[ $count -ge $timeout ]]; then
        echo "Server failed to start in time, exiting"
        exit 1
    fi
    echo "Server ouput was $server_status"

    if [[ $server_status == "healthy" ]]; then
        echo "Server is available to connect to so exiting"
        waiting=false
    else
        sleep $time_wait
    fi


    # Timeout check
    # if [[ $count -ge $timeout ]]; then
    #     echo "Timed out waiting for container to be healthy"
    #     total_wait=$((time_wait*timeout))
    #     echo "Waited $total_wait seconds"
    #     exit 1
    # fi
done

# Startup the MCC client
podman-compose -f ./mcc/compose.yml up -d
# Wait 5 seconds for the MCC client to be fully loaded
wait_time=5
echo "Waiting $wait_time seconds for MCC Websocket server to be ready"
sleep $wait_time

# Build the Robotframework test container
cd robot || exit
podman-compose build
# Run the Robotframework tests
podman-compose up

podman logs mcc_mcc_1 > ./output/mcc_mcc_1.log
podman logs server_mc_1 > ./output/server_mc_1.log

end=$(date +%s)
runtime=$((end-start))
runtime_out=$(date -d@$runtime -u +%H:%M:%S)
echo Total runtime was "$runtime_out" seconds
