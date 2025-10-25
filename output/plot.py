import numpy as np
import matplotlib.pyplot as plt


def plot_chart_bar(field_values_count, x_index, y_index, x_label, y_label, title):
    x_values = [item[x_index] for item in field_values_count]
    y_values = [item[y_index] for item in field_values_count]

    plt.bar(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def prepare_grouped_data(field_values_count, x_index, y_index, group_index):
    x_values_unique = sorted({item[x_index] for item in field_values_count})
    groups = sorted({item[group_index] for item in field_values_count})

    counts_by_year = []
    for x in x_values_unique:
        year_counts = []
        for group in groups:
            count = sum(
                item[y_index]
                for item in field_values_count
                if item[x_index] == x and item[group_index] == group
            )
            year_counts.append(count)
        counts_by_year.append(year_counts)

    return x_values_unique, groups, counts_by_year
