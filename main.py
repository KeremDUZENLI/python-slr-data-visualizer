from config.maps import regions
from src.tools import read_dataset, map_dataset, filter_dataset, count_dataset
from output.print import print_counts

dataset = read_dataset(
    csv_path="data/dataset.csv",
)

dataset_mapped = map_dataset(
    dataset=dataset,
    field="country",
    map=regions,
)

dataset_filtered = filter_dataset(
    dataset=dataset_mapped,
    fields=["year", "country", "historical_site_type"],
)

dataset_counts = count_dataset(
    dataset=dataset_filtered,
    fields=["year", "historical_site_type"],
)


print_counts(dataset_counts)


# plot_chart_bar(
#     field_values_count,
#     0,
#     2,
#     "Year",
#     "Number of Publications",
#     "Timeline of Publications by Historical Site Categories (2015-2024)",
# )

# x, y, z = prepare_grouped_data(field_values_count, 0, 2, 1)
# print(x)
