def get_colors_map(colors, coloring_field):
    if coloring_field in colors:
        return colors[coloring_field]

    return {}


def get_color_heatmap(base_color, min_alpha, max_alpha):
    return {
        "base_color": base_color,
        "min_alpha": min_alpha,
        "max_alpha": max_alpha,
    }


def map_colors_map(colors_from, colors_to, colors_map):
    colors_mapped = {}

    for key, ref_val in zip(colors_from, colors_to):
        color = colors_map.get(ref_val)
        colors_mapped[key] = color

    return colors_mapped
