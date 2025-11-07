import csv
from itertools import product


def read_dataset(csv_path):
    dataset = {}

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []

        for field in fields:
            dataset[field] = []

        for row in reader:
            for field in fields:
                cell = row.get(field, "")
                tokens = [t.strip() for t in str(cell).split(";") if t.strip()]
                dataset[field].append(tokens or [""])

    return dataset


def map_dataset_column(dataset, field, map):
    dataset_mapped = {k: list(v) for k, v in dataset.items()}

    if field in dataset_mapped:
        new_col = []
        for value in dataset_mapped[field]:
            if isinstance(value, list):
                new_col.append([map.get(v, v) for v in value])
            else:
                new_col.append(map.get(value, value))

        dataset_mapped[field] = new_col

    return dataset_mapped


def map_dataset_hierarchy(dataset, field_parent, field_child, map):
    dataset_mapped = {field_parent: [], field_child: []}
    rows = len(next(iter(dataset.values()), []))

    for i in range(rows):
        parents = dataset[field_parent][i]
        children = dataset[field_child][i]

        for p in parents:
            allowed = set(map.get(p, []))
            if not allowed:
                continue
            for c in children:
                if c in allowed:
                    dataset_mapped[field_parent].append(p)
                    dataset_mapped[field_child].append(c)

    return dataset_mapped


def filter_dataset_by_field(dataset, fields):
    dataset_filtered = {}

    for field in fields:
        if field in dataset:
            dataset_filtered[field] = list(dataset[field])

    return dataset_filtered


def filter_dataset_by_value(dataset, field, values, include=True):
    dataset_filtered = {k: [] for k in dataset}
    rows = len(next(iter(dataset.values()), []))

    for i in range(rows):
        cell = dataset[field][i]
        tokens = cell if isinstance(cell, list) else [cell]
        has_value = any(t in values for t in tokens)

        if (include and has_value) or (not include and not has_value):
            for key in dataset:
                dataset_filtered[key].append(dataset[key][i])

    return dataset_filtered


def filter_dataset_by_count(dataset, value, comparison):
    dataset_filtered = {k: [] for k in dataset}
    for i, count in enumerate(dataset["count"]):
        if _compare(a=count, b=value, op=comparison):
            for key in dataset:
                dataset_filtered[key].append(dataset[key][i])
    return dataset_filtered


def stack_datasets(datasets, stack_by, axes):
    datasets_stacked = {ax: [] for ax in axes}

    for ds, mapping in datasets:
        count = None
        for ax in axes:
            src = mapping.get(ax, None)
            if isinstance(src, str) and src in ds:
                count = len(ds[src])
                break
        if count is None:
            continue

        for i in range(count):
            for ax in axes:
                if ax in stack_by:
                    base_key = stack_by[ax]
                    label = mapping.get(base_key, base_key)
                    datasets_stacked[ax].append(label)
                    continue

                src = mapping.get(ax, "")
                if isinstance(src, str) and src in ds:
                    datasets_stacked[ax].append(ds[src][i])
                else:
                    datasets_stacked[ax].append(src)

    return datasets_stacked


def count_dataset(dataset, fields):
    counts = {}
    rows = len(next(iter(dataset.values()), []))

    for i in range(rows):
        token_lists = []
        for name in fields:
            values = dataset.get(name, [[""]])[i]
            tokens = values if isinstance(values, list) else [values]
            token_lists.append(tokens or [""])

        for combo in product(*token_lists):
            counts[combo] = counts.get(combo, 0) + 1

    dataset_counted = {name: [] for name in fields}
    dataset_counted["count"] = []

    for combo in sorted(counts.keys(), key=lambda x: str(x).lower()):
        for order, name in enumerate(fields):
            dataset_counted[name].append(combo[order])

        dataset_counted["count"].append(counts[combo])

    return dataset_counted


def _compare(a, b, op):
    if op == ">=":
        return a >= b
    if op == ">":
        return a > b
    if op == "<=":
        return a <= b
    if op == "<":
        return a < b
    if op == "==":
        return a == b
    return False
