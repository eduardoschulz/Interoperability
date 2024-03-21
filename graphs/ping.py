import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import matplotlib as mpl

mpl.use('QtAgg') 
NUM_ROWS = 600

def conv(x: str):
    x = x.split(" ")[7]
    return float(x[5:])

def read_file(path: str):
    with open(path, 'r') as f:
        t = filter(lambda l: l.startswith("[1"), f.readlines())
    return list(map(lambda x: conv(x), t))
        

paths = [
         "../logs/oai/oai/ping/oai-oai.txt",
         "../logs/srsran/oai/ping/oai.txt", 
         "../logs/oai/open5gs/ping/oai-open5gs.txt",
         "../logs/srsran/open5gs/ping/ping_2024-03-04_20-14-54.txt", 
         "../logs/oai/free5gc/ping/oai-free5gc.txt",
         "../logs/srsran/free5gc/ping/free5gc.txt",
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
count = len(paths)

ax = plt.subplot()


dataset = list(map(lambda path: read_file(path), paths))
ax.set_ylabel("Latência (ms)", fontsize=14)
ax.set_ylim((0, 64))
colors = ["#7EA16B", "#C3D898"]
b = ax.boxplot(dataset, labels=rans, medianprops={"color": "#000000"})
for i in range(len(b['boxes'])):
    box = b['boxes'][i]
    ax.add_patch(Polygon(box.get_xydata(), facecolor=colors[i%2], label=rans[i]))

x = np.arange(len(labels)) * 2 + 1.5
ax.set_xticks(x, labels, fontsize=12)

ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
