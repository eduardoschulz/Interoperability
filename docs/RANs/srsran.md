# SRSRAN

## 1. Building

Version: 23.10.1
UHD version: 4.6.0.0
OS version: Ubuntu Server 22.04 LTS

For building we recommend following the official documentation available [here](https://docs.srsran.com/projects/project/en/latest/user_manuals/source/installation.html) to build srsRAN from source. The UHD driver was used and built from sources following [this guide](https://files.ettus.com/manual/page_build_guide.html).

## 2. Running
After building and installing srsRAN we recommend running the [srsran_performance](https://raw.githubusercontent.com/srsran/srsRAN_Project/release_23_10_1/scripts/srsran_performance) script available in the official srsran_project repository. Since these changes do not persist remember to re-run them if the machine is restarted.

Watchout as srsRAN requires the bind address to be specified whenever trying to connect to an external machine.

Finnaly, free5gc and OAI CN require a change in routing table of the gNB host. This change can be applied with the commands:

- Free5Gc: `sudo ip route add 10.100.200.0/24 via {external addr of the core host} dev {name of the network interface used to reach the core host}`.

- OAI CN: `sudo ip route add 10.100.200.0/26 via {external addr of the core host} dev {name of the network interface used to reach the core host}`.
