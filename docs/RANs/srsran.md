# srsRAN

## 1. Building

Version: 23.10.1
UHD version: 4.6.0.0
OS version: Ubuntu Server 22.04 LTS

For building we recommend following the official documentation available [here](https://docs.srsran.com/projects/project/en/latest/user_manuals/source/installation.html) to build srsRAN from source. Do note that modifications such as compiling the ZMQ adaptor can be changed inside de project's `CMakeLists.txt` or when setting up the cmake build folder. The UHD driver used was built from sources following [this guide](https://files.ettus.com/manual/page_build_guide.html).

## 2. Running
After building and installing srsRAN we recommend running the [srsran_performance](https://raw.githubusercontent.com/srsran/srsRAN_Project/release_23_10_1/scripts/srsran_performance) script available in the official srsran_project repository. Since these changes do not persist remember to re-run them if the machine is restarted.

Watchout as srsRAN requires the bind address to be specified whenever trying to connect to an external machine.

Finnaly, free5gc and OAI CN require a change in routing table of the gNB host. This change can be applied with the commands:

- Free5Gc: `sudo ip route add 10.100.200.0/24 via {external addr of the core host} dev {name of the network interface used to reach the core host}`.

- OAI CN: `sudo ip route add 10.100.200.0/26 via {external addr of the core host} dev {name of the network interface used to reach the core host}`.

## Tips and tricks

- This page is about the srsRAN_5G hosted at [srsran/srsran_project](https://github.com/srsran/srsran_project) NOT the older and to be deprecated srsRAN_4G hosted at [srsran/srsRAN_4G](https://github.com/srsran/srsRAN_4G). However, the latter is used to simulate UEs as it hosts the srsUE project, at least at the time of writing.
- You CAN run the srsRAN gNB with multiple simulated UEs using the srsUE project and the ZMQ library. You will have to use GNURadio as well to multiplex the communication sockets (this means that the transport between the UE and gNB is also simulated) though. You can learn more about it [here](https://docs.srsran.com/projects/project/en/latest/tutorials/source/srsUE/source/index.html#multi-ue-emulation)
- To create a quick setup you can use [this](https://github.com/herlesupreeth/docker_open5gs/tree/master). Just read the entire readme before trying to use it.
