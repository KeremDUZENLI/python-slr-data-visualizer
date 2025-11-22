from config.config import (
    COLORS,
    FONTS_PLOT,
    FONTS_LEGEND,
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
    get_labels_extra,
)
from plot._2_get_colors import (
    get_colors_map,
)
from plot._3_get_legend import (
    get_legend_handles,
)

from plot_style._0_draw import (
    draw_bar_1D,
)
from plot_style._1_labels import (
    labels_bar_numbers,
    labels_extra,
)
from plot_style._2_color import (
    color_bars,
    color_labels,
    color_labels_extra,
)
from plot_style._3_legend import (
    create_legend,
)
from plot_style._4_font import (
    apply_font_plot,
    apply_font_legend,
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
    handles1 = get_legend_handles(
        values=x_values,
        colors_map=colors_map,
    )
    handles2 = get_legend_handles(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#FF5733",
            "Custom B": "#33FF57",
            "Custom C": "#3357FF",
            "Custom D": "#46A819",
            "Custom E": "#FF33A1",
        },
    )

    fig, ax = plt.subplots(figsize=(8, 6))

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

    labels_bar_numbers(
        ax=ax,
        y_values=y_values,
        orientation=orientation,
        offset=1,
    )

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

    legend1 = create_legend(
        ax=ax,
        handles=handles1,
        title="Year",
        loc="upper left",
    )
    legend2 = create_legend(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    apply_font_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    apply_font_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    apply_font_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    plt.tight_layout()
    plt.show()
    fig.savefig(
        "figure/_0_0.png",
        dpi=300,
        bbox_inches="tight",
        bbox_extra_artists=[legend1, legend2],
    )


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
    handles1 = get_legend_handles(
        values=x_values,
        colors_map=colors_map,
    )
    handles2 = get_legend_handles(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#FF5733",
            "Custom B": "#33FF57",
            "Custom C": "#3357FF",
            "Custom D": "#46A819",
            "Custom E": "#FF33A1",
        },
    )

    fig, ax = plt.subplots(figsize=(8, 6))

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

    labels_bar_numbers(
        ax=ax,
        y_values=y_values,
        orientation=orientation,
        offset=1,
    )

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

    legend1 = create_legend(
        ax=ax,
        handles=handles1,
        title="Study Focus",
        loc="upper left",
    )
    legend2 = create_legend(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    apply_font_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    apply_font_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    apply_font_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    plt.tight_layout()
    plt.show()
    fig.savefig(
        "figure/_1_3.png",
        dpi=300,
        bbox_inches="tight",
        bbox_extra_artists=[legend1, legend2],
    )


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
    values_centers = get_labels_extra(
        values=z_values,
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
    handles1 = get_legend_handles(
        values=z_values,
        colors_map=colors_map_legend,
    )
    handles2 = get_legend_handles(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#FF5733",
            "Custom B": "#33FF57",
            "Custom C": "#3357FF",
            "Custom D": "#46A819",
            "Custom E": "#FF33A1",
        },
    )

    fig, ax = plt.subplots(figsize=(8, 6))

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

    labels_bar_numbers(
        ax=ax,
        y_values=y_values,
        orientation=orientation,
        offset=3,
    )
    texts = labels_extra(
        ax=ax,
        values_centers=values_centers,
        orientation=orientation,
        offset=15,
    )

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

    colors_map_labels_extra = get_colors_map(
        values=[t.get_text() for t in texts],
        criteria=[t.get_text() for t in texts],
        colors=COLORS,
        color_field="labels_extra",
    )
    color_labels_extra(
        ax=texts,
        colors_map=colors_map_labels_extra,
    )

    legend1 = create_legend(
        ax=ax,
        handles=handles1,
        title="Software Category",
        loc="upper left",
    )
    legend2 = create_legend(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    apply_font_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    apply_font_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    apply_font_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    plt.tight_layout()
    plt.show()
    fig.savefig(
        "figure/_4_1.png",
        dpi=300,
        bbox_inches="tight",
        bbox_extra_artists=texts + [legend1, legend2],
    )
