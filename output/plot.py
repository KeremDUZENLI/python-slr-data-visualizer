import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.patches import Patch


COLORS = {
    "study_focus": {
        "Reconstruction": "#1f77b4",
        "Restoration": "#2ca02c",
        "Visualization": "#d62728",
    },
    "historical_site_type": {
        "Archaeological Site": "#6aa84f",
        "Artistic Feature": "#f6b26b",
        "Building": "#4a86e8",
        "Natural Space": "#8e7cc3",
    },
    "software_category": {
        "software_data": "#1f77b4",
        "software_modeling": "#2ca02c",
        "software_render": "#d62728",
    },
}


def plot_bar(
    dataset, x_axis, y_axis, x_label, y_label, title, orientation, grp_axis=None
):
    bar = _apply_bar_orient(orientation)
    x_values = dataset[x_axis]
    y_values = dataset[y_axis]

    label_colors = {}
    if grp_axis:
        values = _get_unique_values(field=dataset[grp_axis])
        colors = _apply_bar_colors(grp_axis=grp_axis, values=values)
        for value in values:
            mask = [v == value for v in dataset[grp_axis]]
            x_values_list = [x for x, m in zip(x_values, mask) if m]
            y_values_list = [y for y, m in zip(y_values, mask) if m]
            bar(
                x_values_list,
                y_values_list,
                label=value,
                color=colors[value],
            )
            for x_value in x_values_list:
                if x_value not in label_colors:
                    label_colors[x_value] = colors[value]
    else:
        bar(
            x_values,
            y_values,
        )

    _apply_bar_axes(
        orientation=orientation,
        x_label=x_label,
        y_label=y_label,
        rotation=45,
    )

    if grp_axis:
        _apply_axis_colors(orientation=orientation, colors=label_colors)
        plt.legend(title=_clean_label(name=grp_axis))

    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_bar_group(
    dataset, x_axis, y_axis, x_label, y_label, title, orientation, grp_axis
):
    bar = _apply_bar_orient(orientation)
    x_values = _get_unique_values(field=dataset[x_axis])
    values = _get_unique_values(field=dataset[grp_axis])
    y_values_stacked = _stack_group_values(
        dataset=dataset,
        x_axis=x_axis,
        y_axis=y_axis,
        grp_axis=grp_axis,
        x_values=x_values,
        grp_values=values,
    )
    width, axis_pos, tick_pos = _compute_label_positions(
        axis_count=len(x_values),
        grp_count=len(values),
    )
    colors = _apply_bar_colors(grp_axis=grp_axis, values=values)

    for i, value in enumerate(values):
        x_values_pos = axis_pos + i * width
        size = _apply_bar_size(orientation, width)
        bar(
            x_values_pos,
            y_values_stacked[i],
            label=value,
            color=colors[value],
            **size,
        )

    _apply_bar_axes(
        orientation=orientation,
        x_label=x_label,
        y_label=y_label,
        tick_pos=tick_pos,
        tick_labels=x_values,
        rotation=45,
    )

    plt.title(title)
    plt.legend(title=_clean_label(name=grp_axis))
    plt.tight_layout()
    plt.show()


def plot_stacked(dataset, x_axis, y_axis, x_label, y_label, title, kind, grp_axis):
    x_values = _get_unique_values(field=dataset[x_axis])
    label_values = _get_unique_values(field=dataset[grp_axis])
    y_values_stacked = _stack_group_values(
        dataset=dataset,
        x_axis=x_axis,
        y_axis=y_axis,
        grp_axis=grp_axis,
        x_values=x_values,
        grp_values=label_values,
    )
    x_pos = np.arange(len(x_values))

    _apply_graph_kind(
        kind=kind,
        x_pos=x_pos,
        values=y_values_stacked,
        label_values=label_values,
    )
    _apply_bar_axes(
        orientation="v",
        x_label=x_label,
        y_label=y_label,
        tick_pos=x_pos,
        tick_labels=x_values,
        rotation=45,
    )

    plt.title(title)
    plt.legend(title=_clean_label(name=grp_axis))
    plt.tight_layout()
    plt.show()


