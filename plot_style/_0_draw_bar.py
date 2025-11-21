def draw_bar_1D(ax, x_values, y_values, labels_spec, orientation="v"):
    x_values_list = []
    for x_value in x_values:
        x_values_list.append(str(x_value))

    positions = []
    index = 0
    for _ in x_values_list:
        positions.append(index)
        index += 1

    if orientation == "v":
        for pos, height in zip(positions, y_values):
            ax.bar(pos, height)

        ax.set_xticks(positions)
        ax.set_xticklabels(
            x_values_list, rotation=labels_spec.get("rotation", 0), ha="right"
        )
        ax.set_xlabel(labels_spec.get("x_label", ""))
        ax.set_ylabel(labels_spec.get("y_label", ""))

    if orientation == "h":
        for pos, width in zip(positions, y_values):
            ax.barh(pos, width)

        ax.set_yticks(positions)
        ax.set_yticklabels(x_values_list)
        ax.set_xlabel(labels_spec.get("y_label", ""))
        ax.set_ylabel(labels_spec.get("x_label", ""))
        ax.invert_yaxis()

    ax.set_title(labels_spec.get("title", ""))

    return x_values_list
