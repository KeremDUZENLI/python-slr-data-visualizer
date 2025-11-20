def label_numbers(ax, y_values, orientation="v", offset=3, font=None):
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

        if font:
            ax.text(x, y, str(value), ha=ha, va=va, **font)
        else:
            ax.text(x, y, str(value), ha=ha, va=va)
