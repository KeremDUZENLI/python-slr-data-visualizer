def print_dict(dict):
    for field, values in dict.items():
        print(field)
        print(values)
        print()


def print_counts(dataset, decimal=0):
    field_names, rows = _prepare_count_rows(dataset)
    total_records = sum(row["count"] for row in rows)
    widths, total_width = _compute_label_widths(field_names, rows)

    for row in rows:
        line = _format_row(
            labels=row["labels"],
            widths=widths,
            count=row["count"],
            total_records=total_records,
            decimal=decimal,
        )
        print(line)

    print("-" * total_width)

    label = "TOTAL COUNTS"
    padded_label = label.ljust(total_width)
    print(padded_label + " : " + str(total_records))
    print()


def _prepare_count_rows(dataset):
    field_names = []
    for key in dataset.keys():
        if key != "count":
            field_names.append(key)

    counts = dataset["count"]

    rows = []
    for i in range(len(counts)):
        labels = []
        for name in field_names:
            labels.append(dataset[name][i])

        rows.append({"labels": labels, "count": counts[i]})

    return field_names, rows


def _compute_label_widths(field_names, rows, min_total_width=20, separator=" | "):
    num_columns = len(field_names)
    widths = [0] * num_columns

    for column in range(num_columns):
        max_len = len(str(field_names[column]))

        for row in rows:
            value = row["labels"][column]
            text = _format_label_value(value)
            length = len(text)
            if length > max_len:
                max_len = length

        widths[column] = max_len

    total_width = 0
    for w in widths:
        total_width += w
    total_width += len(separator) * (num_columns - 1)

    if total_width < min_total_width:
        difference = min_total_width - total_width
        widths[-1] = widths[-1] + difference
        total_width = min_total_width

    return widths, total_width


def _format_row(labels, widths, count, total_records, decimal, separator=" | "):
    row = ""

    for i in range(len(labels)):
        text = _format_label_value(labels[i])
        pad = widths[i] - len(text)
        row += text + (" " * pad)

        if i < len(labels) - 1:
            row += separator

    if total_records > 0:
        percent = (count / total_records) * 100
    else:
        percent = 0

    row += f" : {count:<3} ({percent:.{decimal}f}%)"
    return row


def _format_label_value(value):
    return "; ".join(str(v) for v in value)
