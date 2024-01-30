import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/iperf-srsran.json", "../logs/iperf-oai.json"]
labels = ["OAI CN", "Open5Gs", "Open5Gs", "OAI CN"]
count = len(files)
total_count = len(labels)
ax = plt.subplot()

def conv(x):
    stream = x['streams'][0]
    return (float(stream['end']), float(stream['rtt'])/1_000)

def from_iter(x):
    return [conv(t) for t in x['intervals']]

ax.set_ylabel("Taxa de transferencia (Mbps)")

for i in range(count):
    with open(files[i], "r") as file:
        data = json.load(file)
    for test in data:
        if not test['title'].endswith('-rev'):
            continue
        print(test['title'].split('-')[1])
        ax.plot(from_iter(test), label=test['title'])

plt.show()
