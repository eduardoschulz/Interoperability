import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

files = [
    [
        "../logs/oai/oaicn/mono/cpu.csv",
        "../logs/srsran/oaicn/mono/cpu.csv",
    ],
    [
        "../logs/oai/open5gs/mono/cpu.csv",
        "../logs/srsran/open5gs/mono/cpu.csv",
    ],
    [
        "../logs/oai/free5gc/mono/cpu.csv",
        "../logs/srsran/free5gc/mono/cpu.csv",
    ],
]

rans = ["OAI RAN", "srsRAN"]

cores = [
    "OAI CN",
    "Open5GS",
    "Free5GC",
]

def conv(x):
    return float(x)*100

def readfile(file: str):
    data = np.genfromtxt(file, delimiter=",", max_rows=11, usecols=[2], converters={2: conv})
    return data


def build(save=True):
    # there are 40 measurements total. They were taken every 15s
    # so in total the test lasted 600s
    x = np.arange(11) * 30 # the label locations

    colors = ["#7EA16B", "#C3D898"]
    fig, axes = plt.subplots(1, 3, layout='constrained')

    for tests, ax, core in zip(files, axes, cores):
        ax.set_ylim(0, 8)
        for ran, color, test in zip(rans, colors, tests):
            data = readfile(test)
            rects = ax.plot(x, data, label=ran, color=color)
        ax.set_xlabel(core, fontsize=12)

# Add some text for labels, title and custom x-axis tick labels, etc.
    fig.supylabel('CPU Utilization (%)', fontsize=14)
#axes[len(axes)//2].set_xlabel("Tempo (s)", fontsize=14)
    axes[-1].legend(loc='upper right', ncols=2, fontsize=12)
    fig.supxlabel("Time (s)", fontsize=14)

#fig.set_tight_layout()
    fig.set_size_inches(10.4, 4.2)
#plt.show()
    if save:
        fig.savefig("figs/cpu.pdf", dpi=100)

if __name__ == "__main__":
    build(False)
    mpl.use('QtAgg') 
    plt.show()
