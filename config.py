from input._1_read import (
    read_dataset,
)
from input._2_filter import (
    filter_dataset_by_fields,
    filter_dataset_by_values,
    filter_dataset_by_count,
)
from input._3_count import (
    count_dataset,
)
from input._4_tools import (
    group_dataset_by_fields,
)
from output._1_print import (
    print_simple,
    print_counts,
)
from output._2_plot_prep import (
    prepare_data_1D,
    get_colors_map,
)
from output._3_plot_ax import (
    draw_bar_1D,
    color_bars,
    color_labels,
    create_legend,
)
from tools.parse import (
    parse_string,
)
import matplotlib.pyplot as plt


DATASET = read_dataset(csv_path="data/dataset.csv")


def chart_bar_1D(
    fields,
    x_axis,
    y_axis,
    labels_spec,
    orientation,
    color_field,
    color_axis,
    labels_legend,
    filter_values=None,
    filter_count=None,
    save_path=None,
):
    dataset_filtered = filter_dataset_by_fields(
        dataset=DATASET,
        fields=fields,
    )

    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=fields,
    )

    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted = filter_dataset_by_values(
                dataset=dataset_counted,
                field=field,
                values=values,
                include=operation,
            )

    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted = filter_dataset_by_count(
            dataset=dataset_counted,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    print_simple(dataset_counted)
    print_counts(dataset_counted, decimal=1)

    x_values, y_values = prepare_data_1D(
        dataset=dataset_counted,
        x_axis=x_axis,
        y_axis=y_axis,
    )

    colors = get_colors_map(
        field=color_field,
        values=x_values,
    )

    fig, ax = plt.subplots()

    x_values_list = draw_bar_1D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec=labels_spec,
        orientation=orientation,
    )

    color_bars(
        ax=ax,
        colors_map=colors,
        x_values_list=x_values_list,
    )

    color_labels(
        ax=ax,
        colors_map=colors,
        axis=color_axis,
    )

    create_legend(
        ax=ax,
        colors_map=colors,
        values=x_values,
        title=labels_legend.get("title", ""),
        loc=labels_legend.get("loc", "best"),
    )

    plt.tight_layout()
    plt.show()
    fig.savefig(save_path, dpi=300)
