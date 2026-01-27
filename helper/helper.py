def create_empty_dataset(fields):
    dataset = {}
    for field in fields:
        dataset[field] = []

    return dataset


def get_num_rows(dataset):
    for field in dataset:
        return len(dataset[field])


def get_unique_values(values):
    seen = set()
    unique_values = []

    for value in values:
        if value not in seen:
            seen.add(value)
            unique_values.append(value)

    return unique_values


def calculate_labels_nested(x_values, y_values, z_values):
    tree = {}

    for parent, value, child in zip(x_values, y_values, z_values):
        if parent not in tree:
            tree[parent] = []
        tree[parent].append((child, value))

    inner_labels = []
    inner_labels_count = []
    outer_labels = []
    outer_labels_count = []
    inner_outer_links = []

    for parent in tree.keys():
        child_list = tree[parent]
        parent_total = 0

        for child, value in child_list:
            outer_labels.append(child)
            outer_labels_count.append(value)
            inner_outer_links.append(parent)
            parent_total += value

        inner_labels.append(parent)
        inner_labels_count.append(parent_total)

    return (
        inner_labels,
        inner_labels_count,
        outer_labels,
        outer_labels_count,
        inner_outer_links,
    )


def calculate_sankey_flows(column1, column2, column3, counts):
    column1_uniques = get_unique_values(column1)
    column2_uniques = get_unique_values(column2)
    column3_uniques = get_unique_values(column3)

    labels = column1_uniques + column2_uniques + column3_uniques

    offset2 = len(column1_uniques)
    offset3 = len(column1_uniques) + len(column2_uniques)

    map1 = {v: i for i, v in enumerate(column1_uniques)}
    map2 = {v: i + offset2 for i, v in enumerate(column2_uniques)}
    map3 = {v: i + offset3 for i, v in enumerate(column3_uniques)}

    sources = []
    targets = []
    values = []

    for v1, v2, v3, count in zip(column1, column2, column3, counts):

        # Link 1: Left -> Mid
        sources.append(map1[v1])
        targets.append(map2[v2])
        values.append(count)

        # Link 2: Mid -> Right
        sources.append(map2[v2])
        targets.append(map3[v3])
        values.append(count)

    return (
        labels,
        sources,
        targets,
        values,
    )


def calculate_labels_pos_bar(values, distance=5):
    unique_values = get_unique_values(values)
    chart_center = (len(values) - 1) / 2
    total_space_between = (len(unique_values) - 1) * distance

    start_pos = chart_center - (total_space_between / 2)
    labels_center = {}

    for i, label in enumerate(unique_values):
        position = start_pos + (i * distance)
        labels_center[label] = position

    return labels_center


def calculate_labels_pos_pie(inner_radius, outer_radius):
    labels_center = (inner_radius + outer_radius) / (2 * outer_radius)
    return labels_center


def offset_frame(ax, height, orientation, offset=1):
    max_height = max(height)
    change = max_height * (1 + (offset * 0.1))

    if orientation == "v":
        if max_height > 0:
            ax.set_ylim(0, change)

    if orientation == "h":
        if max_height > 0:
            ax.set_xlim(0, change)


def format_labels(values, decimal=0):
    state = {"index": -1}

    def fmt(pct):
        state["index"] += 1
        if state["index"] < len(values):
            label = values[state["index"]]
            return f"{label}\n{pct:.{decimal}f}%"

    return fmt


def parse_string(text):
    operators = ["==", "!=", ">=", ">", "<=", "<", "="]
    found_op = None

    for operation in operators:
        if operation in text:
            found_op = operation
            break

    left, right = text.split(found_op, 1)
    field = left.strip()
    right = right.strip()
    values_raw = [v.strip() for v in right.split(",")]

    values = []
    for v in values_raw:
        if v in ("''", '""'):
            values.append("")
        else:
            values.append(v)

    if len(values) == 1 and values[0] == "":
        values = [""]

    if found_op == "==":
        operation = True
    elif found_op == "!=":
        operation = False
    else:
        operation = found_op

    return field, values, operation
