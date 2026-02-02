from config.config import (
    COLORS,
    FONTS_PLOT,
    FONTS_LEGEND,
    STYLE_PRISMA,
)

from helper.helper import (
    add_dataset_id,
    correct_values,
    calculate_labels_nested,
    calculate_sankey_flows,
    calculate_labels_pos_bar,
    parse_string,
)

from operation._1_filter import (
    filter_dataset_by_fields,
    filter_dataset_by_values,
    filter_dataset_by_count,
)
from operation._2_count import (
    count_dataset,
    get_unique_count,
)

from output._1_print import (
    print_dict,
    print_counts,
)
from output._2_plots import (
    draw_plot,
    show_plot,
    save_plot,
    draw_plot_plotly,
    show_plot_plotly,
    draw_plot_graphviz,
    show_plot_graphviz,
    save_plot_graphviz,
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
    get_legend_handles_bubble,
)

from plot_style._0_draw import (
    draw_bar_1D,
    draw_bar_2D,
    draw_stacked,
    draw_pie,
    draw_pie_nested,
    draw_heatmap,
    draw_scatter,
    draw_sunburst,
    draw_sankey,
    draw_map,
    draw_prisma_nodes,
    draw_prisma_edges,
)
from plot_style._1_number import (
    number_bar,
    number_area,
    number_heatmap,
    add_labels_extra,
    add_grid,
    style_prisma,
)
from plot_style._2_color import (
    color_bar,
    color_area,
    color_pie,
    color_heatmap,
    color_scatter,
    color_sunburst,
    color_sankey_nodes,
    color_sankey_links,
    color_map,
    color_bar_labels,
    color_pie_labels,
    color_heatmap_labels,
    color_sunburst_labels,
    color_sankey_labels,
    color_map_labels,
    color_labels_extra,
)
from plot_style._3_legend import (
    legend_create,
    legend_create_colorbar,
    legend_create_mapbar,
)
from plot_style._4_font import (
    font_apply_plot,
    font_apply_legend,
)
from plot_style._5_text import (
    text_clean_labels,
    text_clean_legend,
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
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
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

    number_bar(
        ax=ax,
        orientation=orientation,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bar(
        ax=ax,
        coloring_values=x_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Year",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1)
    text_clean_legend(legend2)

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
        fields=["software_category", "software"],
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

    ## plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="software",
        y_axis="count",
        z_axis="software_category",
    )
    labels_center = calculate_labels_pos_bar(
        values=z_values,
        distance=5,
    )

    colors_map = get_colors_map(
        colors=COLORS,
        color_field="software_category",
    )
    colors_mapped = map_colors_map(
        colors_from=x_values,
        colors_to=z_values,
        colors_map=colors_map,
    )

    handles1 = get_legend_handles(
        values=z_values,
        colors_map=colors_map,
    )
    handles2 = get_legend_handles(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
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

    number_bar(
        ax=ax,
        orientation=orientation,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )
    texts = add_labels_extra(
        ax=ax,
        labels_center=labels_center,
        orientation=orientation,
        offset=15,
    )

    color_bar(
        ax=ax,
        coloring_values=x_values_list,
        colors_map=colors_mapped,
        border=True,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_mapped,
        orientation=orientation,
    )
    color_labels_extra(
        ax=texts,
        colors_map=colors_map,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Software Category",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_labels(texts)
    text_clean_legend(legend1)
    text_clean_legend(legend2)

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
        fields=["continent"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["continent"],
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
        x_axis="continent",
        y_axis="count",
        z_axis=None,
    )

    colors_map = get_colors_map(
        values=x_values,
        colors=COLORS,
        color_field="continent",
    )

    handles1 = get_legend_handles(
        values=x_values,
        colors_map=colors_map,
    )
    handles2 = get_legend_handles(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
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

    number_bar(
        ax=ax,
        orientation=orientation,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bar(
        ax=ax,
        coloring_values=x_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Continents",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1)
    text_clean_legend(legend2)

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
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
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

    number_bar(
        ax=ax,
        orientation=orientation,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bar(
        ax=ax,
        coloring_values=z_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Historical Site Type",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1)
    text_clean_legend(legend2)

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
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
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

    number_bar(
        ax=ax,
        orientation=orientation,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bar(
        ax=ax,
        coloring_values=z_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Device",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1)
    text_clean_legend(legend2)

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
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
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

    number_bar(
        ax=ax,
        orientation=orientation,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bar(
        ax=ax,
        coloring_values=z_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Study Focus",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1)
    text_clean_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_3_4",
        legends=[legend1, legend2],
        extra_artists=None,
    )


#############################################
################## stacked ##################
#############################################
def _2_3_area(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["year", "platform"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["year", "platform"],
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
    stack_order = ["VR", "AR", "MR", "XR"]
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="year",
        y_axis="count",
        z_axis="platform",
    )

    colors_map = get_colors_map(
        values=z_values,
        colors=COLORS,
        color_field="platform",
    )

    handles1 = get_legend_handles(
        values=stack_order,
        colors_map=colors_map,
    )
    handles2 = get_legend_handles(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
        },
    )

    ### plot_style
    orientation = "v"
    coloring_values_list = draw_stacked(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Year",
            "y_label": "Number of Studies",
            "title": "Platform Adoption Over Time",
            "rotation": 45,
        },
        orientation="area",
        stack_order=stack_order,
    )

    number_area(
        ax=ax,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_area(
        ax=ax,
        coloring_values=coloring_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Platform",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1, type="upper")
    text_clean_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_2_3_area",
        legends=[legend1, legend2],
        extra_artists=None,
    )


def _2_3_bar(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["year", "platform"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["year", "platform"],
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
    stack_order = ["VR", "AR", "MR", "XR"]
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="year",
        y_axis="count",
        z_axis="platform",
    )

    colors_map = get_colors_map(
        values=z_values,
        colors=COLORS,
        color_field="platform",
    )

    handles1 = get_legend_handles(
        values=stack_order,
        colors_map=colors_map,
    )
    handles2 = get_legend_handles(
        values=["Custom A", "Custom B", "Custom C"],
        colors_map={
            "Custom A": "#ff0000",
            "Custom B": "#008000",
            "Custom C": "#0000ff",
        },
    )

    ### plot_style
    orientation = "v"
    coloring_values_list = draw_stacked(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Year",
            "y_label": "Number of Studies",
            "title": "Platform Adoption Over Time",
            "rotation": 45,
        },
        orientation=orientation,
        stack_order=stack_order,
    )

    number_bar(
        ax=ax,
        orientation=orientation,
        offset=1,
    )
    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_bar(
        ax=ax,
        coloring_values=coloring_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Platform",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Custom Legend",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1, type="upper")
    text_clean_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_2_3_bar",
        legends=[legend1, legend2],
        extra_artists=None,
    )


def _4_5_area(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["software_category", "software", "year"],
    )
    dataset_counted_pre = count_dataset(
        dataset=dataset_filtered,
        fields=["software_category", "software"],
    )
    dataset_counted_pos = count_dataset(
        dataset=dataset_filtered,
        fields=["software_category", "software", "year"],
    )

    filter_values = ["software != "]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pre = filter_dataset_by_values(
                dataset=dataset_counted_pre,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = "count >= 10"
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre = filter_dataset_by_count(
            dataset=dataset_counted_pre,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    selected_softwares = [row[0] for row in dataset_counted_pre["software"]]
    filter_values = ["software == " + ", ".join(selected_softwares)]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pos = filter_dataset_by_values(
                dataset=dataset_counted_pos,
                field=field,
                values=values,
                include=operation,
            )

    ### output
    print_dict(dataset_counted_pre)
    print_counts(dataset_counted_pre, decimal=1)
    print_dict(dataset_counted_pos)
    print_counts(dataset_counted_pos, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted_pos,
        x_axis="year",
        y_axis="count",
        z_axis="software",
    )

    colors_map = get_colors_map(
        values=z_values,
        colors=COLORS,
        color_field="software",
    )

    handles1 = get_legend_handles(
        values=z_values,
        colors_map=colors_map,
    )
    handles2 = get_legend_handles(
        values=COLORS["labels_extra"].keys(),
        colors_map=COLORS["labels_extra"],
    )

    ### plot_style
    orientation = "v"
    coloring_values_list = draw_stacked(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Year",
            "y_label": "Number of Studies",
            "title": "Software Usage Trend Over Time",
            "rotation": 45,
        },
        orientation="area",
        stack_order=None,
    )

    add_grid(
        ax=ax,
        orientation=orientation,
    )

    color_area(
        ax=ax,
        coloring_values=coloring_values_list,
        colors_map=colors_map,
        border=False,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Software",
        loc="upper left",
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Software Category",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend1, type="title")
    text_clean_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_4_5_area",
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

    color_pie(
        ax=ax,
        coloring_values=x_values_list,
        colors_map=colors_map,
        border=True,
    )
    color_pie_labels(
        ax=ax,
        color="white",
    )

    font_apply_plot(
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


#############################################
################# pie_nested ################
#############################################
def _1_4(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["historical_site_type", "historical_site_type_sub"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["historical_site_type", "historical_site_type_sub"],
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
        x_axis="historical_site_type",
        y_axis="count",
        z_axis="historical_site_type_sub",
    )

    (
        inner_labels,
        inner_labels_count,
        outer_labels,
        outer_labels_count,
        _,
    ) = calculate_labels_nested(x_values, y_values, z_values)

    inner_colors_map = get_colors_map(
        values=inner_labels,
        colors=COLORS,
        color_field="historical_site_type",
    )
    outer_colors_map = get_colors_map(
        values=outer_labels,
        colors=COLORS,
        color_field="historical_site_type_sub",
    )
    full_colors_map = {**inner_colors_map, **outer_colors_map}

    ### plot_style
    labels_list = draw_pie_nested(
        ax=ax,
        inner_labels=inner_labels,
        inner_labels_count=inner_labels_count,
        outer_labels=outer_labels,
        outer_labels_count=outer_labels_count,
        labels_spec={
            "title": "Historical Site Type & Sub-Type Distribution",
        },
    )

    color_pie(
        ax=ax,
        coloring_values=labels_list,
        colors_map=full_colors_map,
        border=False,
    )
    color_pie_labels(
        ax=ax,
        color="white",
        target="inner",
    )
    color_pie_labels(
        ax=ax,
        color="black",
        target="outer",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_1_4",
        legends=None,
        extra_artists=None,
    )


def _3_2(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["technique", "technique_sub"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["technique", "technique_sub"],
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
        z_axis="technique_sub",
    )

    (
        inner_labels,
        inner_labels_count,
        outer_labels,
        outer_labels_count,
        _,
    ) = calculate_labels_nested(x_values, y_values, z_values)

    inner_colors_map = get_colors_map(
        values=inner_labels,
        colors=COLORS,
        color_field="technique",
    )
    outer_colors_map = get_colors_map(
        values=outer_labels,
        colors=COLORS,
        color_field="technique_sub",
    )
    full_colors_map = {**inner_colors_map, **outer_colors_map}

    ### plot_style
    labels_list = draw_pie_nested(
        ax=ax,
        inner_labels=inner_labels,
        inner_labels_count=inner_labels_count,
        outer_labels=outer_labels,
        outer_labels_count=outer_labels_count,
        labels_spec={
            "title": "Technique & Sub-Technique Distribution",
        },
    )

    color_pie(
        ax=ax,
        coloring_values=labels_list,
        colors_map=full_colors_map,
        border=False,
    )
    color_pie_labels(
        ax=ax,
        color="white",
        target="inner",
    )
    color_pie_labels(
        ax=ax,
        color="black",
        target="outer",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_3_2",
        legends=None,
        extra_artists=None,
    )


#############################################
################### heatmap #################
#############################################
def _3_3(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["historical_site_type", "technique"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["historical_site_type", "technique"],
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
        x_axis="historical_site_type",
        y_axis="count",
        z_axis="technique",
    )

    ### plot_style
    matrix = draw_heatmap(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Historical Site Type",
            "y_label": "Technique",
            "title": "Historical Site Type X Technique",
            "rotation": 45,
        },
    )

    number_heatmap(
        ax=ax,
        matrix=matrix,
    )

    color_heatmap(
        ax=ax,
        matrix=matrix,
        cmap="viridis",
    )
    color_heatmap_labels(
        ax=ax,
        color="white",
    )

    legend_create_colorbar(
        ax=ax,
        title="Count",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_3_3",
        legends=None,
        extra_artists=None,
    )


def _4_2(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["software_category", "software", "technique"],
    )
    dataset_counted_pre = count_dataset(
        dataset=dataset_filtered,
        fields=["software_category", "software"],
    )
    dataset_counted_pos = count_dataset(
        dataset=dataset_filtered,
        fields=["software_category", "software", "technique"],
    )

    filter_values = ["software != "]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pre = filter_dataset_by_values(
                dataset=dataset_counted_pre,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = "count >= 5"
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre = filter_dataset_by_count(
            dataset=dataset_counted_pre,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    selected_softwares = [r[0] for r in dataset_counted_pre["software"]]
    selected_softwares_cat = [r[0] for r in dataset_counted_pre["software_category"]]
    filter_values = ["software == " + ", ".join(selected_softwares)]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pos = filter_dataset_by_values(
                dataset=dataset_counted_pos,
                field=field,
                values=values,
                include=operation,
            )

    ### output
    print_dict(dataset_counted_pos)
    print_counts(dataset_counted_pos, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted_pos,
        x_axis="software",
        y_axis="count",
        z_axis="technique",
    )
    labels_center = calculate_labels_pos_bar(
        values=selected_softwares_cat,
        distance=5,
    )

    colors_map = get_colors_map(
        values=selected_softwares_cat,
        colors=COLORS,
        color_field="software_category",
    )
    colors_mapped = map_colors_map(
        colors_from=selected_softwares,
        colors_to=selected_softwares_cat,
        colors_map=colors_map,
    )

    ### plot_style
    orientation = "v"
    matrix = draw_heatmap(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "",
            "y_label": "Technique",
            "title": "Software X Technique",
            "rotation": 45,
        },
    )

    number_heatmap(
        ax=ax,
        matrix=matrix,
    )
    texts = add_labels_extra(
        ax=ax,
        labels_center=labels_center,
        orientation=orientation,
        offset=-6,
    )

    color_heatmap(
        ax=ax,
        matrix=matrix,
        cmap="viridis",
    )
    color_heatmap_labels(
        ax=ax,
        color="white",
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_mapped,
        orientation=orientation,
    )
    color_labels_extra(
        ax=texts,
        colors_map=colors_map,
    )

    legend_create_colorbar(
        ax=ax,
        title="Count",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    text_clean_labels(texts)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_4_2",
        legends=None,
        extra_artists=texts,
    )


def _4_3(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["software_modeling", "software_data"],
    )
    dataset_counted_pre1 = count_dataset(
        dataset=dataset_filtered,
        fields=["software_modeling"],
    )
    dataset_counted_pre2 = count_dataset(
        dataset=dataset_filtered,
        fields=["software_data"],
    )
    dataset_counted_pos = count_dataset(
        dataset=dataset_filtered,
        fields=["software_modeling", "software_data"],
    )

    filter_values = ["software_modeling != ", "software_data != "]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pos = filter_dataset_by_values(
                dataset=dataset_counted_pos,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = "count >= 5"
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre1 = filter_dataset_by_count(
            dataset=dataset_counted_pre1,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    filter_count = "count >= 5"
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre2 = filter_dataset_by_count(
            dataset=dataset_counted_pre2,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    selected_softwares_m = [r[0] for r in dataset_counted_pre1["software_modeling"]]
    selected_softwares_r = [r[0] for r in dataset_counted_pre2["software_data"]]
    filter_values = [
        "software_modeling == " + ", ".join(selected_softwares_m),
        "software_data == " + ", ".join(selected_softwares_r),
    ]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pos = filter_dataset_by_values(
                dataset=dataset_counted_pos,
                field=field,
                values=values,
                include=operation,
            )

    ### output
    print_dict(dataset_counted_pos)
    print_counts(dataset_counted_pos, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted_pos,
        x_axis="software_modeling",
        y_axis="count",
        z_axis="software_data",
    )

    ### plot_style
    matrix = draw_heatmap(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Software Modeling",
            "y_label": "Software Data",
            "title": "Software Modeling X Software Data",
            "rotation": 45,
        },
    )

    number_heatmap(
        ax=ax,
        matrix=matrix,
    )

    color_heatmap(
        ax=ax,
        matrix=matrix,
        cmap="viridis",
    )
    color_heatmap_labels(
        ax=ax,
        color="white",
    )

    legend_create_colorbar(
        ax=ax,
        title="Count",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_4_3",
        legends=None,
        extra_artists=None,
    )


def _4_4(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["software_modeling", "software_render"],
    )
    dataset_counted_pre1 = count_dataset(
        dataset=dataset_filtered,
        fields=["software_modeling"],
    )
    dataset_counted_pre2 = count_dataset(
        dataset=dataset_filtered,
        fields=["software_render"],
    )
    dataset_counted_pos = count_dataset(
        dataset=dataset_filtered,
        fields=["software_modeling", "software_render"],
    )

    filter_values = ["software_modeling != ", "software_render != "]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pos = filter_dataset_by_values(
                dataset=dataset_counted_pos,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = "count >= 5"
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre1 = filter_dataset_by_count(
            dataset=dataset_counted_pre1,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    filter_count = "count >= 3"
    if filter_count:
        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre2 = filter_dataset_by_count(
            dataset=dataset_counted_pre2,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

    selected_softwares_m = [r[0] for r in dataset_counted_pre1["software_modeling"]]
    selected_softwares_r = [r[0] for r in dataset_counted_pre2["software_render"]]
    filter_values = [
        "software_modeling == " + ", ".join(selected_softwares_m),
        "software_render == " + ", ".join(selected_softwares_r),
    ]
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pos = filter_dataset_by_values(
                dataset=dataset_counted_pos,
                field=field,
                values=values,
                include=operation,
            )

    ### output
    print_dict(dataset_counted_pos)
    print_counts(dataset_counted_pos, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted_pos,
        x_axis="software_modeling",
        y_axis="count",
        z_axis="software_render",
    )

    ### plot_style
    matrix = draw_heatmap(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Software Modeling",
            "y_label": "Software Render",
            "title": "Software Modeling X Software Render",
            "rotation": 45,
        },
    )

    number_heatmap(
        ax=ax,
        matrix=matrix,
    )

    color_heatmap(
        ax=ax,
        matrix=matrix,
        cmap="viridis",
    )
    color_heatmap_labels(
        ax=ax,
        color="white",
    )

    legend_create_colorbar(
        ax=ax,
        title="Count",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_4_4",
        legends=None,
        extra_artists=None,
    )


#############################################
################### scatter #################
#############################################
def _5_1(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset, fields=["continent", "country", "historical_site_type"]
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["continent", "country", "historical_site_type"],
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
        x_axis="country",
        y_axis="count",
        z_axis="historical_site_type",
    )
    continent_values = [row[0] for row in dataset_counted["continent"]]
    count_values = [min(y_values), max(y_values)]
    marker_config = {
        "linecolor": "white",
        "marker": "o",
        "facecolor": "steelblue",
        "edgecolor": "black",
        "edgewidth": 0,
        "markersize": [7, 25],
        "opacity": 0.5,
    }

    colors_map = get_colors_map(
        values=continent_values,
        colors=COLORS,
        color_field="continent",
    )
    colors_mapped = map_colors_map(
        colors_from=x_values,
        colors_to=continent_values,
        colors_map=colors_map,
    )

    handles1 = get_legend_handles_bubble(
        values=count_values,
        config=marker_config,
    )
    handles2 = get_legend_handles(
        values=continent_values,
        colors_map=colors_map,
    )

    ### plot_style
    draw_scatter(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec={
            "x_label": "Country",
            "y_label": "Historical Site Type",
            "title": "Country X Historical Site Type",
            "rotation": 45,
        },
        count_values=count_values,
        markersize=marker_config["markersize"],
    )

    add_grid(
        ax=ax,
        orientation="both",
    )

    color_scatter(
        ax=ax,
        config=marker_config,
    )
    color_bar_labels(
        ax=ax,
        colors_map=colors_mapped,
        orientation="v",
    )

    legend1 = legend_create(
        ax=ax,
        handles=handles1,
        title="Frequency",
        loc="upper left",
        bbox=(1, 0, 0.3, 1),
        labelspacing=1.0,  # Vertical spacing
        handletextpad=1.0,  # Icon--Text spacing
        borderpad=1.0,  # Border padding
    )
    legend2 = legend_create(
        ax=ax,
        handles=handles2,
        title="Region",
        loc="lower left",
    )

    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend1,
        fonts=FONTS_LEGEND,
    )
    font_apply_legend(
        legend=legend2,
        fonts=FONTS_LEGEND,
    )

    text_clean_legend(legend2)

    ### output
    show_plot()
    save_plot(
        fig=fig,
        name="_5_1",
        legends=[legend1, legend2],
        extra_artists=None,
    )


#############################################
################## sunburst #################
#############################################
def _1_4_S(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["historical_site_type", "historical_site_type_sub"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["historical_site_type", "historical_site_type_sub"],
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
    ax = draw_plot_plotly()

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis="historical_site_type",
        y_axis="count",
        z_axis="historical_site_type_sub",
    )

    (
        inner_labels,
        inner_labels_count,
        outer_labels,
        outer_labels_count,
        inner_outer_links,
    ) = calculate_labels_nested(x_values, y_values, z_values)

    all_labels = inner_labels + outer_labels
    all_parents = [""] * len(inner_labels) + inner_outer_links
    all_counts = inner_labels_count + outer_labels_count

    inner_colors_map = get_colors_map(
        values=inner_labels,
        colors=COLORS,
        color_field="historical_site_type",
    )
    outer_colors_map = get_colors_map(
        values=outer_labels,
        colors=COLORS,
        color_field="historical_site_type_sub",
    )
    full_colors_map = {**inner_colors_map, **outer_colors_map}

    ### plot_style
    fig = draw_sunburst(
        ax=ax,
        all_labels=all_labels,
        all_parents=all_parents,
        all_counts=all_counts,
        labels_spec={
            "title": "Historical Site Type & Sub-Type Distribution",
        },
    )

    color_sunburst(
        ax=fig,
        coloring_values=all_labels,
        colors_map=full_colors_map,
        border=False,
    )
    color_sunburst_labels(
        ax=fig,
        color="white",
        target="inner",
    )
    color_sunburst_labels(
        ax=fig,
        color="black",
        target="outer",
    )

    font_apply_plot(
        ax=fig,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot_plotly(fig)


#############################################
#################### sankey #################
#############################################
def _3_1(dataset):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=["study_focus", "historical_site_type", "technique"],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["study_focus", "historical_site_type", "technique"],
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
    ax = draw_plot_plotly()

    ### plot_get
    column1 = [r[0] for r in dataset_counted["study_focus"]]
    column2 = [r[0] for r in dataset_counted["historical_site_type"]]
    column3 = [r[0] for r in dataset_counted["technique"]]
    counts = dataset_counted["count"]

    (
        labels,
        sources,
        targets,
        values,
    ) = calculate_sankey_flows(column1, column2, column3, counts)

    colors_1 = get_colors_map(
        values=column1,
        colors=COLORS,
        color_field="study_focus",
    )
    colors_2 = get_colors_map(
        values=column2,
        colors=COLORS,
        color_field="historical_site_type",
    )
    colors_3 = get_colors_map(values=column3, colors=COLORS, color_field="technique")
    full_colors_map = {**colors_1, **colors_2, **colors_3}

    ### plot_style
    fig = draw_sankey(
        ax=ax,
        labels=labels,
        sources=sources,
        targets=targets,
        values=values,
        labels_spec={
            "title": "Workflow: Study Focus -> Site -> Technique",
        },
    )

    color_sankey_nodes(
        ax=fig,
        labels_list=labels,
        colors_map=full_colors_map,
        pad=15,
        thickness=20,
    )
    color_sankey_links(
        ax=fig,
        color="gray",
        opacity=0.25,
    )
    color_sankey_labels(
        ax=fig,
        color="black",
    )

    font_apply_plot(
        ax=fig,
        fonts=FONTS_PLOT,
    )

    ### output
    show_plot_plotly(fig)


#############################################
##################### map ###################
#############################################
def _5_2(dataset):
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
    ax = draw_plot_plotly()

    ### plot_get
    x_values, y_values = get_labels(
        dataset=dataset_counted,
        x_axis="country",
        y_axis="count",
        z_axis=None,
    )
    corrected_values = correct_values(
        values=x_values,
        correction_map={
            "Turkiye": "Turkey",
            "USA": "United States",
            "UK": "United Kingdom",
            "South Korea": "Korea, South",
        },
    )

    ### plot_style
    fig = draw_map(
        ax=ax,
        countries=corrected_values,
        counts=y_values,
        labels_spec={
            "title": "Geographical Distribution of Publications",
        },
    )

    legend_cbar = legend_create_mapbar(
        ax=fig,
        title="Publications",
    )

    color_map(
        ax=fig,
        cmap="YlOrRd",
        border=True,
        frame=True,
    )
    color_map_labels(
        ax=fig,
        color="black",
    )

    font_apply_plot(
        ax=fig,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend_cbar,
        fonts=FONTS_LEGEND,
    )

    ### output
    show_plot_plotly(fig)


#############################################
################## prisma ###################
#############################################
def _0_1(dataset):
    dataset_with_id = add_dataset_id(dataset=dataset, field="id")

    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset_with_id,
        fields=[
            "id",
            "year",
            "country",
            "study_focus",
            "historical_site_type",
            "historical_site_type_sub",
            "device",
        ],
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=[
            "id",
            "year",
            "country",
            "study_focus",
            "historical_site_type",
            "historical_site_type_sub",
            "device",
        ],
    )
    n_eligible = get_unique_count(dataset=dataset_counted, field="id")

    ### filter
    dataset_counted_religious = filter_dataset_by_values(
        dataset=dataset_counted,
        field="historical_site_type_sub",
        values=["Religious"],
        include=True,
    )
    n_religious = get_unique_count(dataset=dataset_counted_religious, field="id")

    dataset_counted_device = filter_dataset_by_values(
        dataset=dataset_counted_religious,
        field="device",
        values=["HMD"],
        include=True,
    )
    n_device = get_unique_count(dataset=dataset_counted_device, field="id")

    dataset_counted_studyfocus = filter_dataset_by_values(
        dataset=dataset_counted_device,
        field="study_focus",
        values=["Reconstruction"],
        include=True,
    )
    n_studyfocus = get_unique_count(dataset=dataset_counted_studyfocus, field="id")

    values = {
        "search": 614,
        "duplicates": 256,
        "screening": 358,
        "excluded": 266,
        "eligible": n_eligible,
        "religious": n_religious,
        "hmd": n_device,
        "final": n_studyfocus,
    }

    ### output
    name = "_0_1"
    dot = draw_plot_graphviz(
        name=name,
        position="TB",
        splines="polyline",
        nodesep="0.45",
        ranksep="0.72",
    )

    topology = {
        "nodes": {
            "search": f"Studies identified via\nsystematic search\n(n = {values['search']})",
            "duplicates": f"Duplicates & non-relevant records removed\n(n = {values['duplicates']})",
            "screening": f"Studies after deduplication\n(n = {values['screening']})",
            "excluded": f"Studies excluded (score < 4.5)\n(n = {values['excluded']})",
            "eligible": f"Studies passing eligibility screening\n(n = {values['eligible']})",
            "religious": f"Studies on religious buildings\n(n = {values['religious']})",
            "hmd": f"Studies using HMD technology\n(n = {values['hmd']})",
            "final": f"Final selected studies:\nReconstruction-focused\n(n = {values['final']})",
            "note1": "Step 1 - Exclusions:\n• Duplicate records\n• Non-peer-reviewed\n• Book chapters",
            "note2": "Step 2 - Screening Criteria:\n✔ Case study or prototype\n✔ Historical reconstruction\n✔ VR/AR/MR/XR integration",
            "note3": "Step 3 - Final Filtering:\n✔ Religious buildings\n✔ HMD implementation\n✔ Reconstruction focus",
        },
        "flow": [
            ("search", "duplicates"),
            ("duplicates", "screening"),
            ("screening", "excluded"),
            ("screening", "eligible"),
            ("eligible", "religious"),
            ("religious", "hmd"),
            ("hmd", "final"),
        ],
        "notes": [
            ("duplicates", "note1"),
            ("screening", "note2"),
            ("hmd", "note3"),
        ],
    }
    draw_prisma_nodes(
        dot=dot,
        nodes=topology["nodes"],
    )

    style_prisma(
        ax=dot,
        config=STYLE_PRISMA["box_main"],
        nodes=[
            "search",
            "screening",
            "eligible",
            "religious",
            "hmd",
            "final",
        ],
    )
    style_prisma(
        ax=dot,
        config=STYLE_PRISMA["box_excluded"],
        nodes=["duplicates", "excluded"],
    )
    style_prisma(
        ax=dot,
        config=STYLE_PRISMA["note"],
        nodes=[
            "note1",
            "note2",
            "note3",
        ],
    )
    style_prisma(
        ax=dot,
        config=STYLE_PRISMA["edge_flow"],
    )
    draw_prisma_edges(
        dot=dot,
        edges=topology["flow"],
    )

    style_prisma(
        ax=dot,
        config=STYLE_PRISMA["edge_note"],
    )
    draw_prisma_edges(
        dot=dot,
        edges=topology["notes"],
    )

    ### output
    show_plot_graphviz(dot=dot)
    save_plot_graphviz(dot=dot, name=name)


##############################################
################## refactor ##################
##############################################


def bar_1D(
    dataset,
    fields,
    filter_values,
    filter_count,
    x_axis,
    y_axis,
    z_axis,
    orientation,
    color_field,
    color_mapping=False,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_extra=None,
    labels_spec=None,
    legends_config=None,
    save_name="chart",
):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=fields,
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=fields,
    )

    filter_values = filter_values
    if filter_values:
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted = filter_dataset_by_values(
                dataset=dataset_counted,
                field=field,
                values=values,
                include=operation,
            )

    filter_count = filter_count
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
        x_axis=x_axis,
        y_axis=y_axis,
        z_axis=z_axis,
    )
    colors_map = get_colors_map(
        colors=COLORS,
        color_field=color_field,
    )

    ### plot_draw
    coloring_values = draw_bar_1D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec=labels_spec,
        orientation=orientation,
    )

    if color_mapping:
        colors_mapped = map_colors_map(
            colors_from=x_values,
            colors_to=z_values,
            colors_map=colors_map,
        )
        color_bar(
            ax=ax,
            coloring_values=coloring_values,
            colors_map=colors_mapped,
            border=bar_borders,
        )
        color_bar_labels(
            ax=ax,
            colors_map=colors_mapped,
            orientation=orientation,
        )
    else:
        color_bar(
            ax=ax,
            coloring_values=coloring_values,
            colors_map=colors_map,
            border=bar_borders,
        )
        color_bar_labels(
            ax=ax,
            colors_map=colors_map,
            orientation=orientation,
        )

    ### extra ###
    if bar_numbers:
        number_bar(
            ax=ax,
            orientation=orientation,
        )
    if grids:
        add_grid(
            ax=ax,
            orientation=orientation,
        )
    extra_artists = None
    if labels_extra:
        labels_center = calculate_labels_pos_bar(
            values=[i[0] for i in dataset_counted[labels_extra]],
            distance=5,
        )
        texts = add_labels_extra(
            ax=ax,
            labels_center=labels_center,
            orientation=orientation,
            offset=15,
        )
        color_labels_extra(
            ax=texts,
            colors_map=colors_map,
        )
        text_clean_labels(texts)
        extra_artists = texts

    ### font ###
    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### legend ###
    legends = []
    if legends_config:
        for config in legends_config:
            if config.get("source") == "dataset":
                labels = config.get("values", [])
                values = [i[0] for i in dataset_counted[labels]]
            if config.get("source") == "custom":
                values = config.get("values", [])
                colors_map = config.get("colors_map", {})

            handles = get_legend_handles(
                values=values,
                colors_map=colors_map,
            )
            legend = legend_create(
                ax=ax,
                handles=handles,
                legend_spec=config.get("legend_spec"),
            )
            font_apply_legend(
                legend=legend,
                fonts=FONTS_LEGEND,
            )
            text_clean_legend(legend)
            legends.append(legend)

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=legends,
        extra_artists=extra_artists,
    )
