from typing import Any, Dict, List, Optional, Tuple

from config.config import (
    COLORS,
    FONTS_PLOT,
    FONTS_LEGEND,
    STYLE_PRISMA,
)

from helper.helper import (
    add_dataset_id,
    correct_values,
    hide_text_keep_slice_fmt,
    hide_text_keep_slice,
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
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    z_axis: Optional[str],
    orientation: str,
    coloring_field: str,
    bar_borders: bool = False,
    bar_numbers: bool = True,
    grids: bool = True,
    color_mapping: bool = False,
    labels_extra: Optional[str] = None,
    labels_spec: Optional[Dict[str, Any]] = None,
    legends_config: Optional[List[Dict[str, Any]]] = None,
    save_name: Optional[str] = None,
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
        labels_spec=labels_spec if labels_spec else {},
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
    if save_name:
        show_plot()
        save_plot(
            fig=fig,
            name=save_name,
            legends=legends,
            extra_artists=extra_artists,
        )
    else:
        return fig, legends, extra_artists


def bar_2D(
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    z_axis: str,
    orientation: str,
    coloring_field: str,
    bar_borders: bool = False,
    bar_numbers: bool = True,
    grids: bool = True,
    stack_order: Optional[List[str]] = None,
    labels_spec: Optional[Dict[str, Any]] = None,
    legends_config: Optional[List[Dict[str, Any]]] = None,
    save_name: Optional[str] = None,
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
        labels_spec=labels_spec if labels_spec else {},
        orientation=orientation,
        stack_order=stack_order,
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
    extra_artists = None
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
    if save_name:
        show_plot()
        save_plot(
            fig=fig,
            name=save_name,
            legends=legends,
            extra_artists=extra_artists,
        )
    else:
        return fig, legends, extra_artists


def stacked(
    dataset: Dict,
    fields: List[str],
    filter_pre: Optional[List[str]],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    z_axis: str,
    orientation: str,
    coloring_field: str,
    stack_borders: bool = False,
    bar_numbers: bool = True,
    grids: bool = True,
    stack_order: Optional[List[str]] = None,
    labels_spec: Optional[Dict[str, Any]] = None,
    legends_config: Optional[List[Dict[str, Any]]] = None,
    save_name: Optional[str] = None,
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
        labels_spec=labels_spec if labels_spec else {},
        orientation=orientation,
        stack_order=stack_order,
    )

    if orientation == "area":
        orientation = "vertical"
        color_area(
            ax=ax,
            coloring_values=coloring_values,
            colors_map=colors_map,
            border=stack_borders,
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
            border=stack_borders,
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
    extra_artists = None
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
    if save_name:
        show_plot()
        save_plot(
            fig=fig,
            name=save_name,
            legends=legends,
            extra_artists=extra_artists,
        )
    else:
        return fig, legends, extra_artists


def pie(
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    coloring_field: str,
    labels_color: str,
    pie_borders: bool = False,
    labels_spec: Optional[Dict[str, Any]] = None,
    save_name: Optional[str] = None,
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
        labels_spec=labels_spec if labels_spec else {},
    )

    color_pie(
        ax=ax,
        coloring_values=coloring_values,
        colors_map=colors_map,
        border=pie_borders,
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
    legends = None
    extra_artists = None
    if save_name:
        show_plot()
        save_plot(
            fig=fig,
            name=save_name,
            legends=legends,
            extra_artists=extra_artists,
        )
    else:
        return fig, legends, extra_artists


def pie_nested(
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    z_axis: str,
    coloring_field_inner: str,
    coloring_field_outer: str,
    labels_color_inner: str,
    labels_color_outer: str,
    labels_hide_percent: int = 1,
    pie_borders: bool = False,
    labels_spec: Optional[Dict[str, Any]] = None,
    save_name: Optional[str] = None,
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

    inner_labels_display = hide_text_keep_slice(
        all_labels=inner_labels,
        all_counts=inner_labels_count,
        inner_labels_count=inner_labels_count,
        labels_hide_percent=labels_hide_percent,
    )
    outer_labels_display = hide_text_keep_slice(
        all_labels=outer_labels,
        all_counts=outer_labels_count,
        inner_labels_count=inner_labels_count,
        labels_hide_percent=labels_hide_percent,
    )

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
        labels_spec=labels_spec if labels_spec else {},
        inner_labels_display=inner_labels_display,
        outer_labels_display=outer_labels_display,
        labels_hide_percent=labels_hide_percent,
    )

    color_pie(
        ax=ax,
        coloring_values=coloring_values,
        colors_map=full_colors_map,
        border=pie_borders,
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
    legends = None
    extra_artists = None
    if save_name:
        show_plot()
        save_plot(
            fig=fig,
            name=save_name,
            legends=legends,
            extra_artists=extra_artists,
        )
    else:
        return fig, legends, extra_artists


def heatmap(
    dataset: Dict,
    fields: List[str],
    filter_pre: Optional[List[str]],
    filter_pre_sep: Optional[List[str]],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    filter_count_sep: Optional[List[str]],
    x_axis: str,
    y_axis: str,
    z_axis: str,
    cmap: str,
    labels_color: str,
    coloring_field: Optional[str] = None,
    border: bool = False,
    matrix_numbers: bool = True,
    labels_extra: Optional[Dict[str, Any]] = None,
    labels_spec: Optional[Dict[str, Any]] = None,
    save_name: Optional[str] = None,
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
        labels_spec=labels_spec if labels_spec else {},
    )

    ### extra ###
    if matrix_numbers:
        number_heatmap(
            ax=ax,
            matrix=matrix,
        )
    extra_artists = None
    if labels_extra:
        orientation = "vertical"
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
        border=border,
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
    legends = None
    if save_name:
        show_plot()
        save_plot(
            fig=fig,
            name=save_name,
            legends=legends,
            extra_artists=extra_artists,
        )
    else:
        return fig, legends, extra_artists


def scatter(
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    z_axis: str,
    coloring_field: str,
    color_mapping: bool = False,
    grids: bool = True,
    labels_spec: Optional[Dict[str, Any]] = None,
    legends_config: Optional[List[Dict[str, Any]]] = None,
    save_name: Optional[str] = None,
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
                dataset=dataset_counted, field=field, values=values, include=operation
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

    marker_config = {
        "linecolor": "white",
        "marker": "o",
        "facecolor": "steelblue",
        "edgecolor": "black",
        "edgewidth": 0,
        "markersize": [7, 25],
        "opacity": 0.5,
    }

    colors_mapped = None
    if color_mapping:
        colors_map = get_colors_map(
            colors=COLORS,
            coloring_field=coloring_field,
        )
        values = [row[0] for row in dataset_counted[coloring_field]]
        colors_mapped = map_colors_map(
            colors_from=x_values,
            colors_to=values,
            colors_map=colors_map,
        )

    ### plot_draw
    draw_scatter(
        ax=ax,
        x_values=x_values,
        y_values=y_values,
        z_values=z_values,
        labels_spec=labels_spec if labels_spec else {},
        count_values=[min(y_values), max(y_values)],
        markersize=marker_config["markersize"],
    )

    color_scatter(
        ax=ax,
        config=marker_config,
    )

    ### extra ###
    if colors_mapped:
        color_bar_labels(
            ax=ax,
            colors_map=colors_mapped,
            orientation="vertical",
        )
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
    legends = []
    if legends_config:
        for config in legends_config:
            if config.get("source") == "dataset":
                values = [row[0] for row in dataset_counted[config.get("values")]]
                colors_map = get_colors_map(
                    colors=COLORS,
                    coloring_field=config.get("coloring_field"),
                )
                handles = get_legend_handles(
                    values=values,
                    colors_map=colors_map,
                )
                kwargs = {}
                text_clean_legend(
                    legend=legend,
                    casetype=config.get("casetype"),
                )
            if config.get("source") == "bubble":
                handles = get_legend_handles_bubble(
                    values=[min(y_values), max(y_values)],
                    config=marker_config,
                )
                kwargs = {
                    "labelspacing": 1.0,
                    "handletextpad": 1.0,
                    "borderpad": 1.0,
                }

            legend = legend_create(
                ax=ax,
                handles=handles,
                legend_spec=config.get("legend_spec"),
                **kwargs,
            )
            font_apply_legend(
                legend=legend,
                fonts=FONTS_LEGEND,
            )
            legends.append(legend)

    ### output ###
    extra_artists = None
    if save_name:
        show_plot()
        save_plot(
            fig=fig,
            name=save_name,
            legends=legends,
            extra_artists=extra_artists,
        )
    else:
        return fig, legends, extra_artists


def sunburst(
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    z_axis: str,
    coloring_field_inner: str,
    coloring_field_outer: str,
    labels_color_inner: str,
    labels_color_outer: str,
    labels_hide_percent: int = 1,
    pie_borders: bool = False,
    labels_spec: Optional[Dict[str, Any]] = None,
    size: Tuple[int, int] = (500, 500),
    show_plot: bool = True,
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
    ax = draw_plot_plotly()

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
        inner_outer_links,
    ) = calculate_labels_nested(x_values, y_values, z_values)

    all_labels = inner_labels + outer_labels
    all_parents = [""] * len(inner_labels) + inner_outer_links
    all_counts = inner_labels_count + outer_labels_count
    labels_display = hide_text_keep_slice_fmt(
        all_labels=all_labels,
        all_counts=all_counts,
        inner_labels_count=inner_labels_count,
        labels_hide_percent=labels_hide_percent,
    )

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
    fig = draw_sunburst(
        ax=ax,
        all_labels=all_labels,
        all_parents=all_parents,
        all_counts=all_counts,
        formatted_texts=labels_display,
    )
    fig.update_layout(
        title={
            "text": labels_spec.get("title", ""),
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
        margin=dict(t=60, l=0, r=0, b=0),
        width=size[0],
        height=size[1],
    )

    color_sunburst(
        ax=fig,
        coloring_values=all_labels,
        colors_map=full_colors_map,
        border=pie_borders,
    )
    color_sunburst_labels(
        ax=fig,
        color=labels_color_inner,
        target="inner",
    )
    color_sunburst_labels(
        ax=fig,
        color=labels_color_outer,
        target="outer",
    )

    ### font ###
    font_apply_plot(
        ax=fig,
        fonts=FONTS_PLOT,
    )

    ### output
    legends = None
    extra_artists = None
    if show_plot:
        show_plot_plotly(fig)
    else:
        return fig, legends, extra_artists


def sankey(
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    z_axis: str,
    nodes_pad: int,
    nodes_thickness: int,
    links_color: str,
    links_opacity: float,
    labels_color: str,
    labels_spec: Optional[Dict[str, Any]] = None,
    size: Tuple[int, int] = (500, 500),
    show_plot: bool = True,
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
    ax = draw_plot_plotly()

    ### plot_get
    column1 = [r[0] for r in dataset_counted[x_axis]]
    column2 = [r[0] for r in dataset_counted[y_axis]]
    column3 = [r[0] for r in dataset_counted[z_axis]]
    counts = dataset_counted["count"]

    (
        labels,
        sources,
        targets,
        values,
    ) = calculate_sankey_flows(column1, column2, column3, counts)

    colors_1 = get_colors_map(
        colors=COLORS,
        coloring_field=x_axis,
    )
    colors_2 = get_colors_map(
        colors=COLORS,
        coloring_field=y_axis,
    )
    colors_3 = get_colors_map(
        colors=COLORS,
        coloring_field=z_axis,
    )
    full_colors_map = {**colors_1, **colors_2, **colors_3}

    ### plot_draw
    fig = draw_sankey(
        ax=ax,
        labels=labels,
        sources=sources,
        targets=targets,
        values=values,
    )
    fig.update_layout(
        margin=dict(t=70, l=10, r=10, b=10),
        width=size[0],
        height=size[1],
    )

    titles = ["title1", "title2", "title3"]
    x_positions = [0.0, 0.5, 1.0]
    anchors = ["left", "center", "right"]
    for t_key, x_p, anchor in zip(titles, x_positions, anchors):
        if labels_spec.get(t_key):
            fig.add_annotation(
                x=x_p,
                y=1.10,
                text=labels_spec[t_key],
                showarrow=False,
                xref="paper",
                yref="paper",
                xanchor=anchor,
                name="sankey_header",
            )

    color_sankey_nodes(
        ax=fig,
        labels_list=labels,
        colors_map=full_colors_map,
        pad=nodes_pad,
        thickness=nodes_thickness,
    )
    color_sankey_links(
        ax=fig,
        color=links_color,
        opacity=links_opacity,
    )
    color_sankey_labels(
        ax=fig,
        color=labels_color,
    )

    ### font ###
    font_apply_plot(
        ax=fig,
        fonts=FONTS_PLOT,
    )

    ### output
    legends = None
    extra_artists = None
    if show_plot:
        show_plot_plotly(fig)
    else:
        return fig, legends, extra_artists


def worldmap(
    dataset: Dict,
    fields: List[str],
    filter_values: Optional[List[str]],
    filter_count: Optional[str],
    x_axis: str,
    y_axis: str,
    labels_color: str,
    cmap: str = "YlOrRd",
    borders: bool = True,
    frame: bool = True,
    labels_spec: Optional[Dict[str, Any]] = None,
    size: Tuple[int, int] = (500, 500),
    show_plot: bool = True,
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
    ax = draw_plot_plotly()

    ### plot_get
    x_values, y_values, z_values = get_labels(
        dataset=dataset_counted,
        x_axis=x_axis,
        y_axis=y_axis,
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

    ### plot_draw
    fig = draw_map(
        ax=ax,
        countries=corrected_values,
        counts=y_values,
    )
    fig.update_layout(
        title={
            "text": labels_spec.get("title", ""),
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
        margin=dict(t=60, l=0, r=0, b=0),
        width=size[0] if size[0] else None,
        height=size[1] if size[1] else None,
        geo={
            "projection": {"type": "natural earth"},
        },
    )

    legend_cbar = legend_create_mapbar(
        ax=fig,
        title="",
    )

    color_map(
        ax=fig,
        cmap=cmap,
        border=borders,
        frame=frame,
    )
    color_map_labels(
        ax=fig,
        color=labels_color,
    )

    ### font ###
    font_apply_plot(
        ax=fig,
        fonts=FONTS_PLOT,
    )
    font_apply_legend(
        legend=legend_cbar,
        fonts=FONTS_LEGEND,
    )

    ### output
    legends = None
    extra_artists = None
    if show_plot:
        show_plot_plotly(fig)
    else:
        return fig, legends, extra_artists


def prisma(
    dataset: Dict,
    fields: List[str],
    filter_seq: Optional[List[Dict[str, Any]]],
    manual_values: Dict[str, int],
    labels_spec: Dict[str, str],
    flow_config: List[Dict[str, Any]],
    notes_config: Optional[List[Dict[str, Any]]],
    style_groups: Optional[Dict[str, List[str]]],
    save_name: Optional[str] = None,
):
    dataset_with_id = add_dataset_id(
        dataset=dataset,
        field="id",
    )

    ### operation
    dataset_filtered = filter_dataset_by_fields(
        dataset=dataset_with_id,
        fields=["id"] + fields,
    )
    dataset_counted = count_dataset(
        dataset=dataset_filtered,
        fields=["id"] + fields,
    )

    n_eligible = get_unique_count(dataset=dataset_counted, field="id")
    calculated_values = {"eligible": n_eligible}
    dataset_running = dataset_counted

    if filter_seq:
        for step in filter_seq:
            key = step.get("key")
            filter_str = step.get("filter")

            field, values, operation = parse_string(text=filter_str)
            dataset_running = filter_dataset_by_values(
                dataset=dataset_running,
                field=field,
                values=values,
                include=operation,
            )

            count = get_unique_count(dataset=dataset_running, field="id")
            calculated_values[key] = count

    all_values = {**manual_values, **calculated_values}

    ### output
    for i in all_values:
        print(f"{i}: {all_values[i]}")

    name = save_name
    dot = draw_plot_graphviz(
        name=name,
        position="TB",
        splines="polyline",
        nodesep="0.45",
        ranksep="0.72",
    )

    formatted_nodes = {}
    for key, text_template in labels_spec.items():
        try:
            # This replaces {search} in string with 614, etc.
            formatted_nodes[key] = text_template.format(**all_values)
        except KeyError:
            # Fallback for note nodes that don't have numbers
            formatted_nodes[key] = text_template

    ### plot_draw
    draw_prisma_nodes(
        dot=dot,
        nodes=formatted_nodes,
    )

    ### plot_style
    if style_groups:
        for style_key, nodes in style_groups.items():
            if style_key in STYLE_PRISMA:
                style_prisma(
                    ax=dot,
                    config=STYLE_PRISMA[style_key],
                    nodes=nodes,
                )

    style_prisma(
        ax=dot,
        config=STYLE_PRISMA["edge_flow"],
    )
    draw_prisma_edges(
        dot=dot,
        edges=flow_config,
    )

    if notes_config:
        style_prisma(
            ax=dot,
            config=STYLE_PRISMA["edge_note"],
        )
        draw_prisma_edges(
            dot=dot,
            edges=notes_config,
        )

    ### output ###
    legends = None
    extra_artists = None
    if save_name:
        show_plot_graphviz(dot=dot)
        save_plot_graphviz(
            dot=dot,
            name=name,
        )
    else:
        return dot, legends, extra_artists
