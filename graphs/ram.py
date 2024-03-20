import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/oai/oai/iperf/oai-oaicn",
         "../logs/oai/open5gs/iperf/oai-open5gs",
         "../logs/oai/free5gc/iperf/20240304-oai-free5gc",
         "../logs/srsran/oai/iperf/20240304-oai",
         "../logs/srsran/open5gs/iperf/20240304",
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
ax = plt.subplot()

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def from_iter(x):
    return np.fromiter(map(conv, x['intervals']), float)

ax.set_ylabel("Taxa de transferencia (Mbps)", fontsize=14)
ax.set_xlabel("Pares de RAN e núcleo usados no teste", fontsize=14)

dataset = []
for i in range(count):
    with open(files[i], "r") as file:
        data = json.load(file)
    dataset.append(list(from_iter(data)))

ax.boxplot(dataset)
ax.set_xticklabels(labels, fontsize=12)
ax.set_ylim((0,150))

plt.show()
