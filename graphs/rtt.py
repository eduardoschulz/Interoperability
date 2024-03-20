import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/oai/oai/iperf/oai-oaicn",
         "../logs/oai/open5gs/iperf/oai-open5gs",
         "../logs/oai/free5gc/iperf/20240304-oai-free5gc",
         "../logs/srsran/oai/iperf/20240304-oai",
         "../logs/srsran/open5gs/iperf/20240320",
         "../logs/srsran/free5gc/iperf/20240304-free5gc"
]
labels = [
        "OAI (OAI CN)",
        "OAI (Open5Gs)",
        "OAI (Free5Gc)",
        "SRSRAN (OAI CN)",
        "SRSRAN (Open5Gs)",
        "SRSRAN (Free5Gc)",
]
count = len(files)
total_count = len(labels)
ax = plt.subplot()

def conv(x):
    stream = x['streams'][0]
    # rtt comes in micro seconds and we convert it to ms (https://github.com/esnet/iperf/blob/332c31ee6512514c216077407a725b5b958b1582/src/tcp_info.c#L168)
    return float(stream['rtt'])/1_000

def from_iter(x):
    return [conv(t) for t in x['intervals']]

ax.set_ylabel("Tempo de ida e volta (RTT) (ms)", fontsize=14)
ax.set_xlabel("Pares de RAN e núcleo usados no teste", fontsize=14)

datasets = []
for i in range(count):
    with open(files[i], "r") as file:
        data = json.load(file)
    datasets.append(list(from_iter(data)))

ax.boxplot(datasets)
ax.set_xticklabels(labels=labels, fontsize=12)

plt.show()
