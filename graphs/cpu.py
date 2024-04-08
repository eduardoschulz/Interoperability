import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

files = [
    [
        "../logs/oai/oai/iperf/cpu-ran.csv",
        "../logs/srsran/oai/iperf/cpu-ran.csv",
    ],
    [
        "../logs/oai/open5gs/iperf/cpu-ran.csv",
        "../logs/srsran/open5gs/iperf/cpu-ran.csv",
    ],
    [
        "../logs/oai/free5gc/iperf/cpu-ran.csv",
        "../logs/srsran/free5gc/iperf/cpu-ran.csv",
    ],
]
# how many samples to skip until the start of the experiment
skip = [
    [
        15,
        10,
    ],
    [
        19,
        14,
    ],
    [
        14,
        19,
    ],
]

rans = ["OAI RAN", "srsRAN"]

cores = [
    "OAI CN",
    "Open5GS",
    "Free5GC",
]

def conv(x):
    return float(x[:-1])

def readfile(file: str, skip: int):
    data = np.genfromtxt(file, delimiter=",", skip_header=skip, max_rows=40, usecols=[2], converters={2: conv})
    return data


def build(save=True):
    # there are 40 measurements total. They were taken every 15s
    # so in total the test lasted 600s
    x = np.arange(40) * 15 # the label locations

    colors = ["#7EA16B", "#C3D898"]
    fig, axes = plt.subplots(1, 3, layout='constrained')

    for tests, offsets, ax, core in zip(files, skip, axes, cores):
        ax.set_ylim(0, 12)
        for ran, color, test, offset in zip(rans, colors, tests, offsets):
            data = readfile(test, offset)
            rects = ax.plot(x, data, label=ran, color=color)
        ax.set_xlabel(core, fontsize=12)

# Add some text for labels, title and custom x-axis tick labels, etc.
    fig.supylabel('Consumo de CPU (%)', fontsize=14)
#axes[len(axes)//2].set_xlabel("Tempo (s)", fontsize=14)
    axes[-1].legend(loc='upper right', ncols=2, fontsize=12)
    fig.supxlabel("Tempo (s)", fontsize=14)

#fig.set_tight_layout()
    fig.set_size_inches(10.4, 4.2)
#plt.show()
    if save:
        fig.savefig("figs/cpu.pdf", dpi=100)

if __name__ == "__main__":
    build(False)
    mpl.use('QtAgg') 
    plt.show()
