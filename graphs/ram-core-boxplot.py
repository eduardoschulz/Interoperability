import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from itertools import cycle

mpl.use('QtAgg') 
files = [
    "../logs/oai/oai/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 15 53 24.csv", # core
    #"../logs/oai/oai/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 15 52 37.csv", # RAN
    "../logs/srsran/oai/iperf/core/Memory Basic-data-as-joinbyfield-2024-03-04 17 44 59.csv", # core
    #"../logs/srsran/oai/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 17 43 53.csv", # RAN
    "../logs/oai/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 16 21 22.csv", # core
    #"../logs/oai/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 16 21 00.csv", # RAN
    "../logs/srsran/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-20 17 22 53.csv", # core
    #"../logs/srsran/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-20 17 23 19.csv", # RAN
    "../logs/oai/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 44 19.csv", # core
    #"../logs/oai/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 45 26.csv", # RAN
    "../logs/srsran/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 13 53.csv", # core
    #"../logs/srsran/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 13 29.csv", # RAN
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

data = []
for file, skip in zip(files, skips):
    data.append(readfile(file, skip))

b = ax.boxplot(data, labels=rans, medianprops={"color": "#000000"})
for box, ran, color in zip(b['boxes'], rans, cycle(colors)):
    box.set_gapcolor(color)
    box.set_label(ran)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Comsumo de memória no núcleo (GB)', fontsize=14)
x = np.arange(len(labels)) * 2 + 1.5
ax.set_xticks(x, labels, fontsize=12)
ax.set_ylim(0, 2)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
