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


def map_dataset_column(dataset, field, mapping):
    dataset_mapped = create_empty_dataset(dataset.keys())

    # Copy unchanged fields
    for key in dataset:
        if key != field:
            for value in dataset[key]:
                dataset_mapped[key].append(value)

    # Map the specified field
    if field in dataset:
        for row in dataset[field]:
            mapped_row = []
            for value in row:
                mapped_row.append(mapping.get(value, value))
            dataset_mapped[field].append(mapped_row)

    return dataset_mapped


def map_dataset_hierarchy(dataset, field_parent, field_child, mapping):
    dataset_mapped = create_empty_dataset([field_parent, field_child])
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
                    dataset_mapped[field_parent].append([parent])
                    dataset_mapped[field_child].append([child])

    return dataset_mapped
