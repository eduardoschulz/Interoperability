# SRSRAN
## Building

## Running
After building and installing SRSRAN we recommend running the srsran_performance script available in the official srsran_project repository. Since these changes do not persist remember to re-run them if the machine is restarted.

For each of the core networks there is an accompanying helper script, however, you still need to manually change the second line of each script so that they have the name of your network interface.

Finnaly, free5gc and OAI CN require a change in routing table of the gNB host. This change can be applied with the commands:
- Free5Gc: `sudo ip route add 10.100.200.0/24 via {external addr of the core host} dev {name of the network interface used to reach the core host}`.
- OAI CN: `sudo ip route add 10.100.200.0/26 via {external addr of the core host} dev {name of the network interface used to reach the core host}`.