#!/bin/sh
MY_IP=$(ip addr show bri0 | grep -o 'inet [0-9\\.]*' | grep -o '[0-9\\.]*')
sudo gnb -c gnb_speed.yml amf --bind_addr $MY_IP --addr 10.100.200.250
