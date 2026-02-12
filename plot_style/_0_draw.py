from helper.helper import (
    get_unique_values,
    calculate_labels_pos_pie,
    format_labels,
)
import numpy as np


def draw_bar_1D(
    ax,
    x_values,
    y_values,
    labels_spec,
    orientation="vertical",
):
    coloring_values = []
    for x_value in x_values:
        coloring_values.append(str(x_value))

    positions = []
    index = 0
    for _ in coloring_values:
        positions.append(index)
        index += 1

    if orientation == "vertical":
        for pos, height in zip(positions, y_values):
            ax.bar(pos, height)

        ax.set_xticks(positions)
        ax.set_xticklabels(
            coloring_values,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))

    if orientation == "horizontal":
        for pos, width in zip(positions, y_values):
            ax.barh(pos, width)

        ax.set_yticks(positions)
        ax.set_yticklabels(coloring_values)
        ax.set_xlabel(labels_spec.get("y_label", ""))
        ax.set_ylabel(labels_spec.get("x_label", ""))
        ax.invert_yaxis()

    _offset_frame(ax=ax, height=y_values, orientation=orientation, offset=1)
    ax.set_title(labels_spec.get("title", ""))

    return coloring_values


def draw_bar_2D(
    ax,
    x_values,
    y_values,
    z_values,
    labels_spec,
    orientation="vertical",
    stack_order=None,
):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    coloring_values = []
    for z_value in z_values:
        coloring_values.append(str(z_value))

    x_uniques_list = get_unique_values(x_values_list)
    z_uniques_list = stack_order if stack_order else get_unique_values(coloring_values)

    num_groups = len(z_uniques_list)
    golden_ratio = 1.618
    single_bar_width = 0.22
    total_width = num_groups * single_bar_width

    positions = []
    for i in range(len(x_uniques_list)):
        positions.append(i * golden_ratio)

    pos_map = dict(zip(x_uniques_list, positions))
    z_map = {val: i for i, val in enumerate(z_uniques_list)}

    if orientation == "vertical":
        for x_val, y_val, z_val in zip(x_values_list, y_values, coloring_values):
            x_center = pos_map[x_val]
            z_index = z_map[z_val]

            offset = (
                (z_index * single_bar_width)
                - (total_width / 2)
                + (single_bar_width / 2)
            )
            final_pos = x_center + offset

            ax.bar(final_pos, y_val, width=single_bar_width)

        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_uniques_list,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))

    if orientation == "horizontal":
        for x_val, y_val, z_val in zip(x_values_list, y_values, coloring_values):
            x_center = pos_map[x_val]
            z_index = z_map[z_val]

            offset = (
                (z_index * single_bar_width)
                - (total_width / 2)
                + (single_bar_width / 2)
            )
            final_pos = x_center + offset

            ax.barh(final_pos, y_val, height=single_bar_width)

        ax.set_yticks(positions)
        ax.set_yticklabels(x_uniques_list)
        ax.set_xlabel(labels_spec.get("y_label", ""))
        ax.set_ylabel(labels_spec.get("x_label", ""))
        ax.invert_yaxis()

    _offset_frame(ax=ax, height=y_values, orientation=orientation, offset=1)
    ax.set_title(labels_spec.get("title", ""))

    return coloring_values


def draw_stacked(
    ax,
    x_values,
    y_values,
    z_values,
    labels_spec,
    orientation="vertical",
    stack_order=None,
):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    z_values_list = []
    for z_value in z_values:
        z_values_list.append(str(z_value))

    x_uniques_list = get_unique_values(x_values_list)
    z_uniques_list = stack_order if stack_order else get_unique_values(z_values_list)

    x_map = {}
    index_counter = 0
    for x_value in x_uniques_list:
        x_map[x_value] = index_counter
        index_counter += 1

    z_map = {}
    for z_value in z_uniques_list:
        zeros_list = []
        for _ in range(len(x_uniques_list)):
            zeros_list.append(0.0)
        z_map[z_value] = zeros_list

    for i in range(len(x_values_list)):
        x = x_values_list[i]
        y = y_values[i]
        z = z_values_list[i]

        col_idx = x_map.get(x)
        if col_idx is not None:
            z_map[z][col_idx] = z_map[z][col_idx] + float(y)

    positions = []
    index = 0
    for _ in x_uniques_list:
        positions.append(index)
        index += 1

    y_values_total = [0.0] * len(x_uniques_list)
    coloring_values = []

    if orientation == "vertical":
        for z_value in reversed(z_uniques_list):
            row_data = z_map[z_value]
            ax.bar(positions, row_data, bottom=y_values_total, label=z_value)
            y_values_total = [b + r for b, r in zip(y_values_total, row_data)]
            coloring_values.extend([z_value] * len(positions))

        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_uniques_list,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))

    if orientation == "horizontal":
        for z_value in reversed(z_uniques_list):
            row_data = z_map[z_value]
            ax.barh(positions, row_data, left=y_values_total, label=z_value)
            y_values_total = [b + r for b, r in zip(y_values_total, row_data)]
            coloring_values.extend([z_value] * len(positions))

        ax.set_yticks(positions)
        ax.set_yticklabels(x_uniques_list)
        ax.set_xlabel(labels_spec.get("y_label", ""))
        ax.set_ylabel(labels_spec.get("x_label", ""))
        ax.invert_yaxis()

    if orientation == "area":
        stack_data = []
        for z_value in reversed(z_uniques_list):
            row_data = z_map[z_value]
            stack_data.append(row_data)
            y_values_total = [b + r for b, r in zip(y_values_total, row_data)]
            coloring_values.append(z_value)

        ax.stackplot(positions, stack_data, labels=coloring_values)
        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_uniques_list,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))
        orientation = "vertical"

    _offset_frame(ax=ax, height=y_values_total, orientation=orientation, offset=1)
    ax.set_title(labels_spec.get("title", ""))

    return coloring_values