def plot_heatmap(
    dataset, x_axis, y_axis, x_label, y_label, title, count_axis, grp_axis=None
):
    x_values = _get_unique_values(field=dataset[x_axis])
    y_values = _get_unique_values(field=dataset[y_axis])

    r_index = {r: i for i, r in enumerate(y_values)}
    c_index = {c: i for i, c in enumerate(x_values)}
    mat = np.zeros((len(y_values), len(x_values)), dtype=float)

    if grp_axis:
        grp_values = _get_unique_values(field=dataset[grp_axis])
        colors = _apply_bar_colors(grp_axis=grp_axis, values=grp_values)

    number = len(dataset[count_axis])
    label_colors = {}
    for i in range(number):
        r_val = dataset[y_axis][i]
        c_val = dataset[x_axis][i]
        v = dataset[count_axis][i]

        r_vals = r_val if isinstance(r_val, list) else [r_val]
        c_vals = c_val if isinstance(c_val, list) else [c_val]

        for rv in r_vals:
            if rv in r_index:
                for c_val in c_vals:
                    if c_val in c_index:
                        mat[r_index[rv], c_index[c_val]] += v

        if grp_axis:
            group = dataset[grp_axis][i]
            color = colors.get(group)
            if color:
                for c_val in c_vals:
                    if c_val not in label_colors:
                        label_colors[c_val] = color

    plt.imshow(mat, aspect="auto")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(np.arange(len(x_values)), x_values, rotation=45, ha="right")
    plt.yticks(np.arange(len(y_values)), y_values)
    plt.colorbar()

    if grp_axis:
        _apply_axis_colors(orientation="v", colors=label_colors)
        handles = [
            Patch(facecolor=colors[value], edgecolor="none", label=value)
            for value in grp_values
            if colors.get(value)
        ]
        plt.legend(handles=handles, title=_clean_label(name=grp_axis))

    plt.tight_layout()
    plt.show()


def plot_pie(dataset, field, count, title):
    inner_labels = dataset[field]
    inner_values = dataset[count]

    lbls = _format_label(labels=inner_labels, decimal=1)
    pcnt = _center_label_percent(inner_radius=0.0, outer_radius=1.0)

    plt.pie(inner_values, autopct=lbls, startangle=90, radius=1.0, pctdistance=pcnt)
    plt.title(title)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


def plot_pie_group(dataset, field, count, title, grp_axis):
    inner_labels, inner_values, outer_labels, outer_values, outer_parents = (
        _get_hierarchy_values(
            dataset=dataset,
            field_parent=field,
            field_child=grp_axis,
            count=count,
        )
    )

    lbls_out = _format_label(labels=outer_labels, decimal=1)
    lbls_inn = _format_label(labels=inner_labels, decimal=1)
    pcnt_out = _center_label_percent(inner_radius=0.5, outer_radius=1.0)
    pcnt_inn = _center_label_percent(inner_radius=0.0, outer_radius=0.5)

    plt.pie(
        outer_values, autopct=lbls_out, startangle=90, radius=1.0, pctdistance=pcnt_out
    )
    plt.pie(
        inner_values, autopct=lbls_inn, startangle=90, radius=0.5, pctdistance=pcnt_inn
    )
    plt.title(title)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


def plot_sunburst(dataset, field, count, title, grp_axis):
    inner_labels, inner_values, outer_labels, outer_values, outer_parents = (
        _get_hierarchy_values(
            dataset=dataset,
            field_parent=field,
            field_child=grp_axis,
            count=count,
        )
    )

    labels = inner_labels + outer_labels
    parents = [""] * len(inner_labels) + outer_parents
    values = inner_values + outer_values
    fmt = f"%{{label}}<br>%{{percentRoot:.{1}%}}"

    fig = go.Figure(
        go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
            maxdepth=2,
            texttemplate=fmt,
            textinfo="text",
            insidetextorientation="auto",
        )
    )
    fig.update_layout(
        title=title,
        margin=dict(t=60, l=0, r=0, b=0),
    )
    fig.show()


def plot_sankey(dataset, title, column1, column2, column3):
    left_labels = _get_unique_values(field=dataset[column1])
    mid_labels = _get_unique_values(field=dataset[column2])
    right_labels = _get_unique_values(field=dataset[column3])
    labels = left_labels + mid_labels + right_labels

    offset_left = 0
    offset_mid = len(left_labels)
    offset_right = len(left_labels) + len(mid_labels)

    idx = {}
    for i, name in enumerate(left_labels):
        idx[name] = offset_left + i
    for i, name in enumerate(mid_labels):
        idx[name] = offset_mid + i
    for i, name in enumerate(right_labels):
        idx[name] = offset_right + i

    flows_lm = {}
    flows_mr = {}

    rows = len(dataset["count"])
    for i in range(rows):
        a = dataset[column1][i]
        b = dataset[column2][i]
        c = dataset[column3][i]
        v = dataset["count"][i]

        flows_lm[(a, b)] = flows_lm.get((a, b), 0) + v
        flows_mr[(b, c)] = flows_mr.get((b, c), 0) + v

    source = []
    target = []
    values = []

    for (a, b), v in flows_lm.items():
        source.append(idx[a])
        target.append(idx[b])
        values.append(v)

    for (b, c), v in flows_mr.items():
        source.append(idx[b])
        target.append(idx[c])
        values.append(v)

    fig = go.Figure(
        go.Sankey(
            node=dict(label=labels),
            link=dict(source=source, target=target, value=values),
        )
    )
    fig.update_layout(
        title=title,
        margin=dict(t=80, l=0, r=0, b=0),
        annotations=[
            dict(
                x=0.0,
                y=1.0,
                text=_clean_label(name=column1),
                showarrow=False,
            ),
            dict(
                x=0.5,
                y=1.0,
                text=_clean_label(name=column2),
                showarrow=False,
            ),
            dict(
                x=1.0,
                y=1.0,
                text=_clean_label(name=column3),
                showarrow=False,
            ),
        ],
    )

    fig.show()


