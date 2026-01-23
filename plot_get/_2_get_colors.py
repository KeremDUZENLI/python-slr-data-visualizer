def get_colors_map(values, colors, color_field):
    colors_map = {}

    for value in values:
        color = _get_color(value, colors, color_field)
        colors_map[value] = color

    return colors_map


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


def _get_color(value, colors, color_field):
    if color_field not in colors:
        return None

    colors_dict = colors[color_field]
    if value in colors_dict:
        return colors_dict[value]

    return None
