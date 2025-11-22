from helper.helper import (
    get_unique_values,
)


def get_labels(dataset, x_axis, y_axis=None, z_axis=None):
    x_raw = dataset[x_axis]
    y_raw = dataset[y_axis] if y_axis else None
    z_raw = dataset[z_axis] if z_axis else None

    x_values = []
    y_values = [] if y_axis else None
    z_values = [] if z_axis else None

    n = len(x_raw)
    for i in range(n):
        x_val = _extract_value(x_raw[i])
        x_values.append(x_val)

        if y_axis:
            y_val = _extract_value(y_raw[i])
            y_values.append(y_val)

        if z_axis:
            z_val = _extract_value(z_raw[i])
            z_values.append(z_val)

    if y_axis and z_axis:
        return x_values, y_values, z_values
    if y_axis:
        return x_values, y_values
    return x_values


def get_labels_extra(values):
    unique_values = get_unique_values(values)

    positions = {}
    for item in unique_values:
        positions[item] = []

    for i in range(len(values)):
        positions[values[i]].append(i)

    values_centers = {}
    for item in positions:
        total = 0
        count = len(positions[item])
        for index in positions[item]:
            total += index
        values_centers[item] = total / count

    return values_centers


def _extract_value(cell):
    if isinstance(cell, list) and len(cell) == 1:
        return cell[0]
    return cell
