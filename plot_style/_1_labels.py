def labels_bar_numbers(ax, y_values, orientation="v", offset=3):
    for rect, value in zip(ax.patches, y_values):
        if value == 0:
            continue

        if orientation == "v":
            x = rect.get_x() + rect.get_width() / 2
            y = rect.get_height() + offset * 0.1
            ha = "center"
            va = "bottom"
        if orientation == "h":
            x = rect.get_width() + offset * 0.1
            y = rect.get_y() + rect.get_height() / 2
            ha = "left"
            va = "center"

        ax.text(
            x,
            y,
            str(value),
            ha=ha,
            va=va,
            gid="labels_bar_numbers",
        )


def labels_grid(ax, orientation="v"):
    ax.set_axisbelow(True)
    if orientation == "v":
        ax.yaxis.grid(visible=True, linestyle="--", linewidth=0.7, alpha=0.7)
    if orientation == "h":
        ax.xaxis.grid(visible=True, linestyle="--", linewidth=0.7, alpha=0.7)


def labels_extra(ax, labels_center, orientation="v", offset=15):
    texts = []

    for value, center in labels_center.items():
        if orientation == "v":
            x = center
            y = -offset
            rotation = 0
        if orientation == "h":
            x = -offset
            y = center
            rotation = 90

        text = ax.text(
            x=x,
            y=y,
            s=value,
            ha="center",
            va="center",
            rotation=rotation,
            gid="labels_extra",
        )
        texts.append(text)

    return texts
