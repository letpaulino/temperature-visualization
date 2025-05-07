import matplotlib.pyplot as plt
from enum import Enum

class Colormap(Enum):
    Defaut = None
    Blue = plt.cm.Blues
    Orange = plt.cm.Oranges
    Red = plt.cm.Reds

def line_graph(
    x_data: list,
    y_data1: list,
    title: str,
    x_label: str,
    y_label: str,
    y_data2=None,
    with_dates=False,
    linewidth=3,
    label_fontsize=12
):
    assert len(x_data) == len(y_data1)

    fig, ax = plt.subplots()
    ax.plot(x_data, y_data1, linewidth=linewidth, color='red', label="Max")

    if y_data2 is not None:
        ax.plot(x_data, y_data2, linewidth=linewidth, color='blue', label="Min")
        ax.fill_between(x_data, y_data1, y_data2, facecolor='blue', alpha=0.1)

    if with_dates:
        fig.autofmt_xdate()

    plt.title(title, fontsize=15)
    plt.xlabel(x_label, fontsize=label_fontsize)
    plt.ylabel(y_label, fontsize=label_fontsize)
    plt.legend()
    plt.tick_params(axis="both", labelsize=14)
    plt.tight_layout()
    plt.show()


def scatter_plot(
    x_data: list,
    y_data: list,
    title: str,
    x_label: str,
    y_label: str,
    cmap: Colormap = Colormap.Defaut,
    color_max_axis=None,
):
    plt.scatter(x=x_data, y=y_data, cmap=cmap.value, c=color_max_axis)
    plt.title(label=title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def histogram_plot(x_data, bins, title, x_label, y_label, label_fontsize=12):
    plt.hist(x_data, bins=bins, linewidth=3, edgecolor='black')
    plt.title(title, fontsize=15)
    plt.xlabel(x_label, fontsize=label_fontsize)
    plt.ylabel(y_label, fontsize=label_fontsize)
    plt.show()
