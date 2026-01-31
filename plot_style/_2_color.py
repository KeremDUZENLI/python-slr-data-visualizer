import matplotlib.colors as mcolors

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


def color_heatmap(ax, matrix, cmap):
    ax.imshow(matrix, cmap=cmap, aspect="auto")


def color_scatter(ax, config):
    for collection in ax.collections:
        collection.set_facecolor(config.get("facecolor"))
        collection.set_edgecolor(config.get("edgecolor"))
        collection.set_linewidth(config.get("edgewidth"))
        collection.set_alpha(config.get("opacity"))


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


def color_sankey_nodes(ax, labels_list, colors_map, pad=15, thickness=20):
    trace = ax.data[0]
    colors = list(trace.node.color)

    for i, label in enumerate(labels_list):
        color = colors_map.get(label)
        if color:
            colors[i] = color

    trace.node.pad = pad
    trace.node.thickness = thickness
    trace.node.color = colors


def color_sankey_links(ax, color, opacity=0.25):
    trace = ax.data[0]

    if color in ["source", "target"]:
        indices = getattr(trace.link, color)
        base_colors = [trace.node.color[i] for i in indices]
    else:
        base_colors = color

    if isinstance(base_colors, list):
        new_colors = [_hex_to_rgba(color, opacity) for color in base_colors]
        trace.link.color = new_colors
    else:
        trace.link.color = _hex_to_rgba(base_colors, opacity)


def color_map(ax, cmap, border=False, frame=False):
    update_dict = {
        "colorscale": cmap,
    }

    if border == True:
        update_dict["marker"] = {
            "line": {
                "color": "black",
                "width": 0.5,
            }
        }
    if border == False:
        update_dict["marker"] = {
            "line": {
                "width": 0,
            }
        }

    ax.update_traces(update_dict)
    ax.update_layout(geo=dict(showframe=frame))


def color_prisma(ax, fillcolor, fontcolor, nodes=None):
    if nodes:
        for node in nodes:
            ax.node(
                node,
                fillcolor=fillcolor,
                fontcolor=fontcolor,
            )


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


def color_heatmap_labels(ax, color):
    for text in ax.texts:

        if text.get_gid() == "labels_heatmap_numbers":
            text.set_color(color)


def color_sunburst_labels(ax, color, target=None):
    for trace in ax.data:
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


def color_sankey_labels(ax, color):
    for trace in ax.data:
        trace.update(textfont=dict(color=color))

    ax.update_layout(title_font=dict(color=color))


def color_map_labels(ax, color):
    ax.update_layout(
        title_font=dict(color=color),
    )

    ax.update_traces(
        colorbar=dict(
            title_font=dict(color=color),
            tickfont=dict(color=color),
        )
    )


def color_prisma_labels(ax, fontcolors_map):
    ax.edge_attr["fontcolor"] = fontcolors_map["fontcolor_edge"]
    ax.node_attr["fontcolor"] = fontcolors_map["fontcolor_node"]
    ax.edge_attr["color"] = fontcolors_map["color_edge"]


def color_labels_extra(ax, colors_map):
    for text in ax:
        key = text.get_text()
        color = colors_map.get(key)

        if color is not None:
            text.set_color(color)


def _hex_to_rgba(color, opacity):
    if isinstance(color, str) and color.startswith("#"):
        clean = color.lstrip("#")
        if len(clean) in (6, 8):
            r = int(clean[0:2], 16)
            g = int(clean[2:4], 16)
            b = int(clean[4:6], 16)
            return f"rgba({r}, {g}, {b}, {opacity})"
        return color

    try:
        rgb = mcolors.to_rgb(color)
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        return f"rgba({r}, {g}, {b}, {opacity})"
    except (ValueError, TypeError):
        return color
