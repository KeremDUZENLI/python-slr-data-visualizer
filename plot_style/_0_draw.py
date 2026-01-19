from helper.helper import (
    get_unique_values,
    calculate_labels_pos_pie,
    format_labels,
)


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

    ax.set_title(labels_spec.get("title", ""))

    return z_values_list


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
