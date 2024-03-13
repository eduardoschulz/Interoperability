# SIM cards

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
