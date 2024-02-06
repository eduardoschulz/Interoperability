# OAI Core Network

## 1. Set Up
For our test the version 1.5.0 was used.
### 1.1 Core-host Configurations
```shell
sudo sysctl net.ipv4.conf.all.forwarding=1
sudo iptables -P FORWARD ACCEPT
```

### 1.2 Clone oai-cn5g-fed
```shell
git clone https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed.git
git checkout v1.5.0
```

### 1.3 Changing Core Settings

```shell
git clone https://github.com/eduardoschulz/Interoperabilidade.git
cd Interoperabilidade/core-networks/OAI-CN/

rm -r ~/oai-cn5g-fed/docker-compose/database
cp -r database ~/oai-cn5g-fed/docker-compose/database

mv docker-compose-basic-nrf.yaml ~/oai-cn5g-fed/docker-compose/
```

### 1.4 gNB-host Configurations
You also must configure a route to the internal docker network so that the gNB can make a connection.

```shell
sudo ip route add route 192.168.70.128/26 via {ip_addr_corehost} dev {interface}

#example
sudo ip route add route 192.168.70.128/26 via 191.4.205.38 dev br01
```

## 2.0 Deploying the Core Network

+ To start the core
```shell
cd path-to/oai-cn5g-fed/docker-compose
python3 core-networks.py --type start-basic --scenario 1
```
+ To stop the core
```shell
python3 core-networks.py --type stop-basic --scenario 1
```

## 3.0 More Information

[Basic Deployment using Docker Compose](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/blob/master/docs/DEPLOY_SA5G_BASIC_DEPLOYMENT.md)
