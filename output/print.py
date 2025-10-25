def print_counts(dataset, decimal=0):
    total_records = _sum_counts(dataset)
    width_columns, width_max = _compute_width_columns_counts(dataset)
    counts_sorted = sorted(dataset, key=lambda x: str(x[:-1]).lower())

    for row in counts_sorted:
        labels = row[:-1]
        count = row[-1]
        print(_format_rows_counts(labels, width_columns, count, total_records, decimal))

    print("-" * width_max)
    print(f"{'TOTAL FIELD VALUES'.ljust(width_max)} : {total_records}")


def _sum_counts(dataset):
    total = 0
    for row in dataset:
        total += row[-1]
    return total


def _compute_width_columns_counts(dataset):
    columns = []
    for row in dataset:
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
