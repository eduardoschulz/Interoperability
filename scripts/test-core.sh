#!/bin/bash

name=("Open5GS", "OAI", "Free5GC")
start_cmd=("docker compose -f sa-deploy.yaml up -d" "docker compose up -d" "docker compose up -d")
end_cmd=("docker compose -f sa-deploy.yaml down" "docker compose down" "docker compose down")
path=("/home/demo/docker_open5gs/" "/home/demo/oai-cn5g-fed/docker-compose/" "/home/demo/free5gc/free5gc-compose/")

for (( i=0; i<${#name[*]}; ++i)); 
do
    echo "Starting the ${name[$i]} core"
    ssh demo0 "cd ${path[$i]} && ${start_cmd[$i]}"
    # wait for the core to be ready
    sleep 20
    echo "Starting the Iperf server"
    ssh demo2 iperf3 -s --json --logfile ${name[$i]} &

    echo "Executing iperf3 test for 100s"
    ssh phone "./iperf3.sh 191.4.204.202 ${name[$i]} 100"

    echo "Shuting down the Iperf server"
    ssh demo2 "pgrep iperf3 | xargs kill -15"
    fg # let the ssh conn that started the iperf server die
    echo "Shuting down the core network"
    ssh demo0 "cd ${path[$i]} && ${end_cmd[$i]}"
    # TODO handle gnb restarts
    read -p "Press Enter to continue to the next core" </dev/tty
done
