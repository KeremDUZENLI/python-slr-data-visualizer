from output._0_helpers import (
    format_label_value,
)
import matplotlib.patches as Patch


def draw_bar_1D(ax, x_values, y_values, labels_spec, orientation="v"):
    x_values_list = []
    for x_value in x_values:
        x_value_str = format_label_value(x_value)
        x_values_list.append(x_value_str)

    positions = []
    index = 0
    for _ in x_values_list:
        positions.append(index)
        index += 1

    if orientation == "v":
        for pos, height in zip(positions, y_values):
            ax.bar(pos, height)

        ax.set_xticks(positions)
        ax.set_xticklabels(x_values_list, rotation=labels_spec["rotation"])
        ax.set_xlabel(labels_spec["x_label"])
        ax.set_ylabel(labels_spec["y_label"])

    if orientation == "h":
        for pos, width in zip(positions, y_values):
            ax.barh(pos, width)

        ax.set_yticks(positions)
        ax.set_yticklabels(x_values_list)
        ax.set_xlabel(labels_spec["y_label"])
        ax.set_ylabel(labels_spec["x_label"])
        ax.invert_yaxis()

    ax.set_title(labels_spec["title"])

    return x_values_list


def color_bars(ax, colors_map, x_values_list):
    index = 0

    bars = ax.patches
    for bar in bars:
        if index >= len(x_values_list):
            break

        label = x_values_list[index]

        color = colors_map.get(label)
        if color is None:
            color = "#cccccc"

        bar.set_facecolor(color)
        index += 1


def color_labels(ax, colors_map, axis="x"):
    if axis == "x":
        labels = ax.get_xticklabels()
    if axis == "y":
        labels = ax.get_yticklabels()

    for label in labels:
        label_text = label.get_text()
        color = colors_map.get(label_text)

        if color is not None:
            label.set_color(color)


def create_legend(ax, colors_map, values, title, loc):
    handles = []

    for value in values:
        value_str = format_label_value(value)
        color = colors_map.get(value_str)

        patch = Patch.Patch(
            facecolor=color,
            edgecolor="none",
            label=value_str,
        )
        handles.append(patch)

    ax.legend(
        handles=handles,
        title=title,
        loc=loc,
    )
