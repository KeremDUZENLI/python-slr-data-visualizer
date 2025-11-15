from ._0_helpers import (
    create_empty_dataset,
)
import csv


def read_dataset(csv_path):
    with open(csv_path, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        dataset = create_empty_dataset(fields)

        for row in reader:
            for field in fields:
                cell = row.get(field, "")
                tokens = _tokenize_cell(cell)
                dataset[field].append(tokens)

    return dataset


def _tokenize_cell(cell):
    text = str(cell)
    parts = text.split(";")

    tokens = []
    for part in parts:
        value = part.strip()
        if value != "":
            tokens.append(value)

    if tokens == []:
        return [""]

    return tokens
