from src.tools import read_dataset, count_dataset
from output.plot import plot_chart_bar, plot_chart_bar_group
from output.print import print_counts


dataset = read_dataset(
    csv_path="data/dataset.csv",
)

##### X:Year | Y:Count
dataset_counted_year = count_dataset(
    dataset=dataset,
    fields=["year"],
)

print_counts(
    dataset=dataset_counted_year,
    decimal=0,
)

plot_chart_bar(
    dataset=dataset_counted_year,
    x_axis="year",
    y_axis="count",
    x_label="Year",
    y_label="Number of Publications",
    title="Timeline of Publications (2015-2024)",
)

##### X:Year_HST | Y:Count
dataset_counted_year_hst = count_dataset(
    dataset=dataset,
    fields=["year", "historical_site_type"],
)

print_counts(
    dataset=dataset_counted_year_hst,
    decimal=0,
)

plot_chart_bar_group(
    dataset=dataset_counted_year_hst,
    x_axis="year",
    y_axis="count",
    group_axis="historical_site_type",
    x_label="Year",
    y_label="Number of Publications",
    title="Timeline of Publications by Historical Site Categories (2015-2024)",
)
