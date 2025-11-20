def get_color_heatmap(base_color, min_alpha, max_alpha):
    return {
        "base_color": base_color,
        "min_alpha": min_alpha,
        "max_alpha": max_alpha,
    }


def get_colors_map(values, criteria, colors, color_field):
    colors_map = {}

    for i, val in enumerate(values):
        value = criteria[i]
        color = _get_color(value, colors, color_field)
        colors_map[val] = color

    return colors_map


def _get_color(value, colors, color_field):
    if color_field not in colors:
        return None

    colors_dict = colors[color_field]
    if value in colors_dict:
        return colors_dict[value]

    return None