def _stack_group_values(dataset, x_axis, y_axis, grp_axis, x_values, grp_values):
    values_stacked = []

    for g in grp_values:
        values = []
        for x in x_values:
            count = 0
            for j in range(len(dataset[y_axis])):
                if dataset[x_axis][j] == x and dataset[grp_axis][j] == g:
                    count = dataset[y_axis][j]
                    break
            values.append(count)
        values_stacked.append(values)

    return values_stacked


def _get_hierarchy_values(dataset, field_parent, field_child, count):
    inner_labels = _get_unique_values(field=dataset[field_parent])
    idx_map = {p: i for i, p in enumerate(inner_labels)}
    inner_values = [0] * len(inner_labels)

    outer_labels = []
    outer_values = []
    outer_parents = []

    for parent, child, value in zip(
        dataset[field_parent], dataset[field_child], dataset[count]
    ):
        inner_values[idx_map[parent]] += value
        outer_labels.append(child)
        outer_values.append(value)
        outer_parents.append(parent)

    return inner_labels, inner_values, outer_labels, outer_values, outer_parents


def _get_unique_values(field):
    labels = []
    seen = set()
    for value in field:
        if value not in seen:
            seen.add(value)
            labels.append(value)
    return labels


def _clean_label(name):
    return str(name).replace("_", " ").strip().title()


def _format_label(labels, decimal=0):
    labels = list(labels)
    i = {"v": -1}

    def fmt(pct):
        i["v"] += 1
        lab = labels[i["v"]] if i["v"] < len(labels) else ""
        return f"{lab}\n{pct:.{decimal}f}%"

    return fmt


def _center_label_percent(inner_radius, outer_radius):
    return (inner_radius + outer_radius) / (2 * outer_radius)


def _compute_label_positions(axis_count, grp_count):
    width = 0.8 / max(1, grp_count)
    axis_pos = np.arange(axis_count)
    tick_pos = axis_pos + width * (grp_count - 1) / 2
    return width, axis_pos, tick_pos


def _apply_bar_orient(orientation):
    if orientation == "v":
        return plt.bar
    if orientation == "h":
        return plt.barh


def _apply_bar_size(orientation, size):
    if orientation == "v":
        return {"width": size}
    if orientation == "h":
        return {"height": size}


def _apply_bar_axes(
    orientation, x_label, y_label, tick_pos=None, tick_labels=None, rotation=45
):
    if orientation == "v":
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        ha = "right" if rotation else "center"
        plt.xticks(tick_pos, tick_labels, rotation=rotation, ha=ha)
    if orientation == "h":
        plt.xlabel(y_label)
        plt.ylabel(x_label)
        plt.yticks(tick_pos, tick_labels)
        plt.gca().invert_yaxis()


def _apply_bar_colors(grp_axis, values):
    colors = {}
    colors_set = COLORS.get(grp_axis, {})

    for value in values:
        colors[value] = colors_set.get(value, None)

    return colors


def _apply_axis_colors(orientation, colors):
    ax = plt.gca()
    if orientation == "v":
        ticks = ax.get_xticklabels()
    if orientation == "h":
        ticks = ax.get_yticklabels()

    for tick in ticks:
        color = colors.get(tick.get_text())
        if color:
            tick.set_color(color)


def _apply_graph_kind(kind, x_pos, values, label_values):
    if kind == "area":
        plt.stackplot(x_pos, *values, labels=label_values)
    if kind == "bar":
        bottoms = np.zeros(len(x_pos))
        for idx, y_values in enumerate(values):
            plt.bar(
                x_pos,
                y_values,
                bottom=bottoms,
                label=label_values[idx],
            )
            bottoms = bottoms + np.array(y_values)
