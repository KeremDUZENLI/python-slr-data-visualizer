from src.tools import (
    read_dataset,
    filter_dataset_value,
    count_dataset,
)
from output.plot import (
    plot_chart_bar,
    plot_chart_bar_group,
    plot_chart_pie,
    plot_chart_pie_group,
    plot_chart_sunburst,
)
from output.print import print_counts


dataset = read_dataset(
    csv_path="data/dataset.csv",
)

# ### 1_0 ### X:Year | Y:Count
# dataset_counted_year = count_dataset(
#     dataset=dataset,
#     fields=["year"],
# )

# print_counts(
#     dataset=dataset_counted_year,
#     decimal=0,
# )

# plot_chart_bar(
#     dataset=dataset_counted_year,
#     x_axis="year",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications (2015-2024)",
# )

# ### 1_1 ### X:Year_HST | Y:Count
# dataset_counted_year_hst = count_dataset(
#     dataset=dataset,
#     fields=["year", "historical_site_type"],
# )

# print_counts(
#     dataset=dataset_counted_year_hst,
#     decimal=0,
# )

# plot_chart_bar_group(
#     dataset=dataset_counted_year_hst,
#     x_axis="year",
#     y_axis="count",
#     grp_axis="historical_site_type",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications by Historical Site Categories (2015-2024)",
# )


# ### 1_2 ### X:Year_BS | Y:Count
# dataset_value_filtered = filter_dataset_value(
#     dataset=dataset,
#     field="historical_site_type",
#     value="Building",
# )

# dataset_counted_year_bs = count_dataset(
#     dataset=dataset_value_filtered,
#     fields=["year", "historical_site_type_sub"],
# )

# print_counts(
#     dataset=dataset_counted_year_bs,
#     decimal=0,
# )

# plot_chart_bar_group(
#     dataset=dataset_counted_year_bs,
#     x_axis="year",
#     y_axis="count",
#     grp_axis="historical_site_type_sub",
#     x_label="Year",
#     y_label="Number of Publications",
#     title=""Timeline of Publications by Building Subcategories (2015-2024)",
# )


# ### 1_3 ### Study Focus - Percentage
# dataset_counted_sf = count_dataset(
#     dataset=dataset,
#     fields=["study_focus"],
# )

# print_counts(
#     dataset=dataset_counted_sf,
#     decimal=0,
# )

# plot_chart_bar(
#     dataset=dataset_counted_sf,
#     x_axis="study_focus",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Study Focus Distribution",
# )

# plot_chart_pie(
#     dataset=dataset_counted_sf,
#     field="study_focus",
#     count="count",
#     title="Study Focus Distribution",
#     decimal=1,
# )


### 1_3 ### Study Focus - Percentage
dataset_counted_hsts = count_dataset(
    dataset=dataset,
    fields=["historical_site_type", "historical_site_type_sub"],
)

print_counts(
    dataset=dataset_counted_hsts,
    decimal=1,
)

plot_chart_pie_group(
    dataset=dataset_counted_hsts,
    field="historical_site_type",
    count="count",
    grp_axis="historical_site_type_sub",
    title="Distribution of Historical Site Types",
    decimal=1,
)

plot_chart_sunburst(
    dataset=dataset_counted_hsts,
    field="historical_site_type",
    count="count",
    grp_axis="historical_site_type_sub",
    title="Distribution of Historical Site Types",
    decimal=1,
)
