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


def bar_1D(
    dataset,
    fields,
    filter_values,
    filter_count,
    x_axis,
    y_axis,
    z_axis,
    orientation,
    coloring_field,
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

    ### output
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
        coloring_field=coloring_field,
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
            offset=1,
        )
    if grids:
        add_grid(
            ax=ax,
            orientation=orientation,
            linewidth=0.5,
            opacity=0.5,
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
        text_clean_labels(
            texts=texts,
            casetype="title",
        )
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
                colors_map = get_colors_map(
                    colors=COLORS,
                    coloring_field=config.get("coloring_field"),
                )
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
            text_clean_legend(
                legend=legend,
                casetype=config.get("casetype"),
            )
            legends.append(legend)

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=legends,
        extra_artists=extra_artists,
    )


def bar_2D(
    dataset,
    fields,
    filter_values,
    filter_count,
    x_axis,
    y_axis,
    z_axis,
    orientation,
    coloring_field,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
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

    ### output
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
        coloring_field=coloring_field,
    )

    ### plot_draw
    coloring_values = draw_bar_2D(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec=labels_spec,
        orientation=orientation,
    )

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
            offset=1,
        )
    if grids:
        add_grid(
            ax=ax,
            orientation=orientation,
            linewidth=0.5,
            opacity=0.5,
        )

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
                colors_map = get_colors_map(
                    colors=COLORS,
                    coloring_field=config.get("coloring_field"),
                )
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
            text_clean_legend(
                legend=legend,
                casetype=config.get("casetype"),
            )
            legends.append(legend)

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=legends,
        extra_artists=None,
    )


def stacked(
    dataset,
    fields,
    filter_pre,
    filter_values,
    filter_count,
    x_axis,
    y_axis,
    z_axis,
    orientation,
    stack_order,
    coloring_field,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_spec=None,
    legends_config=None,
    save_name="chart",
):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=fields,
    )

    if filter_pre:
        dataset_counted_pre = count_dataset(
            dataset=dataset_filtered,
            fields=filter_pre,
        )

        target_field = ""
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pre = filter_dataset_by_values(
                dataset=dataset_counted_pre,
                field=field,
                values=values,
                include=operation,
            )
            target_field = field

        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre = filter_dataset_by_count(
            dataset=dataset_counted_pre,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

        dataset_counted = count_dataset(
            dataset=dataset_filtered,
            fields=fields,
        )

        valid_items = [row[0] for row in dataset_counted_pre[target_field]]
        dataset_counted = filter_dataset_by_values(
            dataset=dataset_counted,
            field=target_field,
            values=valid_items,
            include=True,
        )
        print_counts(dataset_counted_pre, decimal=1)
    else:
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

    ### output
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
        coloring_field=coloring_field,
    )

    ### plot_draw
    coloring_values = draw_stacked(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec=labels_spec,
        orientation=orientation,
        stack_order=stack_order,
    )

    if orientation == "area":
        orientation = "v"
        color_area(
            ax=ax,
            coloring_values=coloring_values,
            colors_map=colors_map,
            border=bar_borders,
        )
        if bar_numbers:
            number_area(
                ax=ax,
                offset=1,
            )
    else:
        color_bar(
            ax=ax,
            coloring_values=coloring_values,
            colors_map=colors_map,
            border=bar_borders,
        )
        if bar_numbers:
            number_bar(
                ax=ax,
                orientation=orientation,
                offset=1,
            )

    color_bar_labels(
        ax=ax,
        colors_map=colors_map,
        orientation=orientation,
    )

    ### extra ###
    if grids:
        add_grid(
            ax=ax,
            orientation=orientation,
            linewidth=0.5,
            opacity=0.5,
        )

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
                colors_map = get_colors_map(
                    colors=COLORS,
                    coloring_field=config.get("coloring_field"),
                )
            if config.get("source") == "custom":
                values = config.get("values", [])
                colors_map = config.get("colors_map", {})

            handles = get_legend_handles(
                values=stack_order if stack_order else values,
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
            text_clean_legend(
                legend=legend,
                casetype=config.get("casetype"),
            )
            legends.append(legend)

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=legends,
        extra_artists=None,
    )