def draw_pie(
    ax,
    x_values,
    y_values,
    labels_spec,
):
    coloring_values = []
    for x in x_values:
        coloring_values.append(str(x))

    lbls = format_labels(values=coloring_values, decimal=1)
    pcnt = calculate_labels_pos_pie(inner_radius=0.0, outer_radius=1.0)

    _, _, autotexts = ax.pie(
        x=y_values,
        autopct=lbls,
        startangle=90,
        radius=1.0,
        pctdistance=pcnt,
    )
    for text in autotexts:
        text.set_gid("pie_label")

    ax.set_title(labels_spec.get("title", ""))
    ax.axis("equal")

    return coloring_values


def draw_pie_nested(
    ax,
    inner_labels,
    inner_labels_count,
    outer_labels,
    outer_labels_count,
    labels_spec,
):
    inner_labels_list = []
    for i in inner_labels:
        inner_labels_list.append(str(i))
    lbls_inner = format_labels(values=inner_labels_list, decimal=1)
    pcnt_inner = calculate_labels_pos_pie(inner_radius=0.0, outer_radius=0.5)

    outer_labels_list = []
    for o in outer_labels:
        outer_labels_list.append(str(o))
    lbls_outer = format_labels(values=outer_labels_list, decimal=1)
    pcnt_outer = calculate_labels_pos_pie(inner_radius=0.5, outer_radius=1.0)

    _, _, autotexts_inner = ax.pie(
        x=inner_labels_count,
        autopct=lbls_inner,
        startangle=0,
        radius=0.5,
        pctdistance=pcnt_inner,
        wedgeprops=dict(width=0.5, edgecolor="w"),
    )
    for text in autotexts_inner:
        text.set_gid("pie_label_inner")

    _, _, autotexts_outer = ax.pie(
        x=outer_labels_count,
        autopct=lbls_outer,
        startangle=0,
        radius=1.0,
        pctdistance=pcnt_outer,
        wedgeprops=dict(width=0.5, edgecolor="w"),
    )
    for text in autotexts_outer:
        text.set_gid("pie_label_outer")

    ax.set_title(labels_spec.get("title", ""))
    ax.axis("equal")

    return inner_labels_list + outer_labels_list


def draw_pie_nested(
    ax,
    inner_labels,
    inner_labels_count,
    outer_labels,
    outer_labels_count,
    labels_spec,
    inner_labels_display,
    outer_labels_display,
    labels_hide_percent,
):
    lbls_inner = format_labels(
        values=inner_labels_display, decimal=1, threshold=labels_hide_percent
    )
    pcnt_inner = calculate_labels_pos_pie(inner_radius=0.0, outer_radius=0.5)

    lbls_outer = format_labels(
        values=outer_labels_display, decimal=1, threshold=labels_hide_percent
    )
    pcnt_outer = calculate_labels_pos_pie(inner_radius=0.5, outer_radius=1.0)

    _, _, autotexts_inner = ax.pie(
        x=inner_labels_count,
        autopct=lbls_inner,
        startangle=0,
        radius=0.5,
        pctdistance=pcnt_inner,
        wedgeprops=dict(width=0.5, edgecolor="w"),
    )
    for text in autotexts_inner:
        text.set_gid("pie_label_inner")

    _, _, autotexts_outer = ax.pie(
        x=outer_labels_count,
        autopct=lbls_outer,
        startangle=0,
        radius=1.0,
        pctdistance=pcnt_outer,
        wedgeprops=dict(width=0.5, edgecolor="w"),
    )
    for text in autotexts_outer:
        text.set_gid("pie_label_outer")

    ax.set_title(labels_spec.get("title", ""))
    ax.axis("equal")

    return [str(i) for i in inner_labels] + [str(o) for o in outer_labels]


