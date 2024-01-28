import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
NUM_ROWS = 60
files = ["../logs/iperf-oai.json", "../logs/iperf-srsran.json"]
labels = [["OAI CN", "Open5Gs"], ["Open5Gs", "OAI CN"]]
ylim = [(0, 35), (90, 120)]
titles = ["OAI", "SRSRAN"]
count = len(files)
fig, ax = plt.subplots(1, count)

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def from_iter(x):
    print(x['title'].split('-')[1])
    return np.fromiter(map(conv, x['intervals']), float)

ax[0].set_ylabel("Taxa de transferencia (Mbps)")

for i in range(count):
    with open(files[i], "r") as file:
        data = json.load(file)
    rev = filter(lambda x: x['title'].endswith('-rev'),data)
    boxes = list(map(from_iter, rev))
    ax[i].boxplot(boxes, labels=labels[i])
    ax[i].set_ylim(ylim[i])
    ax[i].set_title(titles[i])

plt.show()
