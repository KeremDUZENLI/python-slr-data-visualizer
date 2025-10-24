import csv
from itertools import product


def get_field_values(csv_path, field_names):
    field_values_list = []

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            values = []
            for name in field_names:
                values.append(row.get(name, ""))
            field_values_list.append(tuple(values))

    return field_values_list


def map_field_values(field_values_list, field_names, field_mapping, map):
    mapped_list = []

    map_index = field_names.index(field_mapping)

    for record in field_values_list:
        record_as_list = list(record)
        record_as_list[map_index] = map.get(
            record_as_list[map_index], record_as_list[map_index]
        )
        mapped_list.append(tuple(record_as_list))

    return mapped_list


def count_field_values(field_values, field_indices=[0]):
    counts = {}

    for record in field_values:
        values_per_field = _expand_field_values(record, field_indices)

        for combo in product(*values_per_field):
            counts[combo] = counts.get(combo, 0) + 1

    return [combo + (count,) for combo, count in counts.items()]


def _expand_field_values(record, field_indices):
    values_per_field = []

    for idx in field_indices:
        val = record[idx]

        if isinstance(val, (list, tuple)):
            values_per_field.append(tuple(val))
        else:
            values_per_field.append((val,))

    return values_per_field
