# Open5GS

## 1. Set Up
In our test we used the version v2.7.0

### 1.1 Core-host Configurations

```shell
sudo sysctl net.ipv4.conf.all.forwarding=1
sudo iptables -P FORWARD ACCEPT
```

### 1.2 Clone docker\_open5gs

```shell
git clone https://github.com/herlesupreeth/docker_open5gs
git checkout v2.7.0
```

### 1.3 Changing Core Settings

```shell
git clone https://github.com/eduardoschulz/Interoperabilidade.git
cd Interoperabilidade/core-networks/OPEN5GS
cp sa-deploy.yaml /path/to/docker_open5gs/.
cp .env /path/to/docker_open5gs/. 

cp -r smf/ /path/to/docker_open5gs/ #here you need to modify your dnn 
cp -r upf/ /path/to/docker_open5gs/ #same thing as above
```

## 2.0 Deploying the Core Network

+ To start the core
```shell
cd path-to/docker_open5gs
docker compose -f sa-deploy.yaml up -d
```
+ To stop the core
```shell
docker compose down 
```

### 3.1 Adding UE to Core Database
To set up your UEs you'll need to go to the open5gs webpage on your machine. You should see a login screen when accessing http://<core-ip>:3000. The credentials are **admin** and the password is **1423**.

## 4.0 More Information
[Open5GS - Docker](https://github.com/herlesupreeth/docker_open5gs)
[Open5GS - Documentation](https://open5gs.org/open5gs/docs/)
[Open5GS - Github Page](https://github.com/open5gs/open5gs)
[srsRAN - Docker](https://github.com/srsran/srsRAN_Project/tree/main/docker);
[Gradiant - Open5gs in k8s](https://github.com/Gradiant/5g-charts/tree/main/charts/open5gs).
