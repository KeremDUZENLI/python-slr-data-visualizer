from helper.helper import (
    get_unique_values,
    calculate_labels_pos_pie,
    offset_frame,
    format_labels,
)
import numpy as np


def draw_bar_1D(ax, x_values, y_values, labels_spec, orientation="v"):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    positions = []
    index = 0
    for _ in x_values_list:
        positions.append(index)
        index += 1

    if orientation == "v":
        for pos, height in zip(positions, y_values):
            ax.bar(pos, height)

        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_values_list,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))

    if orientation == "h":
        for pos, width in zip(positions, y_values):
            ax.barh(pos, width)

        ax.set_yticks(positions)
        ax.set_yticklabels(x_values_list)
        ax.set_xlabel(labels_spec.get("y_label", ""))
        ax.set_ylabel(labels_spec.get("x_label", ""))
        ax.invert_yaxis()

    offset_frame(ax=ax, height=y_values, orientation=orientation, offset=1)
    ax.set_title(labels_spec.get("title", ""))

    return x_values_list


def draw_bar_2D(ax, x_values, y_values, z_values, labels_spec, orientation="v"):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    z_values_list = []
    for z_value in z_values:
        z_values_list.append(str(z_value))

    x_uniques_list = get_unique_values(x_values_list)
    z_uniques_list = get_unique_values(z_values_list)

    num_groups = len(z_uniques_list)
    total_width = 0.8
    single_width = total_width / num_groups

    positions = []
    index = 0
    for _ in x_uniques_list:
        positions.append(index)
        index += 1

    if orientation == "v":
        for x_val, y_val, z_val in zip(x_values_list, y_values, z_values_list):
            x_index = x_uniques_list.index(x_val)
            z_index = z_uniques_list.index(z_val)

            offset = (z_index * single_width) - (total_width / 2) + (single_width / 2)
            final_pos = x_index + offset

            ax.bar(final_pos, y_val, width=single_width)

        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_uniques_list,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))

    if orientation == "h":
        for x_val, y_val, z_val in zip(x_values_list, y_values, z_values_list):
            x_index = x_uniques_list.index(x_val)
            z_index = z_uniques_list.index(z_val)

            offset = (z_index * single_width) - (total_width / 2) + (single_width / 2)
            final_pos = x_index + offset

            ax.barh(final_pos, y_val, height=single_width)

        ax.set_yticks(positions)
        ax.set_yticklabels(x_uniques_list)
        ax.set_xlabel(labels_spec.get("y_label", ""))
        ax.set_ylabel(labels_spec.get("x_label", ""))
        ax.invert_yaxis()

    offset_frame(ax=ax, height=y_values, orientation=orientation, offset=1)
    ax.set_title(labels_spec.get("title", ""))

    return z_values_list


def draw_stacked(
    ax, x_values, y_values, z_values, labels_spec, orientation="v", stack_order=None
):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    z_values_list = []
    for z_value in z_values:
        z_values_list.append(str(z_value))

    x_uniques_list = get_unique_values(x_values_list)
    z_uniques_list = stack_order if stack_order else get_unique_values(z_values_list)

    # x_map = {
    # '2015': 0, '2016': 1, '2017': 2, '2018': 3, '2019': 4,
    # '2020': 5, '2021': 6, '2022': 7, '2023': 8, '2024': 9}
    x_map = {}
    index_counter = 0
    for x_value in x_uniques_list:
        x_map[x_value] = index_counter
        index_counter += 1

    # z_map = {
    # 'VR': [2.0, 1.0, 9.0, 4.0, 7.0, 10.0, 7.0, 14.0, 13.0, 9.0],
    # 'AR': [3.0, 4.0, 4.0, 2.0, 3.0, 2.0, 2.0, 4.0, 4.0, 0.0],
    # 'MR': [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 1.0, 1.0],
    # 'XR': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0]}
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
    coloring_values_list = []

    if orientation == "v":
        for z_value in reversed(z_uniques_list):
            row_data = z_map[z_value]
            ax.bar(positions, row_data, bottom=y_values_total, label=z_value)
            y_values_total = [b + r for b, r in zip(y_values_total, row_data)]
            coloring_values_list.extend([z_value] * len(positions))

        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_uniques_list,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))

    if orientation == "h":
        for z_value in reversed(z_uniques_list):
            row_data = z_map[z_value]
            ax.barh(positions, row_data, left=y_values_total, label=z_value)
            y_values_total = [b + r for b, r in zip(y_values_total, row_data)]
            coloring_values_list.extend([z_value] * len(positions))

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
            coloring_values_list.append(z_value)

        ax.stackplot(positions, stack_data, labels=coloring_values_list)
        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_uniques_list,
            rotation=labels_spec.get("rotation", 0),
            ha="right",
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))
        orientation = "v"

    offset_frame(ax=ax, height=y_values_total, orientation=orientation, offset=1)
    ax.set_title(labels_spec.get("title", ""))

    return coloring_values_list


def draw_pie(ax, x_values, y_values, labels_spec):
    x_values_list = []
    for x in x_values:
        x_values_list.append(str(x))

    lbls = format_labels(values=x_values_list, decimal=1)
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

    return x_values_list


