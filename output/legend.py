import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def plot_legend(colors, grp_axis, values, loc, pos):
    palette = colors[grp_axis]
    handles = []

    for value in values:
        color = palette.get(value)
        if color:
            handles.append(
                Patch(
                    facecolor=color,
                    edgecolor="none",
                    label=value,
                )
            )

    return plt.legend(
        handles=handles,
        title=_clean_label(grp_axis),
        loc=loc,
        bbox_to_anchor=pos,
    )


def _clean_label(name):
    return str(name).replace("_", " ").strip().title()
