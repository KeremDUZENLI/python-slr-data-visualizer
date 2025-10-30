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


def plot_chart_bar_group(dataset, x_axis, y_axis, group_axis, x_label, y_label, title):
    x_values = sorted(set(dataset[x_axis]))
    groups = sorted(set(dataset[group_axis]))

    x_pos, width, tick_pos = _compute_positions(len(x_values), len(groups))

    for i, group_value in enumerate(groups):
        y_values = _get_group_values(
            dataset, x_axis, y_axis, group_axis, x_values, group_value
        )
        plt.bar(x_pos + i * width, y_values, width, label=group_value)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(tick_pos, x_values)
    plt.legend(title=group_axis)
    plt.show()


def _compute_positions(xCount, groupCount):
    width = 0.8 / max(1, groupCount)
    x_pos = np.arange(xCount)
    tick_pos = x_pos + width * (groupCount - 1) / 2
    return x_pos, width, tick_pos


def _get_group_values(dataset, x_axis, y_axis, group_axis, x_values, group_value):
    y_values = []
    for x in x_values:
        count = 0
        for j in range(len(dataset[y_axis])):
            if dataset[x_axis][j] == x and dataset[group_axis][j] == group_value:
                count = dataset[y_axis][j]
                break
        y_values.append(count)
    return y_values
