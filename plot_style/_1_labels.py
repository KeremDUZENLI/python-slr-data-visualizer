def labels_bar_numbers(ax, orientation="v", offset=1):
    for rect in ax.patches:

        if orientation == "v":
            value = rect.get_height()
            if value <= 0:
                continue

            x = (rect.get_x()) + (rect.get_width() / 2)
            y = (rect.get_y() + value) + (offset * 0.1)
            ha = "center"
            va = "bottom"

        if orientation == "h":
            value = rect.get_width()
            if value <= 0:
                continue

            x = (rect.get_x() + value) + (offset * 0.1)
            y = (rect.get_y()) + (rect.get_height() / 2)
            ha = "left"
            va = "center"

        ax.text(
            x,
            y,
            str(int(value)),
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
