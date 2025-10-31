from config.maps import (
    map_country,
    map_technique_sub,
)
from output.plot import (
    plot_bar,
    plot_bar_group,
    plot_stacked,
    plot_pie,
    plot_pie_group,
    plot_sunburst,
    plot_sankey,
)
from output.print import (
    print_counts,
)
from src.tools import (
    read_dataset,
    map_dataset,
    map_dataset_hierarchy,
    filter_dataset,
    filter_dataset_value,
    count_dataset,
)


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

# plot_bar(
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

# plot_bar_group(
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

# plot_bar_group(
#     dataset=dataset_counted_year_bs,
#     x_axis="year",
#     y_axis="count",
#     grp_axis="historical_site_type_sub",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications by Building Subcategories (2015-2024)",
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

# plot_bar(
#     dataset=dataset_counted_sf,
#     x_axis="study_focus",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Study Focus Distribution",
# )

# plot_pie(
#     dataset=dataset_counted_sf,
#     field="study_focus",
#     count="count",
#     title="Study Focus Distribution",
#     decimal=1,
# )


# ### 1_4 ### Historical Site Type - Percentage
# dataset_counted_hsts = count_dataset(
#     dataset=dataset,
#     fields=["historical_site_type", "historical_site_type_sub"],
# )

# print_counts(
#     dataset=dataset_counted_hsts,
#     decimal=1,
# )

# plot_pie_group(
#     dataset=dataset_counted_hsts,
#     field="historical_site_type",
#     count="count",
#     grp_axis="historical_site_type_sub",
#     title="Distribution of Historical Site Types",
#     decimal=1,
# )

# plot_sunburst(
#     dataset=dataset_counted_hsts,
#     field="historical_site_type",
#     count="count",
#     grp_axis="historical_site_type_sub",
#     title="Distribution of Historical Site Types",
#     decimal=1,
# )


# ### 2_1 ### Platforms - Publications
# dataset_counted_pp = count_dataset(
#     dataset=dataset,
#     fields=["platform", "device"],
# )

# print_counts(
#     dataset=dataset_counted_pp,
#     decimal=1,
# )

# plot_bar_group(
#     dataset=dataset_counted_pp,
#     x_axis="platform",
#     y_axis="count",
#     grp_axis="device",
#     x_label="Platform",
#     y_label="Number of Publications",
#     title="Distribution of Devices Across Platforms",
# )

# ### 2_2 ### Devices - Publications
# dataset_counted_dp = count_dataset(
#     dataset=dataset,
#     fields=["device", "platform"],
# )

# print_counts(
#     dataset=dataset_counted_dp,
#     decimal=1,
# )

# plot_bar_group(
#     dataset=dataset_counted_dp,
#     x_axis="device",
#     y_axis="count",
#     grp_axis="platform",
#     x_label="Platform",
#     y_label="Number of Publications",
#     title="Distribution of Platforms Across Devices",
# )


# ### 2_3 ### Platforms_Year - Publications
# dataset_counted_pyp = count_dataset(
#     dataset=dataset,
#     fields=["year", "platform"],
# )

# print_counts(
#     dataset=dataset_counted_pyp,
#     decimal=1,
# )

# plot_stacked(
#     dataset_counted_pyp,
#     x_axis="year",
#     y_axis="count",
#     grp_axis="platform",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Platform Adoption Over Time (2015-2024)",
# )


# ### 3_1 ### SF - HST - T
# dataset_counted_sfhstt = count_dataset(
#     dataset=dataset,
#     fields=["study_focus", "historical_site_type", "technique"],
# )

# print_counts(
#     dataset=dataset_counted_sfhstt,
#     decimal=1,
# )

# plot_sankey(
#     dataset=dataset_counted_sfhstt,
#     column1="study_focus",
#     column2="historical_site_type",
#     column3="technique",
#     title="Sankey Diagram of Workflows",
# )


### 3_2 ### Technique - TechniqueSub
dataset_mapped = map_dataset_hierarchy(
    dataset=dataset,
    field_parent="technique",
    field_child="technique_sub",
    map=map_technique_sub,
)

dataset_counted_tts = count_dataset(
    dataset=dataset_mapped,
    fields=["technique", "technique_sub"],
)

print_counts(
    dataset=dataset_counted_tts,
    decimal=1,
)

plot_pie_group(
    dataset=dataset_counted_tts,
    field="technique",
    count="count",
    grp_axis="technique_sub",
    title="Technique & Sub-Technique Distribution",
    decimal=1,
)

plot_sunburst(
    dataset=dataset_counted_tts,
    field="technique",
    count="count",
    grp_axis="technique_sub",
    title="Technique & Sub-Technique Distribution",
    decimal=1,
)
