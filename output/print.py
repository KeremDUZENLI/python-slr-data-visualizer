def print_field_values_count(field_values_list, field_values_freq, decimal=0):
    total_records = len(field_values_list)
    total_field_values = 0
    for row in field_values_freq:
        total_field_values += row[-1]

    width_columns, width_max = _compute_width_columns(field_values_freq)
    sorted_list = sorted(field_values_freq, key=lambda x: str(x[:-1]).lower())

    for row in sorted_list:
        labels = row[:-1]
        count = row[-1]
        print(_format_rows(labels, width_columns, count, total_records, decimal))

    print("-" * (width_max))
    print(f"{'TOTAL RECORDS'.ljust(width_max)} : {total_records}")
    print(f"{'TOTAL FIELD VALUES'.ljust(width_max)} : {total_field_values}")


def _compute_width_columns(field_values_freq):
    columns = []
    for row in field_values_freq:
        columns.append(row[:-1])
    columns_new = list(zip(*columns))

    width_columns = []
    for column in columns_new:
        width_max = max(len(str(item)) for item in column)
        width_columns.append(width_max)

    width_total_min = 20
    width_max = sum(width_columns) + 3 * (len(width_columns) - 1)
    if width_max < width_total_min:
        width_columns[-1] += width_total_min - width_max
        width_max = width_columns[-1]

    return width_columns, width_max


def _format_rows(labels, widths, count, total_records, decimal=0):
    row = ""
    for i in range(len(labels)):
        item_str = str(labels[i])
        padding = widths[i] - len(item_str)
        row += f"{item_str}{' ' * padding}"
        if i < len(labels) - 1:
            row += " | "

    percent = (count / total_records) * 100
    row += f" : {count:<3} ({percent:.{decimal}f}%)"
    return row
