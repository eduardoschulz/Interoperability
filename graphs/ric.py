from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import matplotlib as mpl

charts = [ 
         [
        "../logs/oai-flexric-values-only.log",
        "../logs/srsran-flexric.logs",
        ],
        ["../logs/bouncer-values-only.log",]
]
labels = [
        "Flexric",
        "O-RAN SC RIC",
]
rans = [
        ["OAI RAN",
        "srsRAN",],
        ["srsRAN",],
]
limits = [
    (0, 4000),
    (1, 10000),
]

ylabels = [
    "Tempo de Resposta (μs)",
    "Tempo de Resposta (ms)",
]

scaling_factor = [
    1,
    1_000,
]

scales = [
    'linear',
    'log'
]

def build(save=True):
    fig, axes = plt.subplots(1, len(charts))


    colors = [["#7EA16B", "#C3D898",], ["#C3D898"],]
    for files, ax, label, ran, color, limit, ylabel, sf, scale in zip(charts, axes, labels, rans, colors, limits, ylabels, scaling_factor, scales):
        dataset = []
        for file in files:
            with open(file, "r") as file:
                data = map(lambda line: int(line[:-1])/sf, file.readlines())
            dataset.append(list(data))
        b = ax.boxplot(dataset, medianprops={"color": "#000000"}, widths=0.25*len(files))
        for box, c, r in zip(b['boxes'], color, ran):
            ax.add_patch(Polygon(box.get_xydata(), facecolor=c, label=r))
        ax.legend(loc='upper right', ncols=2, fontsize=12)
        ax.set_ylim(limit)
        ax.set_xlabel(label, fontsize=14)
        ax.set_ylabel(ylabel, fontsize=14)
        ax.set_xticks([])
        ax.set_yscale(scale)

    fig.tight_layout(pad=0.1)

    fig.set_size_inches(8, 4)
#plt.show()
    if save:
        fig.savefig("figs/ric.pdf", dpi=100)

if __name__ == "__main__":
    build(False)
    mpl.use('QtAgg') 
    plt.show()
