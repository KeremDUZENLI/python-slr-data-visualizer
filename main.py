from config.maps import (
    map_country,
    map_technique_sub,
)
from src.tools import (
    read_dataset,
    map_dataset_hierarchy,
    filter_dataset_by_field,
    filter_dataset_by_count,
    stack_datasets,
    count_dataset,
)
from setup import (
    chart_bar,
    chart_bar_group,
    chart_stacked,
    chart_heatmap,
    chart_pie,
    chart_pie_group,
    chart_sunburst,
    chart_sankey,
)


PATH = "data/dataset.csv"
DATASET = read_dataset(csv_path=PATH)


# # 1_0 # BAR CHART # X:Year/Y:Count
# chart_bar(
#     dataset=DATASET,
#     fields=["year"],
#     x_axis="year",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications (2015-2024)",
#     orientation="v",
#     grp_axis=None,
#     filter_value=None,
#     filter_count=None,
# )


# # 1_1 # BAR CHART GROUP # X:Year_HST/Y:Count
# chart_bar_group(
#     dataset=DATASET,
#     fields=["year", "historical_site_type"],
#     x_axis="year",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications by Historical Site Categories (2015-2024)",
#     orientation="v",
#     grp_axis="historical_site_type",
#     filter_value=None,
#     filter_count=None,
# )


# # 1_2 # BAR CHART GROUP # X:Year_BS/Y:Count
# chart_bar_group(
#     dataset=DATASET,
#     fields=["year", "historical_site_type_sub"],
#     x_axis="year",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Timeline of Publications by Building Categories (2015-2024)",
#     orientation="v",
#     grp_axis="historical_site_type_sub",
#     filter_value="historical_site_type=Building",
#     filter_count=None,
# )


# # 1_3 # PIE CHART # X:Study Focus/Y:Count
# chart_bar(
#     dataset=DATASET,
#     fields=["study_focus"],
#     x_axis="study_focus",
#     y_axis="count",
#     x_label="Study Focus",
#     y_label="Number of Publications",
#     title="Study Focus Distribution",
#     orientation="v",
#     grp_axis=None,
#     filter_value=None,
#     filter_count=None,
# )

# chart_pie(
#     dataset=DATASET,
#     fields=["study_focus"],
#     count="count",
#     title="Study Focus Distribution",
#     filter_value=None,
#     filter_count=None,
# )


# # 1_4 # SUNBURST CHART # X:Historical Site Type & Sub/Y:Count
# chart_pie_group(
#     dataset=DATASET,
#     fields=["historical_site_type", "historical_site_type_sub"],
#     count="count",
#     title="Distribution of Historical Site Types",
#     grp_axis="historical_site_type_sub",
#     filter_value=None,
#     filter_count=None,
# )

# chart_sunburst(
#     dataset=DATASET,
#     fields=["historical_site_type", "historical_site_type_sub"],
#     count="count",
#     title="Distribution of Historical Site Types",
#     grp_axis="historical_site_type_sub",
#     filter_value=None,
#     filter_count=None,
# )


# # 2_1 # BAR CHART GROUP # X:Plotform/Y:Count
# chart_bar_group(
#     dataset=DATASET,
#     fields=["platform", "device"],
#     x_axis="platform",
#     y_axis="count",
#     x_label="Platform",
#     y_label="Number of Publications",
#     title="Distribution of Devices Across Platforms",
#     orientation="v",
#     grp_axis="device",
#     filter_value=None,
#     filter_count=None,
# )


# # 2_2 # BAR CHART GROUP # X:Device/Y:Count
# chart_bar_group(
#     dataset=DATASET,
#     fields=["device", "platform"],
#     x_axis="device",
#     y_axis="count",
#     x_label="Device",
#     y_label="Number of Publications",
#     title="Distribution of Platforms Across Devices",
#     orientation="v",
#     grp_axis="platform",
#     filter_value=None,
#     filter_count=None,
# )


# # 2_3 # STACKED BAR CHART # X:Year/Y:Count
# chart_stacked(
#     dataset=DATASET,
#     fields=["year", "platform"],
#     x_axis="year",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Platform Adoption Over Time (2015-2024)",
#     kind="area",
#     grp_axis="platform",
#     filter_value=None,
#     filter_count=None,
# )

# chart_stacked(
#     dataset=DATASET,
#     fields=["year", "platform"],
#     x_axis="year",
#     y_axis="count",
#     x_label="Year",
#     y_label="Number of Publications",
#     title="Platform Adoption Over Time (2015-2024)",
#     kind="bar",
#     grp_axis="platform",
#     filter_value=None,
#     filter_count=None,
# )


