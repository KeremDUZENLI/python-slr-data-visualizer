from helper.helper import (
    get_unique_values,
    clean_label,
)
import matplotlib.patches as Patch


def get_legend_handles(values, colors_map):
    handles = []
    unique_values = get_unique_values(values)

    for value in unique_values:
        color = colors_map.get(value)
        patch = Patch.Patch(facecolor=color, edgecolor="none", label=clean_label(value))
        handles.append(patch)

    return handles
