# Run the RobotFramework tests against a live server and client
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
while [[ $waiting == true ]]; do
    sleep $time_wait
    count=$((count + 1))

    echo "Checking container health $count/$timeout"

    # Check container health
    server_status=$(podman container inspect -f "{{.State.Health.Status}}" \
                    $container_name)
    if [[ $server_status == "healthy" ]]; then
        echo "Server is available to connect to so exiting"
        waiting=false
    fi
    echo "Server ouput was $server_status"


    # Timeout check
    if [[ $count -ge $timeout ]]; then
        echo "Timed out waiting for container to be healthy"
        total_wait=$((time_wait*timeout))
        echo "Waited $total_wait seconds"
        exit 1
    fi
done

# Startup the MCC client
podman-compose -f ./MCC/compose.yml up -d
# Wait 5 seconds for the MCC client to be fully loaded
sleep 5
# Run the RobotFramework tests
# robot --pythonpath ../../:../../mcc/ .
podman-compose -f ./robot/compose.yml up
