from helper.helper import (
    create_empty_dataset,
    get_num_rows,
)


def filter_dataset_by_fields(dataset, fields):
    filtered = {}

    for field in fields:
        if field in dataset:
            filtered[field] = dataset[field]

    return filtered


def filter_dataset_by_values(dataset, field, values, include=True):
    num_rows = get_num_rows(dataset)
    allowed = set(values)
    dataset_filtered = create_empty_dataset(dataset.keys())

    for i in range(num_rows):
        cell = dataset[field][i]

        if include == True:
            kept = [c for c in cell if c in allowed]
        if include == False:
            kept = [c for c in cell if c not in allowed]

        if not kept:
            continue

        for key in dataset:
            if key == field:
                dataset_filtered[key].append(kept)
            else:
                dataset_filtered[key].append(dataset[key][i])

    return dataset_filtered


def filter_dataset_by_count(dataset, field, value, operation):
    num_rows = get_num_rows(dataset)
    dataset_filtered = create_empty_dataset(dataset.keys())

    for i in range(num_rows):
        cell = dataset[field][i]

        if _compare(cell, value, operation):
            for key in dataset:
                dataset_filtered[key].append(dataset[key][i])

    return dataset_filtered


def _compare(a, b, op):
    if op == ">=":
        return a >= b
    if op == ">":
        return a > b
    if op == "<=":
        return a <= b
    if op == "<":
        return a < b
    if op == "=":
        return a == b
    return False
