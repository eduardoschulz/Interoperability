# Free5GC

## 1. Set Up
In our test we used the version v3.3.0.

### 1.1 Core-host Configurations

```shell
sudo sysctl net.ipv4.conf.all.forwarding=1
sudo iptables -P FORWARD ACCEPT
```

### 1.2 Clone free5gc-compose

```shell
git clone https://github.com/free5gc/free5gc-compose
git checkout v3.3.0
```

### 1.3 Changing Core Settings

```shell
git clone https://github.com/eduardoschulz/Interoperabilidade.git
cd Interoperabilidade/core-networks/free5gc/core-networks/FREE5GC
cp -r config path/to/free5gc-compose 
```

### 1.4 gNB-host Configurations
You also must configure a route to the internal docker network so that the gNB can make a connection.

```shell
sudo ip route add 10.100.200.0/24 via {ip_addr_corehost} dev {interface}

#example
sudo ip route add 10.100.200.0/24 via 191.4.205.38 dev br01
```

## 2.0 Installing GTP-U Kernel Module

```shell
git clone https://github.com/free5gc/gtp5g.git && cd gtp5g
make clean && make
sudo make install
``` 

## 3.0 Deploying the Core Network

+ To start the core
```shell
cd path-to/free5gc-compose
docker compose up -d
```
+ To stop the core
```shell
docker compose down 
```

### 3.1 Adding UE to Core Database
To set up your UEs you'll need to go to the free5gc webpage on your machine. You should see a login screen when accessing http://<core-ip>:3000. The credentials are **admin** and the password is **free5gc**.

## 4.0 More Information

[Free5GC - Github Page](https://github.com/free5gc/free5gc)
[Free5GC - Compose](https://github.com/free5gc/free5gc-compose)
[Free5GC - Forum](https://forum.free5gc.org/)
