def create_empty_dataset(fields):
    dataset = {}
    for field in fields:
        dataset[field] = []

    return dataset


def get_num_rows(dataset):
    for field in dataset:
        return len(dataset[field])
