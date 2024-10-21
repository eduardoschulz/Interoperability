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

rans = ["OAI RAN", "srsRAN"]

def conv(x):
    return (x['end']['sum_sent']['retransmits'] * 1358) / x['end']['sum_sent']['bytes']

def readfile(file):
    with open(file, "r") as file:
        data = json.load(file)
    return conv(data)

def build(save=True):
    x = np.arange(len(labels))  # the label locations
    width = 0.33  # the width of the bars
    multiplier = 0

    colors = ["#7EA16B", "#C3D898"]
    fig, ax = plt.subplots(layout='constrained')

    for i in range(len(rans)):
        offset = width * multiplier
        index = i
        data = (readfile(files[index]), readfile(files[index+2]), readfile(files[index+4]))
        rects = ax.bar(x + offset, data, width, label=rans[i], color=colors[i])
        multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Packet retransmission rate (%)', fontsize=14)
    ax.set_xticks(x + width/2, labels, fontsize=12)
    ax.set_ylim(0, 0.0025)
    ax.legend(loc='upper right', ncols=2, fontsize=12)
    fig.set_size_inches(8, 4.2)
#plt.show()
    if save:
        fig.savefig("figs/retrans-split.pdf", dpi=100)

if __name__ == "__main__":
    build(False)
    mpl.use('QtAgg') 
    plt.show()