def draw_pie_nested(
    ax, inner_labels, inner_labels_count, outer_labels, outer_labels_count, labels_spec
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
        startangle=90,
        radius=0.5,
        pctdistance=pcnt_inner,
        wedgeprops=dict(width=0.5, edgecolor="w"),
    )
    for text in autotexts_inner:
        text.set_gid("pie_label_inner")

    _, _, autotexts_outer = ax.pie(
        x=outer_labels_count,
        autopct=lbls_outer,
        startangle=90,
        radius=1.0,
        pctdistance=pcnt_outer,
        wedgeprops=dict(width=0.5, edgecolor="w"),
    )
    for text in autotexts_outer:
        text.set_gid("pie_label_outer")

    ax.set_title(labels_spec.get("title", ""))
    ax.axis("equal")

    return inner_labels_list + outer_labels_list


def draw_heatmap(ax, x_values, y_values, z_values, labels_spec):
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
    ax, x_values, y_values, z_values, labels_spec, count_values, markersize
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


def draw_sunburst(ax, all_labels, all_parents, all_counts, labels_spec):
    fmt = "%{label}<br>%{percentRoot:.1%}"

    trace = {
        "type": "sunburst",
        "labels": all_labels,
        "parents": all_parents,
        "values": all_counts,
        "branchvalues": "total",
        "maxdepth": 2,
        "texttemplate": fmt,
        "textinfo": "text",
        "insidetextorientation": "auto",
    }

    ax.add_trace(trace)

    ax.update_layout(
        title=labels_spec.get("title", ""),
        margin=dict(t=60, l=0, r=0, b=0),
        width=500,
        height=500,
    )

    return ax


def draw_sankey(ax, labels, sources, targets, values, labels_spec):
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

    ax.update_layout(
        title=labels_spec.get("title", ""),
        margin=dict(t=60, l=0, r=0, b=0),
        width=500,
        height=500,
    )

    return ax


def draw_map(ax, countries, counts, labels_spec):
    trace = {
        "type": "choropleth",
        "locations": countries,
        "locationmode": "country names",
        "z": counts,
        "showscale": True,
    }

    ax.add_trace(trace)

    ax.update_layout(
        title=labels_spec.get("title", ""),
        margin=dict(t=60, l=0, r=0, b=0),
        width=500,
        height=500,
        geo={
            "projection": {"type": "natural earth"},
        },
    )

    return ax


def draw_prisma(dot, values, labels_spec):
    # --- 1. Set Main Title ---
    title = labels_spec.get("title", "")
    if title:
        dot.attr(label=f"\n{title}\n", labelloc="t")

    # --- Node Style Config (White Box) ---
    box_style = {
        "shape": "box",
        "style": "rounded,filled",
        "fillcolor": "white",
        "height": "0.6",
        "width": "4.5",
    }

    # --- Exclusion/Note Style Config (Grey Box) ---
    note_style = {
        "shape": "note",
        "style": "filled",
        "fillcolor": "#F9F9F9",
        "fontsize": "12",
    }

    # 1. IDENTIFICATION PHASE
    dot.node(
        "search",
        f"Studies identified via\nsystematic search\n(n = {values['search']})",
        **box_style,
    )

    dot.node(
        "duplicates",
        f"Duplicates & non-relevant records removed\n(n = {values['duplicates']})",
        **box_style,
    )

    dot.node(
        "screening",
        f"Studies after deduplication\n(n = {values['screening']})",
        **box_style,
    )

    dot.edge("search", "duplicates")
    dot.edge("duplicates", "screening")

    # 2. SCREENING PHASE
    dot.node(
        "excluded",
        f"Studies excluded (score < 4.5)\n(n = {values['excluded']})",
        **box_style,
    )

    dot.node(
        "eligible",
        f"Studies passing eligibility screening\n(n = {values['eligible']})",
        **box_style,
    )

    dot.edge("screening", "excluded")
    dot.edge("screening", "eligible")

    # 3. FILTERING PHASE
    dot.node(
        "religious",
        f"Studies on religious buildings\n(n = {values['religious']})",
        **box_style,
    )

    dot.node("hmd", f"Studies using HMD technology\n(n = {values['hmd']})", **box_style)

    dot.edge("eligible", "religious")
    dot.edge("religious", "hmd")

    # 4. FINAL INCLUSION
    dot.node(
        "final",
        f"Final selected studies:\nReconstruction-focused\n(n = {values['final']})",
        **box_style,
        penwidth="2",
    )

    dot.edge("hmd", "final")

    # 5. SIDE NOTES (Exclusion Criteria)
    # We use html-like labels for bullet points if needed, or plain text
    dot.node(
        "note1",
        "Step 1 - Exclusions:\n• Duplicate records\n• Non-peer-reviewed\n• Book chapters",
        **note_style,
    )

    dot.node(
        "note2",
        "Step 2 - Screening Criteria:\n✔ Case study or prototype\n✔ Historical reconstruction\n✔ VR/AR/MR/XR integration",
        **note_style,
    )

    dot.node(
        "note3",
        "Step 3 - Final Filtering:\n✔ Religious buildings\n✔ HMD implementation\n✔ Reconstruction focus",
        **note_style,
    )

    # Align notes with invisible edges or constrained ranks
    dot.edge("duplicates", "note1", style="dotted", arrowhead="none")
    dot.edge("screening", "note2", style="dotted", arrowhead="none")
    dot.edge("hmd", "note3", style="dotted", arrowhead="none")

    return dot
