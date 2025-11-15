from output._0_helpers import (
    format_label_value,
)


COLORS = {
    "year": {
        "2020": "#35b85e",
        "2021": "#ff7f0e",
    },
    "study_focus": {
        "Reconstruction": "#1f77b4",
        "Restoration": "#2ca02c",
        "Visualization": "#d62728",
    },
    "historical_site_type": {
        "Archaeological Site": "#6aa84f",
        "Artistic Feature": "#f6b26b",
        "Building": "#4a86e8",
        "Natural Space": "#8e7cc3",
    },
    "software_category": {
        "software_data": "#0000ff",
        "software_modeling": "#008000",
        "software_render": "#ff0000",
    },
    "software": {
        "Agisoft Metashape": "#c4deed",
        "Autodesk ReCap": "#72aad2",
        "Autodesk 3ds Max": "#c6e7c1",
        "Blender": "#72bc87",
        "Unity": "#fcbca7",
        "Unreal Engine": "#eb6d67",
    },
}


def prepare_data_1D(dataset, x_axis, y_axis):
    x_raw = dataset[x_axis]
    y_raw = dataset[y_axis]

    x_values = []
    y_values = []

    for x_label, value in zip(x_raw, y_raw):
        if x_label in x_values:
            index = x_values.index(x_label)
            y_values[index] += value
        else:
            x_values.append(x_label)
            y_values.append(value)

    return x_values, y_values


def color_heatmap(base_color, min_alpha, max_alpha):
    return {
        "base_color": base_color,
        "min_alpha": min_alpha,
        "max_alpha": max_alpha,
    }


def get_colors_map(field, values):
    colors_map = {}

    for value in values:
        value_str = format_label_value(value)
        color = _get_color(field, value)
        colors_map[value_str] = color

    return colors_map


def _get_color(field, value):
    if field not in COLORS:
        return None

    value_str = format_label_value(value)
    colors_dict = COLORS[field]
    if value_str in colors_dict:
        return colors_dict[value_str]

    return None
