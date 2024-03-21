import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/oai/oai/iperf/oai-oaicn",
         "../logs/srsran/oai/iperf/20240304-oai",
         "../logs/oai/open5gs/iperf/oai-open5gs",
         "../logs/srsran/open5gs/iperf/20240320",
         "../logs/oai/free5gc/iperf/20240304-oai-free5gc",
         "../logs/srsran/free5gc/iperf/20240304-free5gc"
]
labels = [
        "OAI CN",
        "Open5Gs",
        "Free5Gc",
]
rans = [
        "OAI",
        "srsRAN",
        "_OAI",
        "_srsRAN",
        "_OAI",
        "_srsRAN",
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

ax.set_ylabel("Tempo de ida e volta (ms)", fontsize=14)

dataset = []
for i in range(count):
    with open(files[i], "r") as file:
        data = json.load(file)
    dataset.append(list(from_iter(data)))

colors = ["#7EA16B", "#C3D898"]
b = ax.boxplot(dataset, labels=rans, medianprops={"color": "#000000"})
for i in range(len(b['boxes'])):
    box = b['boxes'][i]
    ax.add_patch(Polygon(box.get_xydata(), facecolor=colors[i%2], label=rans[i]))

x = np.arange(len(labels)) * 2 + 1.5
ax.set_xticks(x, labels, fontsize=12)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