def pie(
    dataset,
    fields,
    filter_values,
    filter_count,
    x_axis,
    y_axis,
    coloring_field,
    labels_color,
    bar_borders=False,
    labels_spec=None,
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

    ### output
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis=x_axis,
        y_axis=y_axis,
        z_axis=None,
    )
    colors_map = get_colors_map(
        colors=COLORS,
        coloring_field=coloring_field,
    )

    ### plot_draw
    coloring_values = draw_pie(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        labels_spec=labels_spec,
    )

    color_pie(
        ax=ax,
        coloring_values=coloring_values,
        colors_map=colors_map,
        border=bar_borders,
    )
    color_pie_labels(
        ax=ax,
        color=labels_color,
        target=None,
    )

    ### font ###
    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=None,
        extra_artists=None,
    )


def pie_nested(
    dataset,
    fields,
    filter_values,
    filter_count,
    x_axis,
    y_axis,
    z_axis,
    coloring_field_inner,
    coloring_field_outer,
    labels_color_inner,
    labels_color_outer,
    bar_borders=False,
    labels_spec=None,
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

    ### output
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis=x_axis,
        y_axis=y_axis,
        z_axis=z_axis,
    )
    (
        inner_labels,
        inner_labels_count,
        outer_labels,
        outer_labels_count,
        _,
    ) = calculate_labels_nested(x_values, y_values, z_values)

    inner_colors_map = get_colors_map(
        colors=COLORS,
        coloring_field=coloring_field_inner,
    )
    outer_colors_map = get_colors_map(
        colors=COLORS,
        coloring_field=coloring_field_outer,
    )
    full_colors_map = {**inner_colors_map, **outer_colors_map}

    ### plot_draw
    coloring_values = draw_pie_nested(
        ax=ax,
        inner_labels=inner_labels,
        inner_labels_count=inner_labels_count,
        outer_labels=outer_labels,
        outer_labels_count=outer_labels_count,
        labels_spec=labels_spec,
    )

    color_pie(
        ax=ax,
        coloring_values=coloring_values,
        colors_map=full_colors_map,
        border=bar_borders,
    )
    color_pie_labels(
        ax=ax,
        color=labels_color_inner,
        target="inner",
    )
    color_pie_labels(
        ax=ax,
        color=labels_color_outer,
        target="outer",
    )

    ### font ###
    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=None,
        extra_artists=None,
    )


def heatmap(
    dataset,
    fields,
    filter_pre,
    filter_pre_sep,
    filter_values,
    filter_count,
    filter_count_sep,
    x_axis,
    y_axis,
    z_axis,
    cmap,
    labels_color,
    coloring_field=None,
    bar_numbers=True,
    labels_extra=None,
    labels_spec=None,
    save_name="chart",
):
    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset,
        fields=fields,
    )

    if filter_pre:
        dataset_counted_pre = count_dataset(
            dataset=dataset_filtered,
            fields=filter_pre,
        )

        target_field = ""
        for filter_value in filter_values:
            field, values, operation = parse_string(text=filter_value)
            dataset_counted_pre = filter_dataset_by_values(
                dataset=dataset_counted_pre,
                field=field,
                values=values,
                include=operation,
            )
            target_field = field

        field, values, operation = parse_string(text=filter_count)
        dataset_counted_pre = filter_dataset_by_count(
            dataset=dataset_counted_pre,
            field=field,
            value=int(values[0]),
            operation=operation,
        )

        dataset_counted = count_dataset(
            dataset=dataset_filtered,
            fields=fields,
        )

        valid_items = [row[0] for row in dataset_counted_pre[target_field]]
        dataset_counted = filter_dataset_by_values(
            dataset=dataset_counted,
            field=target_field,
            values=valid_items,
            include=True,
        )

    elif filter_pre_sep:
        dataset_counted_pre1 = count_dataset(
            dataset=dataset_filtered,
            fields=filter_pre_sep[0],
        )
        dataset_counted_pre2 = count_dataset(
            dataset=dataset_filtered,
            fields=filter_pre_sep[1],
        )
        dataset_counted = count_dataset(
            dataset=dataset_filtered,
            fields=fields,
        )

        if filter_values:
            target_fields = []
            for filter_value in filter_values:
                field, values, operation = parse_string(text=filter_value)
                dataset_counted = filter_dataset_by_values(
                    dataset=dataset_counted,
                    field=field,
                    values=values,
                    include=operation,
                )
                target_fields.append(field)

        if filter_count_sep:
            field, values1, operation = parse_string(text=filter_count_sep[0])
            dataset_counted_pre1 = filter_dataset_by_count(
                dataset=dataset_counted_pre1,
                field=field,
                value=int(values1[0]),
                operation=operation,
            )

            field, values2, operation = parse_string(text=filter_count_sep[1])
            dataset_counted_pre2 = filter_dataset_by_count(
                dataset=dataset_counted_pre2,
                field=field,
                value=int(values2[0]),
                operation=operation,
            )

        valid_items1 = [r[0] for r in dataset_counted_pre1[target_fields[0]]]
        valid_items2 = [r[0] for r in dataset_counted_pre2[target_fields[1]]]
        for field in target_fields:
            dataset_counted = filter_dataset_by_values(
                dataset=dataset_counted,
                field=field,
                values=valid_items1 + valid_items2,
                include=True,
            )

    else:
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

    ### output
    print_counts(dataset_counted, decimal=1)
    fig, ax = draw_plot(8, 6)

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis=x_axis,
        y_axis=y_axis,
        z_axis=z_axis,
    )
    if coloring_field:
        colors_map = get_colors_map(
            colors=COLORS,
            coloring_field=coloring_field,
        )

    ### plot_draw
    matrix = draw_heatmap(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec=labels_spec,
    )

    ### extra ###
    if bar_numbers:
        number_heatmap(
            ax=ax,
            matrix=matrix,
        )
    extra_artists = None
    if labels_extra:
        orientation = "v"
        values = [i[0] for i in dataset_counted_pre[labels_extra]]
        colors_mapped = map_colors_map(
            colors_from=valid_items,
            colors_to=values,
            colors_map=colors_map,
        )
        color_bar_labels(
            ax=ax,
            colors_map=colors_mapped,
            orientation=orientation,
        )
        labels_center = calculate_labels_pos_bar(
            values=values,
            distance=5,
        )
        texts = add_labels_extra(
            ax=ax,
            labels_center=labels_center,
            orientation=orientation,
            offset=-6,
        )
        color_labels_extra(
            ax=texts,
            colors_map=colors_map,
        )
        text_clean_labels(
            texts=texts,
            casetype="title",
        )
        extra_artists = texts

    color_heatmap(
        ax=ax,
        matrix=matrix,
        cmap=cmap,
    )
    color_heatmap_labels(
        ax=ax,
        color=labels_color,
    )

    ### font ###
    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### legend ###
    legend_create_colorbar(
        ax=ax,
        title="",
    )

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=None,
        extra_artists=extra_artists,
    )


