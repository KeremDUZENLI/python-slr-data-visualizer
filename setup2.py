from config.maps import (
    map_country,
    map_technique_sub,
)
from output.plot import (
    plot_bar,
    plot_bar_group,
    plot_stacked,
    plot_heatmap,
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
    map_dataset_column,
    map_dataset_hierarchy,
    filter_dataset_by_field,
    filter_dataset_by_value,
    filter_dataset_by_count,
    count_dataset,
    stack_datasets,
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
#     orientation="v",
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
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications by Historical Site Categories (2015-2024)",
#     orientation="v",
#     grp_axis="historical_site_type",
# )


# ### 1_2 ### X:Year_BS | Y:Count
# dataset_value_filtered = filter_dataset_by_value(
#     dataset=dataset,
#     field="historical_site_type",
#     values="Building",
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
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications by Building Subcategories (2015-2024)",
#     orientation="v",
#     grp_axis="historical_site_type_sub",
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
#     orientation="v",
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
#     title="Distribution of Historical Site Types",
#     grp_axis="historical_site_type_sub",
# )

# plot_sunburst(
#     dataset=dataset_counted_hsts,
#     field="historical_site_type",
#     count="count",
#     title="Distribution of Historical Site Types",
#     grp_axis="historical_site_type_sub",
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
#     x_label="Platform",
#     y_label="Number of Publications",
#     title="Distribution of Devices Across Platforms",
#     orientation="v",
#     grp_axis="device",
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
#     x_label="Device",
#     y_label="Number of Publications",
#     title="Distribution of Platforms Across Devices",
#     orientation="v",
#     grp_axis="platform",
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
#     dataset=dataset_counted_pyp,
#     x_axis="year",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Platform Adoption Over Time (2015-2024)",
#     kind="area",
#     grp_axis="platform",
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
#     title="Sankey Diagram of Workflows",
#     column1="study_focus",
#     column2="historical_site_type",
#     column3="technique",
# )


# ### 3_2 ### Technique - TechniqueSub
# dataset_mapped = map_dataset_hierarchy(
#     dataset=dataset,
#     field_parent="technique",
#     field_child="technique_sub",
#     map=map_technique_sub,
# )

# dataset_counted_tts = count_dataset(
#     dataset=dataset_mapped,
#     fields=["technique", "technique_sub"],
# )

# print_counts(
#     dataset=dataset_counted_tts,
#     decimal=1,
# )

# plot_pie_group(
#     dataset=dataset_counted_tts,
#     field="technique",
#     count="count",
#     title="Technique & Sub-Technique Distribution",
#     grp_axis="technique_sub",
# )

# plot_sunburst(
#     dataset=dataset_counted_tts,
#     field="technique",
#     count="count",
#     title="Technique & Sub-Technique Distribution",
#     grp_axis="technique_sub",
# )


# ### 3_3 ### Technique x Historical Site Type — Heatmap
# dataset_counted_th = count_dataset(
#     dataset=dataset,
#     fields=["technique", "historical_site_type"],
# )

# plot_heatmap(
#     dataset=dataset_counted_th,
#     x_axis="historical_site_type",
#     y_axis="technique",
#     x_label="Historical Site Type",
#     y_label="Technique",
#     title="Technique Usage Across Historical Site Types",
#     count_axis="count",
# )


# ### 3_4 ### Technique - Study Focus
# dataset_counted_tsf = count_dataset(
#     dataset=dataset,
#     fields=["technique", "study_focus"],
# )

# plot_bar_group(
#     dataset=dataset_counted_tsf,
#     x_axis="technique",
#     y_axis="count",
#     x_label="Techniques",
#     y_label="Frequency",
#     title="Technique Used in Study Focus",
#     orientation="v",
#     grp_axis="study_focus",
# )


# ### 4_1 ### Software by Category (Horizontal)
# ### software_data ###
# dataset_counted_sc_data = count_dataset(
#     dataset=dataset,
#     fields=["software_data"],
# )
# dataset_sc_data_filtered_by_count = filter_dataset_by_count(
#     dataset=dataset_counted_sc_data,
#     value=5,
#     comparison=">=",
# )
# dataset_sc_data_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_sc_data_filtered_by_count,
#     field="software_data",
#     values=[""],
#     include=False,
# )
# print_counts(
#     dataset=dataset_sc_data_filtered_by_value,
#     decimal=1,
# )


# ### software_modeling ###
# dataset_counted_sc_modeling = count_dataset(
#     dataset=dataset,
#     fields=["software_modeling"],
# )
# dataset_sc_modeling_filtered_by_count = filter_dataset_by_count(
#     dataset=dataset_counted_sc_modeling,
#     value=5,
#     comparison=">=",
# )
# dataset_sc_modeling_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_sc_modeling_filtered_by_count,
#     field="software_modeling",
#     values=[""],
#     include=False,
# )
# print_counts(
#     dataset=dataset_sc_modeling_filtered_by_value,
#     decimal=1,
# )


# ### software_render ###
# dataset_counted_sc_render = count_dataset(
#     dataset=dataset,
#     fields=["software_render"],
# )
# dataset_sc_render_filtered_by_count = filter_dataset_by_count(
#     dataset=dataset_counted_sc_render,
#     value=5,
#     comparison=">=",
# )
# dataset_sc_render_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_sc_render_filtered_by_count,
#     field="software_render",
#     values=[""],
#     include=False,
# )
# print_counts(
#     dataset=dataset_sc_render_filtered_by_value,
#     decimal=1,
# )


# ### stacked ###
# dataset_sc_stacked = stack_datasets(
#     datasets=[
#         (
#             dataset_sc_data_filtered_by_value,
#             {
#                 "software": "software_data",
#                 "count": "count",
#             },
#         ),
#         (
#             dataset_sc_modeling_filtered_by_value,
#             {
#                 "software": "software_modeling",
#                 "count": "count",
#             },
#         ),
#         (
#             dataset_sc_render_filtered_by_value,
#             {
#                 "software": "software_render",
#                 "count": "count",
#             },
#         ),
#     ],
#     stack_by={"softwares": "software"},
#     axes=["softwares", "software", "count"],
# )
# print_counts(
#     dataset=dataset_sc_stacked,
#     decimal=1,
# )


# ### plot ###
# plot_bar(
#     dataset=dataset_sc_stacked,
#     x_axis="software",
#     y_axis="count",
#     x_label="Software",
#     y_label="Frequency",
#     title="Software Usage by Category",
#     orientation="v",
#     grp_axis="softwares",
# )
# plot_bar(
#     dataset=dataset_sc_stacked,
#     x_axis="software",
#     y_axis="count",
#     x_label="Software",
#     y_label="Frequency",
#     title="Software Usage by Category",
#     orientation="h",
#     grp_axis="softwares",
# )


# ### 4_2 ### Technique x Software — Heatmap
# ### software_data ###
# dataset_counted_sc_data = count_dataset(
#     dataset=dataset,
#     fields=["software_data"],
# )
# dataset_sc_data_filtered_by_count = filter_dataset_by_count(
#     dataset=dataset_counted_sc_data,
#     value=5,
#     comparison=">",
# )
# dataset_sc_data_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_sc_data_filtered_by_count,
#     field="software_data",
#     values="",
#     include=False,
# )
# print_counts(
#     dataset=dataset_sc_data_filtered_by_value,
#     decimal=1,
# )

# dataset_counted_ts_data = count_dataset(
#     dataset=dataset,
#     fields=["software_data", "technique"],
# )
# dataset_ts_data_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_counted_ts_data,
#     field="software_data",
#     values="",
#     include=False,
# )

# dataset_ts_data_filtered = filter_dataset_by_value(
#     dataset=dataset_ts_data_filtered_by_value,
#     field="software_data",
#     values=dataset_sc_data_filtered_by_value["software_data"],
#     include=True,
# )
# print_counts(
#     dataset=dataset_ts_data_filtered,
#     decimal=1,
# )


# ### software_modeling ###
# dataset_counted_sc_modeling = count_dataset(
#     dataset=dataset,
#     fields=["software_modeling"],
# )
# dataset_sc_modeling_filtered_by_count = filter_dataset_by_count(
#     dataset=dataset_counted_sc_modeling,
#     value=5,
#     comparison=">",
# )
# dataset_sc_modeling_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_sc_modeling_filtered_by_count,
#     field="software_modeling",
#     values="",
#     include=False,
# )
# print_counts(
#     dataset=dataset_sc_modeling_filtered_by_value,
#     decimal=1,
# )

# dataset_counted_ts_modeling = count_dataset(
#     dataset=dataset,
#     fields=["software_modeling", "technique"],
# )
# dataset_ts_modeling_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_counted_ts_modeling,
#     field="software_modeling",
#     values="",
#     include=False,
# )

# dataset_ts_modeling_filtered = filter_dataset_by_value(
#     dataset=dataset_ts_modeling_filtered_by_value,
#     field="software_modeling",
#     values=dataset_sc_modeling_filtered_by_value["software_modeling"],
#     include=True,
# )
# print_counts(
#     dataset=dataset_ts_modeling_filtered,
#     decimal=1,
# )


# ### software_render ###
# dataset_counted_sc_render = count_dataset(
#     dataset=dataset,
#     fields=["software_render"],
# )
# dataset_sc_render_filtered_by_count = filter_dataset_by_count(
#     dataset=dataset_counted_sc_render,
#     value=5,
#     comparison=">",
# )
# dataset_sc_render_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_sc_render_filtered_by_count,
#     field="software_render",
#     values="",
#     include=False,
# )
# print_counts(
#     dataset=dataset_sc_render_filtered_by_value,
#     decimal=1,
# )

# dataset_counted_ts_render = count_dataset(
#     dataset=dataset,
#     fields=["software_render", "technique"],
# )
# dataset_ts_render_filtered_by_value = filter_dataset_by_value(
#     dataset=dataset_counted_ts_render,
#     field="software_render",
#     values="",
#     include=False,
# )

# dataset_ts_render_filtered = filter_dataset_by_value(
#     dataset=dataset_ts_render_filtered_by_value,
#     field="software_render",
#     values=dataset_sc_render_filtered_by_value["software_render"],
#     include=True,
# )
# print_counts(
#     dataset=dataset_ts_render_filtered,
#     decimal=1,
# )


# ### stacked ###
# dataset_sc_stacked = stack_datasets(
#     datasets=[
#         (
#             dataset_ts_data_filtered,
#             {
#                 "software": "software_data",
#                 "technique": "technique",
#                 "count": "count",
#             },
#         ),
#         (
#             dataset_ts_modeling_filtered,
#             {
#                 "software": "software_modeling",
#                 "technique": "technique",
#                 "count": "count",
#             },
#         ),
#         (
#             dataset_ts_render_filtered,
#             {
#                 "software": "software_render",
#                 "technique": "technique",
#                 "count": "count",
#             },
#         ),
#     ],
#     stack_by={"softwares": "software"},
#     axes=["softwares", "software", "technique", "count"],
# )
# print_counts(
#     dataset=dataset_sc_stacked,
#     decimal=1,
# )

# plot_heatmap(
#     dataset=dataset_sc_stacked,
#     x_axis="software",
#     y_axis="technique",
#     x_label="Software",
#     y_label="Technique",
#     title="Technique Used with Different Software",
#     count_axis="count",
#     grp_axis="softwares",
# )
