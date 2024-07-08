#!/bin/sh
# This can be used if your core is deployed in a kubernetes cluster. If your cluster is 
# in a different machine then you'll need to add a route from your gnb host to the cluster.
# Something like this should work "sudo ip route add 10.0.0.0/8 via 191.4.204.200 dev <your interface>"
#OPEN5GS=$(dig @10.96.0.10 open5gs-amf-ngap.open5gs.svc.cluster.local +short)
DEFAULT_INFACE=$(ip route | grep default | sed -e "s/.* dev \(\w*\) .*/\1/g")
MY_IP=$(ip addr show $DEFAULT_INFACE | grep -o 'inet [0-9\\.]*' | grep -o '[0-9\\.]*')
MY_IP=$(ip addr show bri0 | grep -o 'inet [0-9\\.]*' | grep -o '[0-9\\.]*')
echo "eu desabilitei a conexão com o flexric para debuggar o core"
sudo $HOME/srsran/latest/build/apps/gnb/gnb \
    -c $HOME/srsran/latest/configs/gnb_zmq.yml \
    -c $HOME/srsran/latest/configs/slicing.yml \
    -c $HOME/srsran/latest/configs/flexric.yml \
    amf --bind_addr $MY_IP --addr 127.0.0.1

