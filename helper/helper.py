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


def calculate_labels_center_bar(values):
    unique_values = get_unique_values(values)

    positions = {}
    for item in unique_values:
        positions[item] = []

    for i in range(len(values)):
        positions[values[i]].append(i)

    labels_center = {}
    for item in positions:
        total = 0
        count = len(positions[item])
        for index in positions[item]:
            total += index
        labels_center[item] = total / count

    return labels_center


def calculate_labels_center_pie(inner_radius, outer_radius):
    labels_center = (inner_radius + outer_radius) / (2 * outer_radius)
    return labels_center


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
