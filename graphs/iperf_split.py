from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

files = ["../logs/oai/oaicn/split/iperf.json",
         "../logs/srsran/oaicn/split/iperf.json",
         "../logs/oai/open5gs/split/iperf.json",
         "../logs/srsran/open5gs/split/iperf.json",
         "../logs/oai/free5gc/split/iperf.json",
         "../logs/srsran/free5gc/split/iperf.json",
]
labels = [
        "OAI CN",
        "Open5GS",
        "Free5GC",
]
rans = [
        "OAI RAN",
        "srsRAN",
        "_OAI",
        "_srsRAN",
        "_OAI",
        "_srsRAN",
]
count = len(files)
fig, ax = plt.subplots(1,1)

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def from_iter(x):
    return np.fromiter(map(conv, x['intervals']), float)

def build(save=True):
    ax.set_ylabel("Throughput Rate (Mbps)", fontsize=16)

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
    ax.set_xticks(x, labels, fontsize=16)
    ax.set_ylim((0,150))
    ax.legend(loc='upper right', ncols=2, fontsize=14)

    fig.set_size_inches(10.4, 4.2)
    plt.tight_layout()
#plt.show()
    if save:
        fig.savefig("figs/iperf-split.pdf", dpi=100)

if __name__ == "__main__":
    build(save=False)
    mpl.use('QtAgg') 
    plt.show()
