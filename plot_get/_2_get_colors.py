def get_color_heatmap(base_color, min_alpha, max_alpha):
    return {
        "base_color": base_color,
        "min_alpha": min_alpha,
        "max_alpha": max_alpha,
    }


def get_colors_map(values, colors, color_field):
    colors_map = {}

    for value in values:
        color = _get_color(value, colors, color_field)
        colors_map[value] = color

    return colors_map


def _get_color(value, colors, color_field):
    if color_field not in colors:
        return None

    colors_dict = colors[color_field]
    if value in colors_dict:
        return colors_dict[value]

    return None


def map_colors_map(values_new, values_old, colors_map):
    colors_mapped = {}

    for key, ref_val in zip(values_new, values_old):
        color = colors_map.get(ref_val)
        colors_mapped[key] = color

    return colors_mapped
