from config.data import data
from config.maps import country_to_region
from helper.print import print_field_values_count
from helper.tools import get_field_values, map_field_values, count_field_values


field_values_dict = get_field_values(data, [1, 2, 6])
# print(field_values_dict)

mapped_dict = map_field_values(field_values_dict, country_to_region, 1)
# print(mapped_dict)

field_values_count = count_field_values(mapped_dict, [0, 1, 2])
# print(field_values_count)

print_field_values_count(field_values_dict, field_values_count)
