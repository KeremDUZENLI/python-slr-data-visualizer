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


def map_dataset(dataset, field, map):
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


def filter_dataset(dataset, fields):
    dataset_filtered = {}

    for field in fields:
        if field in dataset:
            dataset_filtered[field] = list(dataset[field])

    return dataset_filtered


def filter_dataset_value(dataset, field, value):
    dataset_filtered = {k: [] for k in dataset}

    rows = len(next(iter(dataset.values()), []))
    for i in range(rows):
        if dataset[field][i] == value:
            for k in dataset:
                dataset_filtered[k].append(dataset[k][i])

    return dataset_filtered


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
