import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
files = [
    #"../logs/oai/oai/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 15 53 24.csv", # core
    "../logs/oai/oai/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 15 52 37.csv", # RAN
    #"../logs/srsran/oai/iperf/core/Memory Basic-data-as-joinbyfield-2024-03-04 17 44 59.csv", # core
    "../logs/srsran/oai/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 17 43 53.csv", # RAN
    #"../logs/oai/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 16 21 22.csv", # core
    "../logs/oai/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-05 16 21 00.csv", # RAN
    #"../logs/srsran/open5gs/iperf/Memory Basic-data-as-joinbyfield-2024-03-20 17 22 53.csv", # core
    "../logs/srsran/open5gs/iperf/old/Memory Basic-data-as-joinbyfield-2024-03-04 16 58 29.csv", # RAN
    #"../logs/oai/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 44 19.csv", # core
    "../logs/oai/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 45 26.csv", # RAN
    #"../logs/srsran/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 13 53.csv", # core
    "../logs/srsran/free5gc/iperf/Memory Basic-data-as-joinbyfield-2024-03-04 18 13 29.csv", # RAN
]
# how many samples to skip until the start of the experiment
skip = [
    14,    
    10,
    17,
    13,
    13,
    18,
]
labels = [
        "OAI CN",
        "Open5Gs",
        "Free5Gc",
]

rans = ["OAI", "srsRAN"]

def conv(x):
    return float(x[:-4])

def readfile(file: str, skip: int):
    data = np.genfromtxt(file, delimiter=",", skip_header=skip, max_rows=40, usecols=[2], converters={2: conv})
    return np.average(data)


x = np.arange(len(labels))  # the label locations
width = 0.33  # the width of the bars
multiplier = 0

colors = ["#7EA16B", "#C3D898"]
fig, ax = plt.subplots(layout='constrained')

for i in range(len(rans)):
    offset = width * multiplier
    data = (readfile(files[i], skip[i]), readfile(files[i+2], skip[i+2]), readfile(files[i+4], skip[i+4]))
    rects = ax.bar(x + offset, data, width, label=rans[i], color=colors[i])
    ax.bar_label(rects, padding=2)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Consumo de mémoria na RAN (GB)', fontsize=14)
ax.set_xticks(x + width/2, labels, fontsize=12)
ax.set_ylim(0, 10)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
