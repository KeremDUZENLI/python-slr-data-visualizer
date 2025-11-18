import matplotlib.patches as Patch


def create_legend(values, colors_map):
    handles = []

    for value in values:
        color = colors_map.get(value)
        patch = Patch.Patch(facecolor=color, edgecolor="none", label=value)
        handles.append(patch)

    return handles
