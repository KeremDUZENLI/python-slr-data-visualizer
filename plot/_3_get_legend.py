import matplotlib.patches as Patch


def get_legend_handles(values, colors_map):
    handles = []
    seen = set()

    for value in values:
        if value in seen:
            continue
        seen.add(value)

        color = colors_map.get(value)
        patch = Patch.Patch(
            facecolor=color, edgecolor="none", label=_clean_label(value)
        )
        handles.append(patch)

    return handles


def _clean_label(name):
    return str(name).replace("_", " ").strip().title()
