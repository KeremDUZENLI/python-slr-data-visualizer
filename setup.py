from config.config import (
    COLORS,
    font_label_numbers,
)
from helper.helper import (
    parse_string,
)
from operation._1_filter import (
    filter_dataset_by_fields,
    filter_dataset_by_values,
    filter_dataset_by_count,
)
from operation._2_count import (
    count_dataset,
)
from plot._1_get_labels import (
    get_labels,
)
from plot._2_get_charts import (
    draw_bar_1D,
)
from plot._3_get_colors import (
    get_colors_map,
)
from plot_style._1_colorize import (
    color_bars,
    color_labels,
)
from plot_style._2_labelize import (
    label_numbers,
)
from plot_style._3_legend import (
    create_legend,
)
from print.print import (
    print_dict,
    print_counts,
)
import matplotlib.pyplot as plt


def _0_0(dataset):
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["year"],
    )

    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["year"],
    )

    filter_values = None
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted = filter_dataset_by_values(
                dataset=dataset_counted,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = None
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted = filter_dataset_by_count(
            dataset=dataset_counted,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)

    x_values, y_values = get_labels(
        dataset=dataset_counted,
        x_axis="year",
        y_axis="count",
        z_axis=None,
    )

    colors_map = get_colors_map(
        values=x_values,
        criteria=x_values,
        colors=COLORS,
        color_field="year",
    )

    fig, ax = plt.subplots()

    orientation = "v"
    x_values_list = draw_bar_1D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec={
            "x_label": "Year",
            "y_label": "Number of Studies",
            "title": "Studies Per Year",
            "rotation": 45,
        },
        orientation=orientation,
    )

    handles = create_legend(
        values=x_values,
        colors_map=colors_map,
    )
    legend = ax.legend(
        handles=handles,
        title="Year",
        loc="upper right",
    )
    ax.add_artist(legend)

    handles_ext = create_legend(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#FF5733",
            "Custom B": "#33FF57",
            "Custom C": "#3357FF",
        },
    )
    legend_ext = ax.legend(
        handles=handles_ext,
        title="Custom Legend",
        loc="lower right",
    )
    ax.add_artist(legend_ext)

    color_bars(
        ax=ax,
        x_values_list=x_values_list,
        colors_map=colors_map,
    )
    color_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    plt.tight_layout()
    plt.show()
    fig.savefig("figure/_0_0.png", dpi=300)


def _1_3(dataset):
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["study_focus"],
    )

    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["study_focus"],
    )

    filter_values = None
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted = filter_dataset_by_values(
                dataset=dataset_counted,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = None
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted = filter_dataset_by_count(
            dataset=dataset_counted,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)

    x_values, y_values = get_labels(
        dataset=dataset_counted,
        x_axis="study_focus",
        y_axis="count",
        z_axis=None,
    )

    colors_map = get_colors_map(
        values=x_values,
        criteria=x_values,
        colors=COLORS,
        color_field="study_focus",
    )

    fig, ax = plt.subplots()

    orientation = "v"
    x_values_list = draw_bar_1D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec={
            "x_label": "Study Focus",
            "y_label": "Number of Studies",
            "title": "Studies Per Year",
            "rotation": 45,
        },
        orientation=orientation,
    )

    handles = create_legend(
        values=x_values,
        colors_map=colors_map,
    )
    legend = ax.legend(
        handles=handles,
        title="Study Focus",
        loc="upper right",
    )
    ax.add_artist(legend)

    handles_ext = create_legend(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#FF5733",
            "Custom B": "#33FF57",
            "Custom C": "#3357FF",
        },
    )
    legend_ext = ax.legend(
        handles=handles_ext,
        title="Custom Legend",
        loc="lower right",
    )
    ax.add_artist(legend_ext)

    color_bars(
        ax=ax,
        x_values_list=x_values_list,
        colors_map=colors_map,
    )
    color_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    plt.tight_layout()
    plt.show()
    fig.savefig("figure/_1_3.png", dpi=300)


def _4_1(dataset):
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["software_category", "software", "technique"],
    )

    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["software_category", "software"],
    )

    filter_values = ["software != "]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted = filter_dataset_by_values(
                dataset=dataset_counted,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = "count >= 5"
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted = filter_dataset_by_count(
            dataset=dataset_counted,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)

    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="software",
        y_axis="count",
        z_axis="software_category",
    )

    colors_map = get_colors_map(
        values=x_values,
        criteria=z_values,
        colors=COLORS,
        color_field="software_category",
    )
    colors_map_legend = get_colors_map(
        values=z_values,
        criteria=z_values,
        colors=COLORS,
        color_field="software_category",
    )

    fig, ax = plt.subplots()

    orientation = "h"
    x_values_list = draw_bar_1D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec={
            "x_label": "",
            "y_label": "",
            "title": "Software Usage by Category",
            "rotation": 45,
        },
        orientation=orientation,
    )

    handles = create_legend(
        values=z_values,
        colors_map=colors_map_legend,
    )
    legend = ax.legend(
        handles=handles,
        title="Software Category",
        loc="upper right",
    )
    ax.add_artist(legend)

    handles_ext = create_legend(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#FF5733",
            "Custom B": "#33FF57",
            "Custom C": "#3357FF",
            "Custom D": "#46A819",
            "Custom E": "#FF33A1",
        },
    )
    legend_ext = ax.legend(
        handles=handles_ext,
        title="Custom Legend",
        loc="lower right",
    )
    ax.add_artist(legend_ext)

    color_bars(
        ax=ax,
        x_values_list=x_values_list,
        colors_map=colors_map,
    )
    color_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )
    label_numbers(
        ax=ax,
        y_values=y_values,
        orientation=orientation,
        offset=3,
        font=font_label_numbers,
    )

    plt.tight_layout()
    plt.show()
    fig.savefig("figure/_4_1.png", dpi=300)
