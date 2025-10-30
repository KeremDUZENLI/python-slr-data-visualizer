def print_counts(dataset, decimal=0):
    field_names = [k for k in dataset.keys() if k != "count"]
    total_records = sum(dataset["count"])

    rows = []
    for i in range(len(dataset["count"])):
        labels = [dataset[name][i] for name in field_names]
        count = dataset["count"][i]
        rows.append(tuple(labels + [count]))

    width_columns, width_max = _compute_width_columns_counts(rows)
    rows_sorted = sorted(rows, key=lambda x: str(x[:-1]).lower())

    for row in rows_sorted:
        labels = row[:-1]
        count = row[-1]
        print(_format_rows_counts(labels, width_columns, count, total_records, decimal))

    print("-" * width_max)
    print(f"{'TOTAL FIELD VALUES'.ljust(width_max)} : {total_records}\n\n\n")


def _compute_width_columns_counts(rows):
    columns = []
    for row in rows:
        columns.append(row[:-1])

    if columns:
        columns_new = list(zip(*columns))
    else:
        columns_new = []

    width_columns = []
    for column in columns_new:
        width_max = 0
        for item in column:
            l = len(str(item))
            if l > width_max:
                width_max = l
        width_columns.append(width_max)

    width_total_min = 20
    if not width_columns:
        width_columns = [width_total_min]

    width_sum = 0
    for w in width_columns:
        width_sum += w

    width_max = width_sum + 3 * (len(width_columns) - 1)
    if width_max < width_total_min:
        width_columns[-1] += width_total_min - width_max
        width_max = width_total_min

    return width_columns, width_max


def _format_rows_counts(labels, widths, count, total_records, decimal=0):
    row = ""
    for i in range(len(labels)):
        item_str = str(labels[i])
        padding = widths[i] - len(item_str)
        row += f"{item_str}{' ' * padding}"
        if i < len(labels) - 1:
            row += " | "

    percent = (count / total_records * 100) if total_records else 0
    row += f" : {count:<3} ({percent:.{decimal}f}%)"
    return row
