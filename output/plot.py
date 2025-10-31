import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def plot_bar(dataset, x_axis, y_axis, x_label, y_label, title):
    x_values = dataset[x_axis]
    y_values = dataset[y_axis]

    plt.bar(x_values, y_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def plot_bar_group(dataset, x_axis, y_axis, grp_axis, x_label, y_label, title):
    x_values = _unique(dataset[x_axis])
    grp_values = _unique(dataset[grp_axis])

    x_pos, width, tick_pos = _compute_positions(len(x_values), len(grp_values))

    for i, grp_value in enumerate(grp_values):
        y_values = _get_group_values(
            dataset, x_axis, y_axis, grp_axis, x_values, grp_value
        )
        plt.bar(x_pos + i * width, y_values, width, label=grp_value)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(tick_pos, x_values)
    plt.legend(title=grp_axis)
    plt.show()


def plot_stacked(dataset, x_axis, y_axis, grp_axis, x_label, y_label, title):
    x_values = _unique(dataset[x_axis])
    grp_values = _unique(dataset[grp_axis])

    series = []
    for grp_value in grp_values:
        y_values = _get_group_values(
            dataset, x_axis, y_axis, grp_axis, x_values, grp_value
        )
        series.append(y_values)

    x_pos = np.arange(len(x_values))
    plt.stackplot(x_pos, *series, labels=grp_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(x_pos, x_values)
    plt.legend(title=grp_axis)
    plt.show()


def plot_pie(dataset, field, count, title, decimal=0):
    inner_labels = dataset[field]
    inner_values = dataset[count]

    labels = _autolabels(labels=inner_labels, decimal=decimal)
    pct = _center_pctdistance(inner_radius=0.0, outer_radius=1.0)

    plt.pie(
        inner_values,
        autopct=labels,
        startangle=90,
        radius=1.0,
        pctdistance=pct,
    )
    plt.title(title)
    plt.axis("equal")
    plt.show()


def plot_pie_group(dataset, field, count, grp_axis, title, decimal=0):
    result = _get_hierarchy_values(dataset, field, grp_axis, count)
    inner_labels, inner_values, outer_labels, outer_values, outer_parents = result

    labels_outer = _autolabels(labels=outer_labels, decimal=decimal)
    labels_inner = _autolabels(labels=inner_labels, decimal=decimal)
    pct_outer = _center_pctdistance(inner_radius=0.5, outer_radius=1.0)
    pct_inner = _center_pctdistance(inner_radius=0.0, outer_radius=0.5)

    plt.pie(
        outer_values,
        autopct=labels_outer,
        startangle=90,
        radius=1.0,
        pctdistance=pct_outer,
    )
    plt.pie(
        inner_values,
        autopct=labels_inner,
        startangle=90,
        radius=0.5,
        pctdistance=pct_inner,
    )
    plt.title(title)
    plt.axis("equal")
    plt.show()


def plot_sunburst(dataset, field, count, grp_axis, title, decimal=0):
    result = _get_hierarchy_values(dataset, field, grp_axis, count)
    inner_labels, inner_values, outer_labels, outer_values, outer_parents = result

    labels = inner_labels + outer_labels
    parents = [""] * len(inner_labels) + outer_parents
    values = inner_values + outer_values
    fmt = f"%{{label}}<br>%{{percentRoot:.{decimal}%}}"

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
    fig.update_layout(title=title, margin=dict(t=60, l=0, r=0, b=0))
    fig.show()


def plot_sankey(dataset, column1, column2, column3, title):
    left_labels = _unique(dataset[column1])
    mid_labels = _unique(dataset[column2])
    right_labels = _unique(dataset[column3])
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

    src = []
    tgt = []
    val = []

    for (a, b), v in flows_lm.items():
        src.append(idx[a])
        tgt.append(idx[b])
        val.append(v)

    for (b, c), v in flows_mr.items():
        src.append(idx[b])
        tgt.append(idx[c])
        val.append(v)

    fig = go.Figure(
        go.Sankey(
            node=dict(label=labels),
            link=dict(source=src, target=tgt, value=val),
        )
    )
    fig.update_layout(
        title=title,
        margin=dict(t=80, l=0, r=0, b=0),
        annotations=[
            dict(
                x=0.0,
                y=1.0,
                text=_clean_label(column1),
                showarrow=False,
            ),
            dict(
                x=0.5,
                y=1.0,
                text=_clean_label(column2),
                showarrow=False,
            ),
            dict(
                x=1.0,
                y=1.0,
                text=_clean_label(column3),
                showarrow=False,
            ),
        ],
    )

    fig.show()


def _unique(field):
    out = []
    seen = set()
    for value in field:
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def _clean_label(name):
    return str(name).replace("_", " ").strip().upper()


def _autolabels(labels, decimal=0):
    it = iter(labels)
    return lambda pct: f"{next(it, '')}\n{pct:.{decimal}f}%"


def _center_pctdistance(inner_radius, outer_radius):
    return (inner_radius + outer_radius) / (2 * outer_radius)


def _compute_positions(x_count, grp_count):
    width = 0.8 / max(1, grp_count)
    x_pos = np.arange(x_count)
    tick_pos = x_pos + width * (grp_count - 1) / 2
    return x_pos, width, tick_pos


def _get_group_values(dataset, x_axis, y_axis, group_axis, x_values, grp_value):
    y_values = []
    for x in x_values:
        count = 0
        for j in range(len(dataset[y_axis])):
            if dataset[x_axis][j] == x and dataset[group_axis][j] == grp_value:
                count = dataset[y_axis][j]
                break
        y_values.append(count)
    return y_values


def _get_hierarchy_values(dataset, field_parent, field_child, count):
    inner_labels = _unique(dataset[field_parent])
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
