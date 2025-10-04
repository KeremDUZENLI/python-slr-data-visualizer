from config.data import data
from config.maps import country_to_region
from helper.plots import plot_chart_bar, prepare_grouped_data
from helper.print import print_field_values_count
from helper.tools import get_field_values, map_field_values, count_field_values


field_values_dict = get_field_values(data, [1, 4])
# print(field_values_dict)

field_values_count = count_field_values(field_values_dict, [0, 1])
print(field_values_count)

# print_field_values_count(field_values_dict, field_values_count)

# plot_chart_bar(
#     field_values_count,
#     0,
#     2,
#     "Year",
#     "Number of Publications",
#     "Timeline of Publications by Historical Site Categories (2015-2024)",
# )

x, y, z = prepare_grouped_data(field_values_count, 0, 2, 1)
print(x)
