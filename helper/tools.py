from itertools import product


def get_field_values(data, field_indices):
    field_values_dict = []

    for record in data:
        field_value_list = []

        for idx in field_indices:
            field_value_list.append(record[idx])

        field_values_dict.append(tuple(field_value_list))

    return field_values_dict


def map_field_values(dict, map, map_index):
    mapped_dict = []

    for record in dict:
        record_as_list = list(record)
        record_as_list[map_index] = map.get(
            record_as_list[map_index], record_as_list[map_index]
        )

        mapped_dict.append(tuple(record_as_list))

    return mapped_dict


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
