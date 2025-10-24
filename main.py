from config.maps import regions
from src.tools import get_field_values, map_field_values

csv_path = "data/dataset.csv"
field_names = ["year", "country", "historical_site_type"]

field_values = get_field_values(csv_path, field_names)
print(field_values)

mapped_values = map_field_values(field_values, field_names, "country", regions)
print(mapped_values)

# field_values_dict = get_field_values(data, [1, 2, 4])
# map_field_values_dict = map_field_values(field_values_dict, country_to_region, 1)
# field_values_count = count_field_values(map_field_values_dict, [0, 1, 2])

# print_field_values_count(field_values_dict, field_values_count)

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


# helper/io.py
