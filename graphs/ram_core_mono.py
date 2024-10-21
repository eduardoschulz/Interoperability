import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
files = [
    "../logs/oai/oaicn/mono/mem.csv",
    "../logs/oai/open5gs/mono/mem.csv",
    "../logs/oai/free5gc/mono/mem.csv",
    "../logs/srsran/oaicn/mono/mem.csv",
    "../logs/srsran/open5gs/mono/mem.csv",
    "../logs/srsran/free5gc/mono/mem.csv",
]
# how many samples to skip until the start of the experiment
labels = [
        "OAI CN",
        "Open5Gs",
        "Free5Gc",
]

rans = ["OAI", "srsRAN"]

def conv(x):
    return int(x)/1024/1024/1024

def readfile(file: str):
    data = np.genfromtxt(file, delimiter=",", max_rows=11, usecols=[2], converters={2: conv})
    return np.average(data)


def build(save=True):
    x = np.arange(len(labels))  # the label locations
    width = 0.33  # the width of the bars
    multiplier = 0

    colors = ["#7EA16B", "#C3D898"]
    fig, ax = plt.subplots(layout='constrained')

    for i in range(len(rans)):
        offset = width * multiplier
        data = (readfile(files[i]), readfile(files[i+2]), readfile(files[i+4]))
        rects = ax.bar(x + offset, data, width, label=rans[i], color=colors[i])
        ax.bar_label(rects, padding=2)
        multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Core memory consumption (GB)', fontsize=14)
    ax.set_xticks(x + width/2, labels, fontsize=12)
    ax.set_ylim(0, 4)
    ax.legend(loc='upper right', ncols=2, fontsize=12)

    if save:
        fig.savefig("figs/ram-core-mono.pdf", dpi=100)

if __name__ == "__main__":
    build(False)
    mpl.use('QtAgg') 
    plt.show()
