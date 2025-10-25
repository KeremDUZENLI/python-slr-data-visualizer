from config.maps import regions
from output.print import print_counts
from src.tools import read_csv, map_csv, filter_fields, count_fields

csv_path = "data/dataset.csv"
fields = ["year", "country", "historical_site_type"]

dataset = read_csv(csv_path)
dataset_mapped = map_csv(dataset, ["country"], [regions])
dataset_filtered = filter_fields(dataset_mapped, fields)
dataset_counts = count_fields(dataset, ["year"])

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
