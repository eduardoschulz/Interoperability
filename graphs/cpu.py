import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
files = [
    "../logs/oai/free5gc/iperf/cpu-ran.csv",
    "../logs/srsran/free5gc/iperf/cpu-ran.csv",
]
# how many samples to skip until the start of the experiment
skip = [
    14,
    19,
]

rans = ["OAI", "srsRAN"]

def conv(x):
    return float(x[:-1])

def readfile(file: str, skip: int):
    data = np.genfromtxt(file, delimiter=",", skip_header=skip, max_rows=40, usecols=[2], converters={2: conv})
    return data


x = np.arange(40) * 15 # the label locations

colors = ["#7EA16B", "#C3D898"]
fig, ax = plt.subplots(layout='constrained')

for i in range(len(rans)):
    data = readfile(files[i], skip[i])
    rects = ax.plot(x, data, label=rans[i], color=colors[i])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Consumo de CPU (%)', fontsize=14)
ax.set_xlabel("Tempo (s)", fontsize=14)
ax.set_ylim(0, 12)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
