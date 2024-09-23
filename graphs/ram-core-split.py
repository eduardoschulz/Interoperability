import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
files = [
    "../logs/oai/oaicn/split/mem.csv",
    "../logs/oai/open5gs/split/mem.csv",
    "../logs/oai/free5gc/split/mem.csv",
    "../logs/srsran/oaicn/split/mem.csv",
    "../logs/srsran/open5gs/split/mem.csv",
    "../logs/srsran/free5gc/split/mem.csv",
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
ax.set_ylabel('Comsumo de memória no núcleo (GB)', fontsize=14)
ax.set_xticks(x + width/2, labels, fontsize=12)
ax.set_ylim(0, 4)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
