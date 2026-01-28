from helper.helper import (
    get_unique_values,
)
import matplotlib.patches as Patch
import matplotlib.lines as mlines


def get_legend_handles(values, colors_map):
    handles = []
    unique_values = get_unique_values(values)

    for value in unique_values:
        color = colors_map.get(value)
        patch = Patch.Patch(
            facecolor=color,
            edgecolor="none",
            label=value,
        )
        handles.append(patch)

    return handles


def get_legend_handles_bubble(values, config):
    linecolor = config.get("linecolor")
    marker = config.get("marker")
    facecolor = config.get("facecolor")
    edgecolor = config.get("edgecolor")
    edgewidth = config.get("edgewidth")
    markersize = config.get("markersize")
    opacity = config.get("opacity")

    h1 = mlines.Line2D(
        [],
        [],
        color=linecolor,
        marker=marker,
        markerfacecolor=facecolor,
        markeredgecolor=edgecolor,
        markeredgewidth=edgewidth,
        markersize=markersize[0],
        alpha=opacity,
        label=f"Min: {int(values[0])}",
    )

    h2 = mlines.Line2D(
        [],
        [],
        color=linecolor,
        marker=marker,
        markerfacecolor=facecolor,
        markeredgecolor=edgecolor,
        markeredgewidth=edgewidth,
        markersize=markersize[1],
        alpha=opacity,
        label=f"Max: {int(values[1])}",
    )

    return [h1, h2]
