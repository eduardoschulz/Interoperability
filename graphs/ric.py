from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.use('QtAgg') 
files = [
        "../logs/fake-oai-flexric.logs",
        "../logs/srsran-flexric.logs",
        "../logs/bouncer-values-only.log",
]
labels = [
        "Flexric",
        "Flexric",
        "ORAN SC RIC",
]
rans = [
        "OAI",
        "srsRAN",
        "_srsRAN",
]
count = len(files)
ax = plt.subplot()

ax.set_ylabel("Tempo de Resposta (us)", fontsize=14)

dataset = []
for i in range(count):
    with open(files[i], "r") as file:
        data = map(lambda line: int(line[:-1]), file.readlines())
    dataset.append(list(data))

colors = ["#7EA16B", "#C3D898", "#C3D898"]
b = ax.boxplot(dataset, labels=rans, medianprops={"color": "#000000"})
for box, color, ran in zip(b['boxes'], colors, rans):
    ax.add_patch(Polygon(box.get_xydata(), facecolor=color, label=ran))

x = np.arange(len(labels)) + 1
ax.set_xticks(x, labels, fontsize=12)
ax.legend(loc='upper right', ncols=2, fontsize=12)

plt.show()
