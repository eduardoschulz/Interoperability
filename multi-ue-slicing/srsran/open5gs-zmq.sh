#!/bin/sh
MY_IP=$(ip addr show bri0 | grep -o 'inet [0-9\\.]*' | grep -o '[0-9\\.]*')
echo "eu desabilitei a conexão com o flexric para debuggar o core"
sudo ~/srsran/latest/build/apps/gnb/gnb \
    -c $HOME/srsran/latest/configs/gnb_zmq.yml \
    -c $HOME/srsran/latest/configs/slicing.yml \
    -c $HOME/srsran/latest/configs/flexric.yml \
    amf --bind_addr $MY_IP --addr 191.4.204.200