def draw_heatmap(
    ax,
    x_values,
    y_values,
    z_values,
    labels_spec,
):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    z_values_list = []
    for z_value in z_values:
        z_values_list.append(str(z_value))

    x_uniques_list = get_unique_values(x_values_list)
    z_uniques_list = get_unique_values(z_values_list)

    matrix = np.zeros((len(z_uniques_list), len(x_uniques_list)))

    x_map = {}
    index_counter = 0
    for x_value in x_uniques_list:
        x_map[x_value] = index_counter
        index_counter += 1

    z_map = {}
    index_counter = 0
    for z_value in z_uniques_list:
        z_map[z_value] = index_counter
        index_counter += 1

    for i in range(len(x_values_list)):
        x = x_values_list[i]
        y = y_values[i]
        z = z_values_list[i]

        row = z_map.get(z)
        col = x_map.get(x)

        if row is not None and col is not None:
            matrix[row, col] = matrix[row, col] + float(y)

    ax.set_xticks(np.arange(len(x_uniques_list)))
    ax.set_yticks(np.arange(len(z_uniques_list)))
    ax.set_xticklabels(
        x_uniques_list,
        rotation=labels_spec.get("rotation", 0),
        ha="right",
    )
    ax.set_yticklabels(z_uniques_list)
    ax.set_xlabel(labels_spec.get("x_label", ""))
    ax.set_ylabel(labels_spec.get("y_label", ""))
    ax.set_title(labels_spec.get("title", ""))

    return matrix


def draw_scatter(
    ax,
    x_values,
    y_values,
    z_values,
    labels_spec,
    count_values,
    markersize,
):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    z_values_list = []
    for z_value in z_values:
        z_values_list.append(str(z_value))

    x_uniques_list = get_unique_values(x_values_list)
    z_uniques_list = get_unique_values(z_values_list)

    x_map = {}
    index_counter = 0
    for x_value in x_uniques_list:
        x_map[x_value] = index_counter
        index_counter += 1

    z_map = {}
    index_counter = 0
    for z_value in z_uniques_list:
        z_map[z_value] = index_counter
        index_counter += 1

    plot_x = []
    plot_y = []
    plot_bubble = []

    min_count = count_values[0]
    max_count = count_values[1]

    min_size = markersize[0] * markersize[0]
    max_size = markersize[1] * markersize[1]

    for i in range(len(x_values_list)):
        x = x_values_list[i]
        y = y_values[i]
        z = z_values_list[i]

        col = x_map.get(x)
        row = z_map.get(z)

        if row is not None and col is not None:
            plot_x.append(col)
            plot_y.append(row)

            if max_count == min_count:
                norm = 0.5
            else:
                norm = (y - min_count) / (max_count - min_count)

            size = min_size + (norm * (max_size - min_size))
            plot_bubble.append(size)

    ax.scatter(
        plot_x,
        plot_y,
        s=plot_bubble,
        zorder=3,
    )
    ax.set_xticks(range(len(x_uniques_list)))
    ax.set_yticks(range(len(z_uniques_list)))
    ax.set_xticklabels(
        x_uniques_list,
        rotation=labels_spec.get("rotation", 0),
        ha="right",
    )
    ax.set_yticklabels(z_uniques_list)
    ax.set_xlabel(labels_spec.get("x_label", ""))
    ax.set_ylabel(labels_spec.get("y_label", ""))
    ax.set_title(labels_spec.get("title", ""))


def draw_sunburst(
    ax,
    all_labels,
    all_parents,
    all_counts,
    formatted_texts,
):
    trace = {
        "type": "sunburst",
        "labels": all_labels,
        "parents": all_parents,
        "values": all_counts,
        "branchvalues": "total",
        "sort": False,
        "maxdepth": 2,
        "text": formatted_texts,
        "textinfo": "text",
        "texttemplate": "%{text}",
        "insidetextorientation": "auto",
    }

    ax.add_trace(trace)
    return ax


def draw_sankey(
    ax,
    labels,
    sources,
    targets,
    values,
):
    trace = {
        "type": "sankey",
        "node": {
            "label": labels,
            "color": ["grey"] * len(labels),
        },
        "link": {
            "source": sources,
            "target": targets,
            "value": values,
        },
    }

    ax.add_trace(trace)
    return ax


def draw_map(
    ax,
    countries,
    counts,
):
    trace = {
        "type": "choropleth",
        "locations": countries,
        "locationmode": "country names",
        "z": counts,
        "showscale": True,
    }

    ax.add_trace(trace)
    return ax


def draw_prisma_nodes(
    dot,
    nodes,
):
    for node_id, label_text in nodes.items():
        dot.node(node_id, label_text)


def draw_prisma_edges(
    dot,
    edges,
):
    for src, dst in edges:
        dot.edge(src, dst)


def _offset_frame(ax, height, orientation, offset=1):
    max_height = max(height)
    change = max_height * (1 + (offset * 0.1))

    if orientation == "vertical":
        if max_height > 0:
            ax.set_ylim(0, change)

    if orientation == "horizontal":
        if max_height > 0:
            ax.set_xlim(0, change)
