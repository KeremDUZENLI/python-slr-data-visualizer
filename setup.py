from output.plot import (
    plot_bar,
    plot_bar_group,
    plot_stacked,
    plot_heatmap,
    plot_pie,
    plot_pie_group,
    plot_sunburst,
    plot_sankey,
    _clean_label,
)
from output.print import (
    print_counts,
)
from src.tools import (
    filter_dataset_by_value,
    filter_dataset_by_count,
    count_dataset,
)


def chart_bar(
    dataset,
    fields,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    orientation,
    grp_axis=None,
    filter_values=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_values=filter_values,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=0,
    )
    values = plot_bar(
        dataset=dict_prepared,
        x_axis=x_axis,
        y_axis=y_axis,
        x_label=x_label,
        y_label=y_label,
        title=title,
        orientation=orientation,
        grp_axis=grp_axis,
    )

    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    from output.plot import COLORS, _get_unique_values

    handles_series = [
        Patch(
            facecolor=COLORS[grp_axis].get(value, ""),
            edgecolor="none",
            label=_clean_label(value),
        )
        for value in values
    ]
    legend = plt.legend(
        handles=handles_series,
        title=_clean_label(grp_axis),
        loc="lower right",
        bbox_to_anchor=(1, 0),
    )
    plt.gca().add_artist(legend)

    field = "software_category"
    values = _get_unique_values(field=dict_prepared[field])

    handles_cats = [
        Patch(
            facecolor=COLORS[field].get(value, ""),
            edgecolor="none",
            label=_clean_label(value),
        )
        for value in values
    ]
    legend_ext = plt.legend(
        handles=handles_cats,
        title=_clean_label(field),
        loc="upper right",
        bbox_to_anchor=(1, 1),
    )
    plt.gca().add_artist(legend_ext)

    plt.show()


def chart_bar_group(
    dataset,
    fields,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    orientation,
    grp_axis,
    filter_values=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_values=filter_values,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=0,
    )
    plot_bar_group(
        dataset=dict_prepared,
        x_axis=x_axis,
        y_axis=y_axis,
        x_label=x_label,
        y_label=y_label,
        title=title,
        orientation=orientation,
        grp_axis=grp_axis,
    )


def chart_stacked(
    dataset,
    fields,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    kind,
    grp_axis,
    filter_values=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_values=filter_values,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=1,
    )
    plot_stacked(
        dataset=dict_prepared,
        x_axis=x_axis,
        y_axis=y_axis,
        x_label=x_label,
        y_label=y_label,
        title=title,
        kind=kind,
        grp_axis=grp_axis,
    )


def chart_heatmap(
    dataset,
    fields,
    x_axis,
    y_axis,
    x_label,
    y_label,
    title,
    count_axis,
    grp_axis,
    filter_values=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_values=filter_values,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=1,
    )
    plot_heatmap(
        dataset=dict_prepared,
        x_axis=x_axis,
        y_axis=y_axis,
        x_label=x_label,
        y_label=y_label,
        title=title,
        count_axis=count_axis,
        grp_axis=grp_axis,
    )


def chart_pie(
    dataset,
    fields,
    count,
    title,
    filter_values=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_values=filter_values,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=1,
    )
    plot_pie(
        dataset=dict_prepared,
        field=fields[0],
        count=count,
        title=title,
    )


def chart_pie_group(
    dataset,
    fields,
    count,
    title,
    grp_axis,
    filter_values=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_values=filter_values,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=1,
    )
    plot_pie_group(
        dataset=dict_prepared,
        field=fields[0],
        count=count,
        title=title,
        grp_axis=grp_axis,
    )


def chart_sunburst(
    dataset,
    fields,
    count,
    title,
    grp_axis,
    filter_values=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_values=filter_values,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=1,
    )
    plot_sunburst(
        dataset=dict_prepared,
        field=fields[0],
        count=count,
        title=title,
        grp_axis=grp_axis,
    )


def chart_sankey(
    dataset,
    fields,
    title,
    column1,
    column2,
    column3,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=1,
    )
    plot_sankey(
        dataset=dict_prepared,
        title=title,
        column1=column1,
        column2=column2,
        column3=column3,
    )


def _prepare_dict(
    dataset,
    fields,
    filter_values=None,
    filter_count=None,
):
    if filter_values:
        for fv in filter_values:
            field, operation, values = _parse_string(text=fv)
            dataset = filter_dataset_by_value(
                dataset=dataset,
                field=field,
                values=values,
                include=operation,
            )

    dataset_prepared = count_dataset(
        dataset=dataset,
        fields=fields,
    )

    if filter_count:
        field, operation, values = _parse_string(text=filter_count)
        dataset_prepared = filter_dataset_by_count(
            dataset=dataset_prepared,
            field=field,
            value=int(values[0]),
            comparison=operation,
        )

    return dataset_prepared


def _parse_string(text):
    operators = ["==", "!=", ">=", ">", "<=", "<", "="]
    found_op = None

    for operation in operators:
        if operation in text:
            found_op = operation
            break

    left, right = text.split(found_op, 1)
    field = left.strip()
    right = right.strip()
    values_raw = [v.strip() for v in right.split(",")]

    values = []
    for v in values_raw:
        if v in ("''", '""'):
            values.append("")
        else:
            values.append(v)

    if len(values) == 1 and values[0] == "":
        values = [""]

    if found_op == "==":
        operation = True
    elif found_op == "!=":
        operation = False
    else:
        operation = found_op

    return field, operation, values