def scatter(
    dataset,
    fields,
    filter_values,
    filter_count,
    x_axis,
    y_axis,
    z_axis,
    coloring_field,
    color_mapping=False,
    grids=True,
    labels_spec=None,
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

    ### output
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
        coloring_field=coloring_field,
    )
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

    legends = []
    if color_mapping:
        values = [row[0] for row in dataset_counted[coloring_field]]
        colors_mapped = map_colors_map(
            colors_from=x_values,
            colors_to=values,
            colors_map=colors_map,
        )
        handles_extra = get_legend_handles(
            values=values,
            colors_map=colors_map,
        )
        legend_extra = legend_create(
            ax=ax,
            handles=handles_extra,
            legend_spec={
                "title": "Region",
                "loc": "lower left",
                "bbox": (1, 0, 0.3, 1),
            },
        )
        font_apply_legend(
            legend=legend_extra,
            fonts=FONTS_LEGEND,
        )
        text_clean_legend(
            legend=legend_extra,
            casetype="title",
        )
        legends.append(legend_extra)

    ### plot_draw
    draw_scatter(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec=labels_spec,
        count_values=count_values,
        markersize=marker_config["markersize"],
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

    ### extra ###
    if grids:
        add_grid(
            ax=ax,
            orientation="both",
            linewidth=0.5,
            opacity=0.5,
        )

    ### font ###
    font_apply_plot(
        ax=ax,
        fonts=FONTS_PLOT,
    )

    ### legend ###
    handles = get_legend_handles_bubble(
        values=count_values,
        config=marker_config,
    )
    legend = legend_create(
        ax=ax,
        handles=handles,
        legend_spec={
            "title": "Frequency",
            "loc": "upper left",
            "bbox": (1, 0, 0.3, 1),
        },
        labelspacing=1.0,  # Vertical spacing
        handletextpad=1.0,  # Icon--Text spacing
        borderpad=1.0,  # Border padding
    )
    font_apply_legend(
        legend=legend,
        fonts=FONTS_LEGEND,
    )
    text_clean_legend(
        legend=legend,
        casetype="title",
    )
    legends.append(legend)

    ### output ###
    show_plot()
    save_plot(
        fig=fig,
        name=save_name,
        legends=legends,
        extra_artists=None,
    )
