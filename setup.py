from output.plot import (
    plot_bar,
    plot_bar_group,
    plot_stacked,
    plot_heatmap,
    plot_pie,
    plot_pie_group,
    plot_sunburst,
    plot_sankey,
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
    filter_value=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_value=filter_value,
        filter_count=filter_count,
    )
    print_counts(
        dataset=dict_prepared,
        decimal=0,
    )
    plot_bar(
        dataset=dict_prepared,
        x_axis=x_axis,
        y_axis=y_axis,
        x_label=x_label,
        y_label=y_label,
        title=title,
        orientation=orientation,
        grp_axis=grp_axis,
    )


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
    filter_value=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_value=filter_value,
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
    filter_value=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_value=filter_value,
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
    filter_value=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_value=filter_value,
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
    filter_value=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_value=filter_value,
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
    filter_value=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_value=filter_value,
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
    filter_value=None,
    filter_count=None,
):
    dict_prepared = _prepare_dict(
        dataset=dataset,
        fields=fields,
        filter_value=filter_value,
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
    filter_value=None,
    filter_count=None,
):
    if filter_value:
        field, operation, values = _parse_string(text=filter_value)
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
    values = [v.strip() for v in right.split(",")]

    if len(values) == 1 and values[0] == "":
        values = [""]

    if found_op == "==":
        operation = True
    elif found_op == "!=":
        operation = False
    else:
        operation = found_op

    return field, operation, values
