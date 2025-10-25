import csv
from itertools import product


def read_csv(csv_path):
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


def map_csv(dataset, fields, maps):
    dataset_mapped = {}

    for field in dataset:
        dataset_mapped[field] = list(dataset[field])

    for i, field in enumerate(fields):
        if field in dataset_mapped:
            mapping = maps[i]
            dataset_mapped[field] = [
                mapping.get(value, value) for value in dataset_mapped[field]
            ]

    return dataset_mapped


def filter_fields(dataset, fields):
    dataset_filtered = {}

    for field in fields:
        if field in dataset:
            dataset_filtered[field] = list(dataset[field])

    return dataset_filtered


def count_fields(dataset, fields):
    counts = {}
    rows = len(next(iter(dataset.values()), []))

    for record in range(rows):
        values_per_field = _expand_field_values(dataset, fields, record)

        for combo in product(*values_per_field):
            counts[combo] = counts.get(combo, 0) + 1

    return [combo + (count,) for combo, count in counts.items()]


def _expand_field_values(dataset, fields, index):
    values_per_field = []

    for name in fields:
        val = dataset.get(name, [""])[index]

        if isinstance(val, (list, tuple)):
            values_per_field.append(tuple(val))
        else:
            values_per_field.append((val,))

    return values_per_field
