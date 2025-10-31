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
                dataset[field].append(row.get(field, ""))

    return dataset


def map_dataset(dataset, field, map):
    dataset_mapped = {}

    for column in dataset:
        dataset_mapped[column] = list(dataset[column])

    if field in dataset_mapped:
        dataset_mapped[field] = [
            map.get(value, value) for value in dataset_mapped[field]
        ]

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
            value = dataset.get(name, [""])[i]
            tokens = [t.strip() for t in str(value).split(";") if t.strip()]
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
