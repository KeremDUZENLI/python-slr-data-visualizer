from ._0_helpers import (
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
