def get_labels(dataset, x_axis, y_axis, z_axis=None):
    x_raw = dataset[x_axis]
    y_raw = dataset[y_axis]
    z_raw = dataset[z_axis] if z_axis else None

    x_values = []
    y_values = []
    z_values = [] if z_axis else None

    for i in range(len(x_raw)):
        x_val = _extract_value(x_raw[i])
        y_val = _extract_value(y_raw[i])
        z_val = _extract_value(z_raw[i]) if z_axis else None

        x_values.append(x_val)
        y_values.append(y_val)
        if z_axis:
            z_values.append(z_val)

    if z_axis:
        return x_values, y_values, z_values

    return x_values, y_values


def _extract_value(cell):
    if isinstance(cell, list) and len(cell) == 1:
        return cell[0]
    return cell