# # 3_1 # SANKEY DIAGRAM # Study Focus | Historical Site Type | Technique
# chart_sankey(
#     dataset=DATASET,
#     fields=["study_focus", "historical_site_type", "technique"],
#     title="Sankey Diagram of Workflows",
#     column1="study_focus",
#     column2="historical_site_type",
#     column3="technique",
# )


# # 3_2 # SUNBURST CHART # X:Technique & Sub/Y:Count
# dataset_mapped = map_dataset_hierarchy(
#     dataset=DATASET,
#     field_parent="technique",
#     field_child="technique_sub",
#     map=map_technique_sub,
# )

# chart_pie_group(
#     dataset=dataset_mapped,
#     fields=["technique", "technique_sub"],
#     count="count",
#     title="Technique & Sub-Technique Distribution",
#     grp_axis="technique_sub",
#     filter_value=None,
#     filter_count=None,
# )

# chart_sunburst(
#     dataset=dataset_mapped,
#     fields=["technique", "technique_sub"],
#     count="count",
#     title="Technique & Sub-Technique Distribution",
#     grp_axis="technique_sub",
#     filter_value=None,
#     filter_count=None,
# )


# # 3_3 # HEATMAP CHART # X:Technique/Y:Historical Site Type
# chart_heatmap(
#     dataset=DATASET,
#     fields=["technique", "historical_site_type"],
#     x_axis="historical_site_type",
#     y_axis="technique",
#     x_label="Historical Site Type",
#     y_label="Technique",
#     title="Technique Usage Across Historical Site Types",
#     count_axis="count",
#     grp_axis=None,
# )


# # 3_4 # BAR CHART GROUP # X:Technique/Y:Count
# chart_bar_group(
#     dataset=DATASET,
#     fields=["technique", "study_focus"],
#     x_axis="technique",
#     y_axis="count",
#     x_label="Technique",
#     y_label="Frequency",
#     title="Technique Used in Study Focus",
#     orientation="v",
#     grp_axis="study_focus",
#     filter_value=None,
#     filter_count=None,
# )


# 4_1 # BAR CHART # X:Software/Y:Count
dataset_stacked = stack_datasets(
    datasets=[
        (
            DATASET,
            {
                "software": "software_data",
            },
        ),
        (
            DATASET,
            {
                "software": "software_modeling",
            },
        ),
        (
            DATASET,
            {
                "software": "software_render",
            },
        ),
    ],
    stack_by={"software_category": "software"},
    axes=["software_category", "software"],
)

chart_bar(
    dataset=dataset_stacked,
    fields=["software_category", "software"],
    x_axis="software",
    y_axis="count",
    x_label="Software",
    y_label="Frequency",
    title="Software Usage by Category",
    orientation="v",
    grp_axis="software_category",
    filter_value="software!=",
    filter_count="count>=5",
)

chart_bar(
    dataset=dataset_stacked,
    fields=["software_category", "software"],
    x_axis="software",
    y_axis="count",
    x_label="Software",
    y_label="Frequency",
    title="Software Usage by Category",
    orientation="h",
    grp_axis="software_category",
    filter_value="software!=",
    filter_count="count>=5",
)


# 4_2 # HEATMAP CHART # X:Software/Y:Technique
dataset_stacked = stack_datasets(
    datasets=[
        (
            DATASET,
            {
                "software": "software_data",
                "technique": "technique",
            },
        ),
        (
            DATASET,
            {
                "software": "software_modeling",
                "technique": "technique",
            },
        ),
        (
            DATASET,
            {
                "software": "software_render",
                "technique": "technique",
            },
        ),
    ],
    stack_by={"software_category": "software"},
    axes=["software_category", "software", "technique"],
)

chart_heatmap(
    dataset=dataset_stacked,
    fields=["software_category", "software", "technique"],
    x_axis="software",
    y_axis="technique",
    x_label="Software",
    y_label="Technique",
    title="Technique Used with Different Software",
    count_axis="count",
    grp_axis="software_category",
    filter_value="software!=",
    filter_count="count>=3",
)


# 4_3 # HEATMAP CHART # X:Software_Modeling/Y:Software_Data
chart_heatmap(
    dataset=DATASET,
    fields=["software_modeling", "software_data"],
    x_axis="software_modeling",
    y_axis="software_data",
    x_label="Software for Modeling",
    y_label="Software for Data",
    title="Software for Modeling - Software for Data",
    count_axis="count",
    grp_axis=None,
    filter_value="software_modeling!=",
    filter_count="count>2",
)
