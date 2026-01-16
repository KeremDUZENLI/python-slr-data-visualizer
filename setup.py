from config.config import (
    COLORS,
    FONTS_PLOT,
    FONTS_LEGEND,
)

from helper.helper import (
    calculate_labels_center_bar,
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

from output._1_print import (
    print_dict,
    print_counts,
)
from output._2_plots import (
    draw_plot,
    show_plot,
    save_plot,
)

from plot_get._1_get_labels import (
    get_labels,
)
from plot_get._2_get_colors import (
    get_colors_map,
    map_colors_map,
)
from plot_get._3_get_legend import (
    get_legend_handles,
)

from plot_style._0_draw import (
    draw_bar_1D,
    draw_bar_2D,
    draw_pie,
)
from plot_style._1_labels import (
    labels_bar_numbers,
    labels_grid,
    labels_extra,
)
from plot_style._2_color import (
    color_bars,
    color_slices,
    color_labels,
    color_labels_pie,
    color_labels_extra,
)
from plot_style._3_legend import (
    create_legend,
)
from plot_style._4_font import (
    apply_font_plot,
    apply_font_legend,
)
from plot_style._5_text import (
    update_text_labels,
    update_text_legend,
)


################################################
#################### bar_1D ####################
################################################


def _1_0(dataset):
    ### operation
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

    ### output
    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values = get_labels(
        dataset=dataset_counted,
        x_axis="year",
        y_axis="count",
        z_axis=None,
    )

    colors_map = get_colors_map(
        values=x_values,
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

    ### plot_style
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
    labels_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bars(
        ax=ax,
        coloring_values_list=x_values_list,
        colors_map=colors_map,
        border=False,
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

    update_text_legend(legend1)
    update_text_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_1_0",
        legends=[legend1, legend2],
        extra_artists=None,
    )


def _4_1(dataset):
    ### operation
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

    ### output
    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="software",
        y_axis="count",
        z_axis="software_category",
    )
    labels_center = calculate_labels_center_bar(
        values=z_values,
    )

    colors_map = get_colors_map(
        values=z_values,
        colors=COLORS,
        color_field="software_category",
    )
    colors_mapped = map_colors_map(
        values_new=x_values,
        values_old=z_values,
        colors_map=colors_map,
    )

    handles1 = get_legend_handles(
        values=z_values,
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

    ### plot_style
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
    labels_grid(
        ax=ax,
        orientation=orientation,
    )
    texts = labels_extra(
        ax=ax,
        labels_center=labels_center,
        orientation=orientation,
        offset=15,
    )

    color_bars(
        ax=ax,
        coloring_values_list=x_values_list,
        colors_map=colors_mapped,
        border=True,
    )
    color_labels(
        ax=ax,
        colors_map=colors_mapped,
        orientation=orientation,
    )
    color_labels_extra(
        ax=texts,
        colors_map=colors_map,
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

    update_text_labels(texts)
    update_text_legend(legend1)
    update_text_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_4_1",
        legends=[legend1, legend2],
        extra_artists=texts,
    )


def _5_0(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["country"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["country"],
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

    ### output
    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values = get_labels(
        dataset=dataset_counted,
        x_axis="country",
        y_axis="count",
        z_axis=None,
    )

    colors_map = get_colors_map(
        values=x_values,
        colors=COLORS,
        color_field="country",
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

    ### plot_style
    orientation = "v"
    x_values_list = draw_bar_1D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec={
            "x_label": "Continents",
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
        coloring_values_list=x_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = create_legend(
        ax=ax,
        handles=handles1,
        title="Continents",
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

    update_text_legend(legend1)
    update_text_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_5_0",
        legends=[legend1, legend2],
        extra_artists=None,
    )


################################################
#################### bar_2D ####################
################################################


def _1_1(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["year", "historical_site_type"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["year", "historical_site_type"],
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

    ### output
    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="year",
        y_axis="count",
        z_axis="historical_site_type",
    )

    colors_map = get_colors_map(
        values=z_values,
        colors=COLORS,
        color_field="historical_site_type",
    )

    handles1 = get_legend_handles(
        values=z_values,
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

    ### plot_style
    orientation = "v"
    z_values_list = draw_bar_2D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Year",
            "y_label": "Number of Studies",
            "title": "Number of Studies by Historical Site Type",
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
    labels_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bars(
        ax=ax,
        coloring_values_list=z_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = create_legend(
        ax=ax,
        handles=handles1,
        title="Historical Site Type",
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

    update_text_legend(legend1)
    update_text_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_1_1",
        legends=[legend1, legend2],
        extra_artists=None,
    )


def _2_1(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["platform", "device"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["platform", "device"],
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

    ### output
    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="platform",
        y_axis="count",
        z_axis="device",
    )

    colors_map = get_colors_map(
        values=z_values,
        colors=COLORS,
        color_field="device",
    )

    handles1 = get_legend_handles(
        values=z_values,
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

    ### plot_style
    orientation = "v"
    z_values_list = draw_bar_2D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Platform",
            "y_label": "Number of Studies",
            "title": "Distribution of Devices Across Platforms",
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
    labels_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bars(
        ax=ax,
        coloring_values_list=z_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = create_legend(
        ax=ax,
        handles=handles1,
        title="Device",
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

    update_text_legend(legend1)
    update_text_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_2_1",
        legends=[legend1, legend2],
        extra_artists=None,
    )


def _3_4(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["technique", "study_focus"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["technique", "study_focus"],
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

    ### output
    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="technique",
        y_axis="count",
        z_axis="study_focus",
    )

    colors_map = get_colors_map(
        values=z_values,
        colors=COLORS,
        color_field="study_focus",
    )

    handles1 = get_legend_handles(
        values=z_values,
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

    ### plot_style
    orientation = "v"
    z_values_list = draw_bar_2D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Technique",
            "y_label": "Number of Studies",
            "title": "Techniques Used in Study Focus",
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
    labels_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bars(
        ax=ax,
        coloring_values_list=z_values_list,
        colors_map=colors_map,
        border=False,
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

    update_text_legend(legend1)
    update_text_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_3_4",
        legends=[legend1, legend2],
        extra_artists=None,
    )


#############################################
#################### pie ####################
#############################################


def _1_3(dataset):
    ### operation
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

    ### output
    print_dict(dataset_counted)
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values = get_labels(
        dataset=dataset_counted,
        x_axis="study_focus",
        y_axis="count",
        z_axis=None,
    )

    colors_map = get_colors_map(
        values=x_values,
        colors=COLORS,
        color_field="study_focus",
    )

    ### plot_style
    x_values_list = draw_pie(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec={
            "title": "Study Focus Distribution",
        },
    )

    color_slices(
        ax=ax,
        coloring_values_list=x_values_list,
        colors_map=colors_map,
        border=True,
    )
    color_labels_pie(
        ax=ax,
        color="white",
    )

    apply_font_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_1_3",
        legends=None,
        extra_artists=None,
    )
