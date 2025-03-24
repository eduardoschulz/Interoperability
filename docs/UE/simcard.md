# COTS UE setup

Deciding which phone you'll use is probably the most import decision you'll make. The srsRAN project maintains a compatibility table on [their documentation](https://docs.srsran.com/projects/project/en/latest/knowledge_base/source/cots_ues/source/index.html). 

## SIM cards

The SIM cards user are made by osmocom so we used their tool to flash new identities to the cards.
```
git clone https://github.com/osmocom/pysim
cd pysim
sudo apt-get install --no-install-recommends \
    pcscd libpcsclite-dev \
    python3 \
    python3-setuptools \
    python3-pyscard \
    python3-pip
pip3 install -r requirements.txt
```

The values in the card used in our testing was flashed using the following command (note: the `-a` part is your ADM-KEY and it **will** differ from ours)
```
./pySim-prog.py -p0 -s 8988211000000689615 --mcc=001 --mnc=01 -a 77190612 --imsi=001010123456789  -k 41B7157E3337F0ADD8DA89210D89E17F --opc=1CD638FC96E02EBD35AA0D41EB6F812F
```

We also had a seconf simcard with the following configuration

```
imsi: 901700000028080
k: 724d0f31f2259622700437430b7b5c6e
opc: 1140620b2805d84b44643bfcfbe6218c
```
## Troubleshooting

- Some devices seem to block some PLMN IDs so testing different ones may be a good idea. Just be careful not to break any laws.
- Sometimes, the phone will randomly decide they can't find the network anymore. Restarting the device and removing the SIM card may help. Using the same SIM in a different phone may also solve the issue.
- In some rare instances, we observed through wireshark that our test phone decided to join a slice on its own. This can cause the phone to be rejected by the core. If this happens, make sure that you don't have anyother configurations that may interfere; if so, add that slice to your core.
- In all setups described in this website, **you will** need to manually create an access point configuration on your device. Failing that will not allow the UE to connect to the network.
- Some apps may allow you to set an android phone to 5G-only mode. This will prevent your phone from connecting to other networks if your lab is in a 4G-only zone.
