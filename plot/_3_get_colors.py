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


def get_color_heatmap(base_color, min_alpha, max_alpha):
    return {
        "base_color": base_color,
        "min_alpha": min_alpha,
        "max_alpha": max_alpha,
    }


def get_colors_map(color_values, color_field):
    colors_map = {}

    for value in color_values:
        color = _get_color(color_field, value)
        colors_map[value] = color

    return colors_map


def _get_color(field, value):
    if field not in COLORS:
        return None

    colors_dict = COLORS[field]
    if value in colors_dict:
        return colors_dict[value]

    return None
