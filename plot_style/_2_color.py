def color_bars(ax, coloring_values_list, colors_map, border=False):
    index = 0

    bars = ax.patches
    for bar in bars:
        if index >= len(coloring_values_list):
            break

        label = coloring_values_list[index]
        color = colors_map.get(label)

        if color is None:
            color = "#cccccc"

        bar.set_facecolor(color)

        if border:
            bar.set_edgecolor("black")
            bar.set_linewidth(1)

        index += 1


def color_slices(ax, coloring_values_list, colors_map, border=False):
    slices = ax.patches
    for slice, label in zip(slices, coloring_values_list):
        color = colors_map.get(label)

        if color is None:
            color = "#cccccc"

        slice.set_facecolor(color)

        if border:
            slice.set_edgecolor("black")
            slice.set_linewidth(1)


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


def color_labels_pie(ax, color):
    for label in ax.texts:
        label.set_color(color)


def color_labels_extra(ax, colors_map):
    for text in ax:
        key = text.get_text()
        color = colors_map.get(key)

        if color is not None:
            text.set_color(color)
