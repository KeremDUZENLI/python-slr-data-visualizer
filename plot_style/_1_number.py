def number_bar(ax, orientation="v", offset=1):
    for rect in ax.patches:

        if orientation == "v":
            height = rect.get_height()
            if height <= 0:
                continue

            x = (rect.get_x()) + (rect.get_width() / 2)
            y = (rect.get_y() + height) + (offset * 0.1)
            ha = "center"
            va = "bottom"

        if orientation == "h":
            height = rect.get_width()
            if height <= 0:
                continue

            x = (rect.get_x() + height) + (offset * 0.1)
            y = (rect.get_y()) + (rect.get_height() / 2)
            ha = "left"
            va = "center"

        ax.text(
            x,
            y,
            str(int(height)),
            ha=ha,
            va=va,
            gid="labels_height_numbers",
        )


def number_area(ax, offset=0):
    for poly in ax.collections:
        paths = poly.get_paths()

        if not paths:
            continue

        points = {}
        for x, y in paths[0].vertices:
            points.setdefault(round(x), []).append(y)

        for x_val, y_list in points.items():
            if len(y_list) < 2:
                continue

            y_top, y_bot = max(y_list), min(y_list)
            height = y_top - y_bot

            if height < 0.1:
                continue

            x = x_val
            y = y_top + (offset * 0.1)

            ax.text(
                x,
                y,
                str(int(height)),
                ha="center",
                va="bottom",
                gid="labels_height_numbers",
            )


def number_heatmap(ax, matrix):
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            value = matrix[row, col]
            ax.text(
                col,
                row,
                str(int(value)),
                ha="center",
                va="center",
                gid="labels_heatmap_numbers",
            )


def add_labels_extra(ax, labels_center, orientation="v", offset=15):
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


def add_grid(ax, orientation="v"):
    ax.set_axisbelow(True)
    if orientation == "v":
        ax.yaxis.grid(visible=True, linestyle="--", linewidth=0.7, alpha=0.7)
    if orientation == "h":
        ax.xaxis.grid(visible=True, linestyle="--", linewidth=0.7, alpha=0.7)
