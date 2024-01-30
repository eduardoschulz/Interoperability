import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = ["../logs/iperf-srsran.json", "../logs/iperf-oai.json"]
labels = ["OAI CN (SRSRAN)", "Open5Gs (SRSRAN)", "Open5Gs (OAI)", "OAI CN (OAI)"]
count = len(files)
ax = plt.subplot()
values = []
total_count = 0

def conv(x):
    return x['end']['sum_sent']['retransmits']

ax.set_ylabel("Pacotes retransmitidos")

for i in range(count):
    with open(files[i], "r") as file:
        data = json.load(file)
    temp = [conv(test) for test in data if test['title'].endswith('-rev')]
    total_count += len(temp)
    values += temp

ax.bar(1 + np.arange(total_count), values, tick_label=labels)
plt.show()
