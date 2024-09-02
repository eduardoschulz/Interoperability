#!/bin/bash

name=("Open5GS", "OAI", "Free5GC")
start_cmd=("docker compose -f sa-deploy.yaml up -d" "python3 core-network.py --start-basic --scenario-1" "docker compose up -d")
end_cmd=("docker compose -f sa-deploy.yaml down" "python3 core-network.py --stop-basic --scenario-1" "docker compose down")
path=("/home/demo/docker_open5gs/" "/home/demo/oai-cn5g-fed/docker-compose/" "/home/demo/free5gc/free5gc-compose/")
nrf_ips=("172.22.0.12" "192.168.70.130" "10.100.200.3")
nrf_ports=("7777" "8080" "8000")
nrf_path=("/nnrf-nfm/v1/nf-instances" "/nnrf-nfm/v1/nf-instances?nr-type=AMF" "/nnrf-disc/v1/nf-instances?targerequester-nf-type=SSS&t-nf-type=AMF")

for (( i=0; i<${#name[*]}; ++i)); 
do
    echo "Starting the ${name[$i]} core"
    ssh demo0 "cd ${path[$i]} && ${start_cmd[$i]}"
    # wait for the core to be ready
    while [$(curl -s --http2-prior-knowledge -X GET "http://${nrf_ips[$i]}:${nrf_ports[$i]}${nrf_path[$i]}" | jq ._links.items[].href) -lt 1]
    do
        sleep 2
    done

    echo "Starting the Iperf server"
    ssh demo2 iperf3 -s --json --logfile ${name[$i]} &
    read -p "Press Enter when the phone connects to the network" </dev/tty

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
