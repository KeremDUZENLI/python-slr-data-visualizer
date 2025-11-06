import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def plot_bar(
    dataset,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    orientation,
    grp_axis=None,
):
    x_values = dataset[x_axis]
    y_values = dataset[y_axis]
    bar = _orient_bar(orientation)

    if grp_axis:
        groups = _unique(field=dataset[grp_axis])
        for g in groups:
            mask = [v == g for v in dataset[grp_axis]]
            xv = [x for x, m in zip(x_values, mask) if m]
            yv = [y for y, m in zip(y_values, mask) if m]
            bar(xv, yv, label=_clean_label(name=g))
        plt.legend(title=_clean_label(name=grp_axis))
    else:
        bar(x_values, y_values)

    _apply_bar_axes(
        orientation=orientation,
        x_label=x_label,
        y_label=y_label,
        rotation=0,
    )

    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_bar_group(
    dataset,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    orientation,
    grp_axis,
):
    x_values = _unique(field=dataset[x_axis])
    label_values = _unique(field=dataset[grp_axis])
    y_values_stacked = _stack_group_values(
        dataset=dataset,
        x_axis=x_axis,
        y_axis=y_axis,
        grp_axis=grp_axis,
        x_values=x_values,
        grp_values=label_values,
    )
    x_pos, width, tick_pos = _compute_positions(
        x_count=len(x_values),
        grp_count=len(label_values),
    )
    bar = _orient_bar(orientation)

    for i, grp_value in enumerate(label_values):
        x_values_pos = x_pos + i * width
        size = _size_bar(orientation, width)
        bar(
            x_values_pos,
            y_values_stacked[i],
            label=_clean_label(name=grp_value),
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


def plot_stacked(
    dataset,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    kind,
    grp_axis,
):
    x_values = _unique(field=dataset[x_axis])
    label_values = _unique(field=dataset[grp_axis])
    y_values_stacked = _stack_group_values(
        dataset=dataset,
        x_axis=x_axis,
        y_axis=y_axis,
        grp_axis=grp_axis,
        x_values=x_values,
        grp_values=label_values,
    )

    x_pos = np.arange(len(x_values))
    _choose_kind(
        kind=kind, x_pos=x_pos, values=y_values_stacked, label_values=label_values
    )
    _apply_bar_axes(
        orientation="v",
        x_label=x_label,
        y_label=y_label,
        tick_pos=x_pos,
        tick_labels=x_values,
        rotation=0,
    )

    plt.title(title)
    plt.legend(title=_clean_label(name=grp_axis))
    plt.tight_layout()
    plt.show()


def plot_heatmap(
    dataset,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    count_axis,
    grp_axis=None,
):
    x_values = _unique(field=dataset[x_axis])
    y_values = _unique(field=dataset[y_axis])

    r_index = {r: i for i, r in enumerate(y_values)}
    c_index = {c: i for i, c in enumerate(x_values)}
    mat = np.zeros((len(y_values), len(x_values)), dtype=float)

    n = len(dataset[count_axis])
    for i in range(n):
        r_val = dataset[y_axis][i]
        c_val = dataset[x_axis][i]
        v = dataset[count_axis][i]

        r_vals = r_val if isinstance(r_val, list) else [r_val]
        c_vals = c_val if isinstance(c_val, list) else [c_val]

        for rv in r_vals:
            if rv in r_index:
                for cv in c_vals:
                    if cv in c_index:
                        mat[r_index[rv], c_index[cv]] += v

    plt.imshow(mat, aspect="auto")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(np.arange(len(x_values)), x_values, rotation=45, ha="right")
    plt.yticks(np.arange(len(y_values)), y_values)
    plt.colorbar()
    plt.tight_layout()
    plt.show()


def plot_pie(
    dataset,
    field,
    count,
    title,
    decimal=0,
):
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
    plt.tight_layout()
    plt.show()


def plot_pie_group(
    dataset,
    field,
    count,
    grp_axis,
    title,
    decimal=0,
):
    result = _get_hierarchy_values(
        dataset=dataset,
        field_parent=field,
        field_child=grp_axis,
        count=count,
    )
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
    plt.tight_layout()
    plt.show()


def plot_sunburst(
    dataset,
    field,
    count,
    grp_axis,
    title,
    decimal=0,
):
    result = _get_hierarchy_values(
        dataset=dataset,
        field_parent=field,
        field_child=grp_axis,
        count=count,
    )
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


def plot_sankey(
    dataset,
    column1,
    column2,
    column3,
    title,
):
    left_labels = _unique(field=dataset[column1])
    mid_labels = _unique(field=dataset[column2])
    right_labels = _unique(field=dataset[column3])
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


def _unique(field):
    out = []
    seen = set()
    for value in field:
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def _clean_label(name):
    return str(name).replace("_", " ").strip().title()


def _autolabels(labels, decimal=0):
    labels = list(labels)
    i = {"v": -1}

    def fmt(pct):
        i["v"] += 1
        lab = labels[i["v"]] if i["v"] < len(labels) else ""
        return f"{lab}\n{pct:.{decimal}f}%"

    return fmt


def _center_pctdistance(inner_radius, outer_radius):
    return (inner_radius + outer_radius) / (2 * outer_radius)


def _compute_positions(x_count, grp_count):
    width = 0.8 / max(1, grp_count)
    x_pos = np.arange(x_count)
    tick_pos = x_pos + width * (grp_count - 1) / 2
    return x_pos, width, tick_pos


def _get_group_values(dataset, x_axis, y_axis, grp_axis, x_values, grp_value):
    values = []
    for x in x_values:
        count = 0
        for j in range(len(dataset[y_axis])):
            if dataset[x_axis][j] == x and dataset[grp_axis][j] == grp_value:
                count = dataset[y_axis][j]
                break
        values.append(count)

    return values


def _stack_group_values(dataset, x_axis, y_axis, grp_axis, x_values, grp_values):
    values_stacked = []
    for g in grp_values:
        y_values = _get_group_values(
            dataset=dataset,
            x_axis=x_axis,
            y_axis=y_axis,
            grp_axis=grp_axis,
            x_values=x_values,
            grp_value=g,
        )
        values_stacked.append(y_values)
    return values_stacked


def _get_hierarchy_values(dataset, field_parent, field_child, count):
    inner_labels = _unique(field=dataset[field_parent])
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


def _orient_bar(orientation):
    if orientation == "v":
        return plt.bar
    if orientation == "h":
        return plt.barh


def _size_bar(orientation, size):
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
        plt.xticks(tick_pos, tick_labels, rotation=rotation, ha="center")
    if orientation == "h":
        plt.xlabel(y_label)
        plt.ylabel(x_label)
        plt.yticks(tick_pos, tick_labels)
        plt.gca().invert_yaxis()


def _choose_kind(kind, x_pos, values, label_values):
    if kind == "area":
        plt.stackplot(x_pos, *values, labels=label_values)
    if kind == "bar":
        bottoms = np.zeros(len(x_pos))
        for idx, yvals in enumerate(values):
            plt.bar(
                x_pos,
                yvals,
                bottom=bottoms,
                label=_clean_label(name=label_values[idx]),
            )
            bottoms = bottoms + np.array(yvals)
