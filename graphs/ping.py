import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
NUM_ROWS = 600

def conv(x: str):
    x = x.split(" ")[7]
    return float(x[5:])

def read_file(path: str):
    with open(path, 'r') as f:
        t = filter(lambda l: l.startswith("64 bytes"), f.readlines())
    print(len(list(t)))
    return list(map(lambda x: conv(x), t))
        

paths = ["../logs/srsran/oai/ping/oai.txt", 
         "../logs/srsran/open5gs/ping/ping_2024-03-04_20-14-54.txt", 
         "../logs/srsran/free5gc/ping/free5gc.txt",
         "../logs/oai/free5gc/ping/oai-free5gc.txt",
         "../logs/oai/open5gs/ping/oai-open5gs.txt",
         "../logs/oai/oai/ping/oai-oai.txt"]
xlabels = ["Open5Gs (SRSRAN)", "OAI CN (SRSRAN)", "Free5Gc (SRSRAN)", "Free5Gc (OAI)", "Open5Gs (OAI)", "OAI CN (OAI)"]
count = len(paths)
if len(xlabels) != count:
    print("different number of files and x-axis labels")
    exit()

ax = plt.subplot()

data = list(map(lambda path: read_file(path), paths))
ax.boxplot(data, labels=xlabels)
ax.set_xticklabels(labels=xlabels, fontsize=12)
ax.set_ylabel("Latência (ms)", fontsize=12)
#ax.set_ylim((8, 32))

plt.show()
