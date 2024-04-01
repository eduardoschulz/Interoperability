import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
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

rans = ["OAI", "srsRAN"]

def conv(x):
    return float(x[:-1])

def readfile(file: str, skip: int):
    data = np.genfromtxt(file, delimiter=",", skip_header=skip, max_rows=40, usecols=[2], converters={2: conv})
    return data


# there are 40 measurements total. They were taken every 15s
# so in total the test lasted 600s
x = np.arange(40) * 15 # the label locations

colors = ["#7EA16B", "#C3D898"]
fig, axes = plt.subplots(1, 3, layout='constrained')

for tests, offsets, ax in zip(files, skip, axes):
    ax.set_ylim(0, 12)
    for ran, color, test, offset in zip(rans, colors, tests, offsets):
        data = readfile(test, offset)
        rects = ax.plot(x, data, label=ran, color=color)

# Add some text for labels, title and custom x-axis tick labels, etc.
axes[0].set_ylabel('Consumo de CPU (%)', fontsize=14)
axes[len(axes)//2].set_xlabel("Tempo (s)", fontsize=14)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
