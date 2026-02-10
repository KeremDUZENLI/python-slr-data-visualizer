from helper.helper import (
    create_empty_dataset,
    get_num_rows,
)


def group_dataset_by_fields(datasets, stack_by, axes):
    dataset_grouped = create_empty_dataset(axes)

    for dataset, mapping in datasets:
        row_count = get_num_rows(dataset)

        for i in range(row_count):
            for ax in axes:
                if ax in stack_by:
                    base_key = stack_by[ax]
                    label = mapping.get(base_key, base_key)
                    dataset_grouped[ax].append([label])
                    continue

                src = mapping.get(ax, "")
                dataset_grouped[ax].append(dataset[src][i])

    return dataset_grouped


def map_dataset_column(dataset, field_from, field_to, mapping):
    all_fields = list(dataset.keys())
    if field_to not in all_fields:
        all_fields.append(field_to)

    dataset_mapped_by_col = create_empty_dataset(all_fields)

    for key in dataset:
        if key == field_to:
            continue

        for value in dataset[key]:
            dataset_mapped_by_col[key].append(value)

    if field_from in dataset:
        for row in dataset[field_from]:
            mapped_row = []
            for value in row:
                mapped_row.append(mapping.get(value, value))

            dataset_mapped_by_col[field_to].append(mapped_row)

    return dataset_mapped_by_col


def map_dataset_hierarchy(dataset, field_parent, field_child, mapping):
    dataset_mapped_by_hier = create_empty_dataset([field_parent, field_child])
    rows = get_num_rows(dataset)

    for i in range(rows):
        parents = dataset[field_parent][i]  # ['3D Scanning','Image-Based Techniques'..]
        children = dataset[field_child][i]  # ['Laser Scanning','Photogrammetry'..]

        # iterate every parent token in that row
        for parent in parents:
            allowed_children = mapping.get(parent, [])

            # if mapping has no allowed children for this parent, skip
            if not allowed_children:
                continue

            # for every child token in the row, if it is allowed, append pair
            for child in children:
                if child in allowed_children:
                    dataset_mapped_by_hier[field_parent].append([parent])
                    dataset_mapped_by_hier[field_child].append([child])

    return dataset_mapped_by_hier
