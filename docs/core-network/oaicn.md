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
sudo ip route add 192.168.70.128/26 via {ip_addr_corehost} dev {interface}

#example
sudo ip route add 192.168.70.128/26 via 191.4.205.38 dev br01
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

### 2.1 Adding UE to Core Database
```shell

docker exec -it mysql bash
mysql -u root -p

password: linux 
```

```SQL
use oai_db;
INSERT INTO `AuthenticationSubscription` (`ueid`, `authenticationMethod`, `encPermanentKey`, `protectionParameterId`, `sequenceNumber`, `authenticationManagementField`, `algorithmId`, `encOpcKey`, `encTopcKey`, `vectorGenerationInHss`, `n5gcAuthMethod`, `rgAuthenticationInd`, `supi`) VALUES
('001010123456789', '5G_AKA', '41B7157E3337F0ADD8DA89210D89E17F', '41B7157E3337F0ADD8DA89210D89E17F', '{\"sqn\": \"000000000020\", \"sqnScheme\": \"NON_TIME_BASED\", \"lastIndexes\": {\"ausf\": 0}}', '8000', 'milenage', '1CD638FC96E02EBD35AA0D41EB6F812F', NULL, NULL, NULL, NULL, '001010123456789');

INSERT INTO `SessionManagementSubscriptionData` (`ueid`, `servingPlmnid`, `singleNssai`, `dnnConfigurations`) VALUES
('001010123456789', '00101', '{\"sst\": 222, \"sd\": \"123\"}','{\"default\":{\"pduSessionTypes\":{ \"defaultSessionType\": \"IPV4\"},\"sscModes\": {\"defaultSscMode\": \"SSC_MODE_1\"},\"5gQosProfile\": {\"5qi\": 6,\"arp\":{\"priorityLevel\": 1,\"preemptCap\": \"NOT_PREEMPT\",\"preemptVuln\":\"NOT_PREEMPTABLE\"},\"priorityLevel\":1},\"sessionAmbr\":{\"uplink\":\"1000Mbps\", \"downlink\":\"1000Mbps\"},\"staticIpAddress\":[{\"ipv4Addr\": \"12.1.1.4\"}]}}');
```
**The configuration above is only going to last until the core is restarted**. If you want to make this static you must make changes on the db files inside path/oaicn/docker-compose/databases/.

## 3.0 More Information

[Basic Deployment using Docker Compose](https://gitlab.eurecom.fr/oai/cn5g/oai-cn5g-fed/-/blob/master/docs/DEPLOY_SA5G_BASIC_DEPLOYMENT.md)
