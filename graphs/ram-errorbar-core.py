import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from itertools import cycle
from matplotlib.patches import Polygon


mpl.use('QtAgg') 
files = [
    "../logs/oai/oai/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 15 53 24.csv", # core
    "../logs/srsran/oai/iperf/core/Memory Basic-data-as-joinbyfield-2024-03-04 17 44 59.csv", # core
    "../logs/oai/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 16 21 22.csv", # core
    "../logs/srsran/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-20 17 22 53.csv", # core
    "../logs/oai/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 44 19.csv", # core
    "../logs/srsran/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 13 53.csv", # core
]
# how many samples to skip until the start of the experiment
skips = [
    14,    
    9,
    16,
    16,
    18,
    16,
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

def conv(x):
    return float(x[:-4])

def readfile(file: str, skip: int):
    data = np.genfromtxt(file, delimiter=",", skip_header=skip, max_rows=40, usecols=[2], converters={2: conv})
    return data


colors = ["#7EA16B", "#C3D898"]
fig, ax = plt.subplots(layout='constrained')

xaxis = np.arange(len(files))
for file, skip, x, color, ran in zip(files, skips, xaxis, cycle(colors), rans):
    data = readfile(file, skip)
    median = np.median(data)
    stddev = np.std(data)
    ax.errorbar(x, median, yerr=stddev, label=ran, color=color, capsize=3.0, linewidth=4.2, capthick=4.2)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Comsumo de memória no núcleo (GB)', fontsize=14)
x = np.arange(len(labels))*2 + 0.5
ax.set_xticks(x, labels, fontsize=12)
ax.set_ylim(1.1, 1.4)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
