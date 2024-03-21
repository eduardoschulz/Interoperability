from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/oai/oai/iperf/oai-oaicn",
         "../logs/srsran/oai/iperf/20240304-oai",
         "../logs/oai/open5gs/iperf/oai-open5gs",
         "../logs/srsran/open5gs/iperf/20240320",
         "../logs/oai/free5gc/iperf/20240304-oai-free5gc",
         "../logs/srsran/free5gc/iperf/20240321-free5gc"
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
ax = plt.subplot()

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def from_iter(x):
    return np.fromiter(map(conv, x['intervals']), float)

ax.set_ylabel("Taxa de transferência (Mbps)", fontsize=14)

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
ax.set_ylim((50,130))
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
