from helper.helper import (
    create_empty_dataset,
    get_num_rows,
)
from itertools import product


def count_dataset(dataset, fields):
    counts = _build_counts(dataset, fields)
    dataset_counted = _counts_to_dataset(fields, counts)
    return dataset_counted


def get_unique_count(dataset, field):
    all_ids = []

    if field in dataset:
        for cell in dataset[field]:
            if len(cell) > 0:
                all_ids.append(cell[0])

    return len(set(all_ids))


def _build_counts(dataset, fields):
    counts = {}
    num_rows = get_num_rows(dataset)

    for row_index in range(num_rows):
        token_lists = _get_token_lists_for_row(dataset, fields, row_index)

        for combo in product(*token_lists):
            if combo in counts:
                counts[combo] += 1
            else:
                counts[combo] = 1

    return counts


def _get_token_lists_for_row(dataset, fields, row_index):
    token_lists = []

    for field in fields:
        values = dataset[field][row_index]

        if values == []:
            values = [""]

        token_lists.append(values)

    return token_lists


def _counts_to_dataset(fields, counts):
    dataset_counted = create_empty_dataset(fields + ["count"])
    sorted_combos = sorted(counts.keys())

    for combo in sorted_combos:
        for index in range(len(fields)):
            field = fields[index]
            value = combo[index]
            dataset_counted[field].append([value])

        dataset_counted["count"].append(counts[combo])

    return dataset_counted
