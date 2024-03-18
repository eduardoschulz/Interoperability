import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/oai/oai/iperf/oai-oaicn",
         "../logs/oai/open5gs/iperf/oai-open5gs",
         "../logs/oai/free5gc/iperf/20240304-oai-free5gc",
         "../logs/",
         "../logs/",
         "../logs/",
]
labels = {
        "srsran-oai-rev": "SRSRAN (OAI CN)",
        "srsran-open5gs-rev": "SRSRAN (Open5Gs)",
        "oai-open5gs-rev": "OAI (Open5Gs)",
        "oai-oai-rev": "OAI (OAI CN)",
        }
count = len(files)
total_count = len(labels)
ax = plt.subplot()

def conv(x):
    stream = x['streams'][0]
    # rtt comes in micro seconds and we convert it to ms (https://github.com/esnet/iperf/blob/332c31ee6512514c216077407a725b5b958b1582/src/tcp_info.c#L168)
    return float(stream['rtt'])/1_000

def from_iter(x):
    return [conv(t) for t in x['intervals']]

ax.set_ylabel("Tempo de ida e volta (RTT) (ms)")
ax.set_xlabel("Duração do teste (s)")

for i in range(count):
    with open(files[i], "r") as file:
        data = json.load(file)
    for test in data:
        if not test['title'].endswith('-rev'):
            continue
        ax.plot(from_iter(test), label=labels[test['title']])
        ax.legend()

plt.show()
