import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
NUM_ROWS = 60

def conv(x):
    return float(x[5:])

paths = ["../logs/srsran-ping-open5gs", "../logs/srsran-ping-oai", "../logs/oai-open5gs-ping", "../logs/oai-oai-ping"]
xlabels = ["Open5Gs (SRSRAN)", "OAI CN (SRSRAN)", "Open5Gs (OAI)", "OAI CN (OAI)"]
count = len(paths)
if len(xlabels) != count:
    print("different number of files and x-axis labels")
    exit()

ax = plt.subplot()

data = map(lambda path: np.loadtxt(path, skiprows=1, usecols=(6), max_rows=NUM_ROWS, converters=conv), paths)
ax.boxplot(list(data), labels=xlabels)
ax.set_ylabel("Latência (ms)")
ax.set_ylim((8, 32))

plt.show()
