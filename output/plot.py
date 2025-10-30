import numpy as np
import matplotlib.pyplot as plt


def plot_chart_bar(dataset, x_axis, y_axis, x_label, y_label, title):
    x_values = dataset[x_axis]
    y_values = dataset[y_axis]

    plt.bar(x_values, y_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def plot_chart_bar_group(dataset, x_axis, y_axis, grp_axis, x_label, y_label, title):
    x_values = _unique(dataset[x_axis])
    grp_values = _unique(dataset[grp_axis])

    x_pos, width, tick_pos = _compute_positions(len(x_values), len(grp_values))

    for i, grp_value in enumerate(grp_values):
        y_values = _get_group_values(
            dataset, x_axis, y_axis, grp_axis, x_values, grp_value
        )
        plt.bar(x_pos + i * width, y_values, width, label=grp_value)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(tick_pos, x_values)
    plt.legend(title=grp_axis)
    plt.show()


def _compute_positions(xCount, groupCount):
    width = 0.8 / max(1, groupCount)
    x_pos = np.arange(xCount)
    tick_pos = x_pos + width * (groupCount - 1) / 2
    return x_pos, width, tick_pos


def _get_group_values(dataset, x_axis, y_axis, group_axis, x_values, grp_value):
    y_values = []
    for x in x_values:
        count = 0
        for j in range(len(dataset[y_axis])):
            if dataset[x_axis][j] == x and dataset[group_axis][j] == grp_value:
                count = dataset[y_axis][j]
                break
        y_values.append(count)
    return y_values


def _unique(seq):
    out = []
    seen = set()
    for v in seq:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out
