def color_bars(ax, x_values_list, colors_map):
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


def color_labels(ax, colors_map, orientation="v"):
    if orientation == "v":
        labels = ax.get_xticklabels()
    if orientation == "h":
        labels = ax.get_yticklabels()

    for label in labels:
        label_text = label.get_text()
        color = colors_map.get(label_text)

        if color is not None:
            label.set_color(color)
