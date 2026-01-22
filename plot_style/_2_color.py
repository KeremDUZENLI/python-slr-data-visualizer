DEFAULT_COLOR = "#cccccc"


def color_bar(ax, coloring_values_list, colors_map, border=False):
    index = 0

    bars = ax.patches
    for bar in bars:
        if index >= len(coloring_values_list):
            break

        label = coloring_values_list[index]
        color = colors_map.get(label)

        if color is None:
            color = DEFAULT_COLOR

        bar.set_facecolor(color)

        if border:
            bar.set_edgecolor("black")
            bar.set_linewidth(1)

        index += 1


def color_area(ax, coloring_values_list, colors_map, border=False):
    index = 0

    areas = ax.collections
    for area in areas:
        if index >= len(coloring_values_list):
            break

        label = coloring_values_list[index]
        color = colors_map.get(label)

        if color is None:
            color = DEFAULT_COLOR

        area.set_facecolor(color)

        if border:
            area.set_edgecolor("black")
            area.set_linewidth(1)

        index += 1


def color_pie(ax, coloring_values_list, colors_map, border=False):
    slices = ax.patches
    for slice, label in zip(slices, coloring_values_list):
        color = colors_map.get(label)

        if color is None:
            color = DEFAULT_COLOR

        slice.set_facecolor(color)

        if border:
            slice.set_edgecolor("black")
            slice.set_linewidth(1)


def color_sunburst(ax, coloring_values_list, colors_map, border=False):
    colors = []

    for label in coloring_values_list:
        color = colors_map.get(label)

        if color is None:
            color = DEFAULT_COLOR

        colors.append(color)

    ax.update_traces(marker=dict(colors=colors))

    if border:
        ax.update_traces(marker=dict(line=dict(color="black", width=1)))


def color_heatmap(ax, matrix, cmap):
    ax.imshow(matrix, cmap=cmap, aspect="auto")


def color_bar_labels(ax, colors_map, orientation="v"):
    if orientation == "v":
        labels = ax.get_xticklabels()
    if orientation == "h":
        labels = ax.get_yticklabels()

    for label in labels:
        label_text = label.get_text()
        color = colors_map.get(label_text)

        if color is not None:
            label.set_color(color)


def color_pie_labels(ax, color, target=None):
    for text in ax.texts:
        gid = text.get_gid()
        if target == "inner" and gid == "pie_label_inner":
            text.set_color(color)
        if target == "outer" and gid == "pie_label_outer":
            text.set_color(color)
        if target == None:
            text.set_color(color)


def color_sunburst_labels(ax, color, target=None):
    for trace in ax.data:
        if trace.type == "sunburst":
            count = len(trace.labels)
            existing_color = trace.insidetextfont.color or DEFAULT_COLOR

            if isinstance(existing_color, (list, tuple)):
                current_colors = list(existing_color)
            else:
                current_colors = [existing_color] * count

            parents = trace.parents
            for i, parent in enumerate(parents):
                is_inner = parent == ""

                if target == "inner" and is_inner:
                    current_colors[i] = color
                if target == "outer" and not is_inner:
                    current_colors[i] = color
                if target is None:
                    current_colors[i] = color

            trace.update(insidetextfont=dict(color=current_colors))


def color_heatmap_labels(ax, color):
    for text in ax.texts:

        if text.get_gid() == "labels_heatmap_numbers":
            text.set_color(color)


def color_labels_extra(ax, colors_map):
    for text in ax:
        key = text.get_text()
        color = colors_map.get(key)

        if color is not None:
            text.set_color(color)
