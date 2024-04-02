from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('QtAgg') 
charts = [ 
         [
        "../logs/oai-flexric-values-only.log",
        "../logs/srsran-flexric.logs",
        ],
        ["../logs/bouncer-values-only.log",]
]
labels = [
        "Flexric",
        "ORAN SC RIC",
]
rans = [
        ["OAI RAN",
        "srsRAN",],
        ["srsRAN",],
]
limits = [
    (0, 4000),
    (0, 1_200),
]

ylabels = [
    "Tempo de Resposta (μs)",
    "Tempo de Resposta (ms)",
]

scaling_factor = [
    1,
    1_000,
]

fig, axes = plt.subplots(1, len(charts))


colors = [["#7EA16B", "#C3D898",], ["#C3D898"],]
for files, ax, label, ran, color, limit, ylabel, sf in zip(charts, axes, labels, rans, colors, limits, ylabels, scaling_factor):
    dataset = []
    for file in files:
        with open(file, "r") as file:
            data = map(lambda line: int(line[:-1])/sf, file.readlines())
        dataset.append(list(data))
    b = ax.boxplot(dataset, medianprops={"color": "#000000"}, widths=0.8)
    for box, c, r in zip(b['boxes'], color, ran):
        ax.add_patch(Polygon(box.get_xydata(), facecolor=c, label=r))
    ax.legend(loc='upper right', ncols=2, fontsize=12)
    ax.set_ylim(limit)
    ax.set_xlabel(label)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.set_xticks([])

plt.show()
