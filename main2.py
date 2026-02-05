from data.maps import (
    COUNTRY_TO_CONTINENT,
    TECHNIQUE_TO_TECHNIQUESUB,
)

from input._1_read import (
    read_dataset,
)
from input._2_prepare import (
    group_dataset_by_fields,
    map_dataset_column,
    map_dataset_hierarchy,
)

from setup2 import (
    bar_1D,
    bar_2D,
    stacked,
    pie,
    pie_nested,
    heatmap,
    scatter,
)


DATASET = read_dataset(csv_path="data/dataset.csv")
DATASET_SOFTWARE_STACKED = group_dataset_by_fields(
    datasets=[
        (
            DATASET,
            {"software": "software_data", "year": "year", "technique": "technique"},
        ),
        (
            DATASET,
            {"software": "software_modeling", "year": "year", "technique": "technique"},
        ),
        (
            DATASET,
            {"software": "software_render", "year": "year", "technique": "technique"},
        ),
    ],
    stack_by={"software_category": "software"},
    axes=["software_category", "software", "year", "technique"],
)
DATASET_COUNTRY_MAPPED = map_dataset_column(
    dataset=DATASET,
    field_from="country",
    field_to="continent",
    mapping=COUNTRY_TO_CONTINENT,
)
DATASET_TECHNIQUE_HIERARCHY = map_dataset_hierarchy(
    dataset=DATASET,
    field_parent="technique",
    field_child="technique_sub",
    mapping=TECHNIQUE_TO_TECHNIQUESUB,
)


# bar_1D(
#     dataset=DATASET,
#     fields=["year"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="year",
#     y_axis="count",
#     z_axis=None,
#     orientation="v",
#     coloring_field="year",
#     color_mapping=False,
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_extra=None,
#     labels_spec={
#         "x_label": "Year",
#         "y_label": "Number of Studies",
#         "title": "Studies Per Year",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "year",
#             "coloring_field": "year",
#             "legend_spec": {
#                 "title": "Year",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#     ],
#     save_name="1.0",
# )


# bar_1D(
#     dataset=DATASET_SOFTWARE_STACKED,
#     fields=["software_category", "software"],
#     filter_values=["software != "],
#     filter_count="count >= 5",
#     x_axis="software",
#     y_axis="count",
#     z_axis="software_category",
#     orientation="h",
#     coloring_field="software_category",
#     color_mapping=True,
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_extra="software_category",
#     labels_spec={
#         "x_label": "",
#         "y_label": "Number of Studies",
#         "title": "Studies Per Year",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "software_category",
#             "coloring_field": "software_category",
#             "legend_spec": {
#                 "title": "Software Category",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#         {
#             "source": "custom",
#             "values": ["Custom A", "Custom B", "Custom C"],
#             "colors_map": {
#                 "Custom A": "#ff0000",
#                 "Custom B": "#008000",
#                 "Custom C": "#0000ff",
#             },
#             "legend_spec": {
#                 "title": "Custom Legend",
#                 "loc": "lower left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "upper",
#         },
#     ],
#     save_name="4.1",
# )


# bar_1D(
#     dataset=DATASET_COUNTRY_MAPPED,
#     fields=["continent"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="continent",
#     y_axis="count",
#     z_axis=None,
#     orientation="v",
#     coloring_field="continent",
#     color_mapping=False,
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_extra=None,
#     labels_spec={
#         "x_label": "Continents",
#         "y_label": "Number of Studies",
#         "title": "Studies Per Year",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "continent",
#             "coloring_field": "continent",
#             "legend_spec": {
#                 "title": "Continents",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#     ],
#     save_name="5.0",
# )


# bar_2D(
#     dataset=DATASET,
#     fields=["year", "historical_site_type"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="year",
#     y_axis="count",
#     z_axis="historical_site_type",
#     orientation="v",
#     coloring_field="historical_site_type",
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_spec={
#         "x_label": "Year",
#         "y_label": "Number of Studies",
#         "title": "Studies Per Year",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "historical_site_type",
#             "coloring_field": "historical_site_type",
#             "legend_spec": {
#                 "title": "Historical Site Type",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#     ],
#     save_name="1.1",
# )


# bar_2D(
#     dataset=DATASET,
#     fields=["platform", "device"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="platform",
#     y_axis="count",
#     z_axis="device",
#     orientation="v",
#     coloring_field="device",
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_spec={
#         "x_label": "Platform",
#         "y_label": "Number of Studies",
#         "title": "Distribution of Devices Across Platforms",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "device",
#             "coloring_field": "device",
#             "legend_spec": {
#                 "title": "Device",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#     ],
#     save_name="2.1",
# )


# bar_2D(
#     dataset=DATASET,
#     fields=["technique", "study_focus"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="technique",
#     y_axis="count",
#     z_axis="study_focus",
#     orientation="v",
#     coloring_field="study_focus",
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_spec={
#         "x_label": "Technique",
#         "y_label": "Number of Studies",
#         "title": "Techniques Used in Study Focus",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "study_focus",
#             "coloring_field": "study_focus",
#             "legend_spec": {
#                 "title": "Study Focus",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#     ],
#     save_name="3.4",
# )


# stacked(
#     dataset=DATASET,
#     fields=["year", "platform"],
#     filter_pre=None,
#     filter_values=None,
#     filter_count=None,
#     x_axis="year",
#     y_axis="count",
#     z_axis="platform",
#     orientation="area",
#     stack_order=["VR", "AR", "MR", "XR"],
#     coloring_field="platform",
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_spec={
#         "x_label": "Year",
#         "y_label": "Number of Studies",
#         "title": "Platform Adoption Over Time",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "platform",
#             "coloring_field": "platform",
#             "legend_spec": {
#                 "title": "Platform",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "upper",
#         },
#     ],
#     save_name="2.3.area",
# )


# stacked(
#     dataset=DATASET,
#     fields=["year", "platform"],
#     filter_pre=None,
#     filter_values=None,
#     filter_count=None,
#     x_axis="year",
#     y_axis="count",
#     z_axis="platform",
#     orientation="v",
#     stack_order=["VR", "AR", "MR", "XR"],
#     coloring_field="platform",
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_spec={
#         "x_label": "Year",
#         "y_label": "Number of Studies",
#         "title": "Platform Adoption Over Time",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "platform",
#             "coloring_field": "platform",
#             "legend_spec": {
#                 "title": "Platform",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "upper",
#         },
#     ],
#     save_name="2.3.bar",
# )


# stacked(
#     dataset=DATASET_SOFTWARE_STACKED,
#     fields=["software_category", "software", "year"],
#     filter_pre=["software_category", "software"],
#     filter_values=["software != "],
#     filter_count="count >= 10",
#     x_axis="year",
#     y_axis="count",
#     z_axis="software",
#     orientation="area",
#     stack_order=None,
#     coloring_field="software",
#     bar_borders=False,
#     bar_numbers=True,
#     grids=True,
#     labels_spec={
#         "x_label": "Year",
#         "y_label": "Number of Studies",
#         "title": "Software Adoption Over Time",
#         "rotation": 45,
#     },
#     legends_config=[
#         {
#             "source": "dataset",
#             "values": "software",
#             "coloring_field": "software",
#             "legend_spec": {
#                 "title": "Software",
#                 "loc": "upper left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#         {
#             "source": "dataset",
#             "values": "software_category",
#             "coloring_field": "software_category",
#             "legend_spec": {
#                 "title": "Software Category",
#                 "loc": "lower left",
#                 "bbox": (1, 0, 0.3, 1),
#             },
#             "casetype": "title",
#         },
#     ],
#     save_name="4.5.area",
# )


# pie(
#     dataset=DATASET,
#     fields=["study_focus"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="study_focus",
#     y_axis="count",
#     coloring_field="study_focus",
#     labels_color="white",
#     bar_borders=True,
#     labels_spec={
#         "title": "Study Focus Distribution",
#     },
#     save_name="1.3",
# )


# pie_nested(
#     dataset=DATASET,
#     fields=["historical_site_type", "historical_site_type_sub"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="historical_site_type",
#     y_axis="count",
#     z_axis="historical_site_type_sub",
#     coloring_field_inner="historical_site_type",
#     coloring_field_outer="historical_site_type_sub",
#     labels_color_inner="white",
#     labels_color_outer="black",
#     bar_borders=False,
#     labels_spec={
#         "title": "Historical Site Type & Sub-Type Distribution",
#     },
#     save_name="1.4",
# )


# pie_nested(
#     dataset=DATASET,
#     fields=["technique", "technique_sub"],
#     filter_values=None,
#     filter_count=None,
#     x_axis="technique",
#     y_axis="count",
#     z_axis="technique_sub",
#     coloring_field_inner="technique",
#     coloring_field_outer="technique_sub",
#     labels_color_inner="white",
#     labels_color_outer="black",
#     bar_borders=False,
#     labels_spec={
#         "title": "Technique & Sub-Technique Distribution",
#     },
#     save_name="3.2",
# )


# heatmap(
#     dataset=DATASET,
#     fields=["historical_site_type", "technique"],
#     filter_pre=None,
#     filter_pre_sep=None,
#     filter_values=None,
#     filter_count=None,
#     filter_count_sep=None,
#     x_axis="historical_site_type",
#     y_axis="count",
#     z_axis="technique",
#     cmap="viridis",
#     labels_color="white",
#     coloring_field=None,
#     bar_numbers=True,
#     labels_extra=None,
#     labels_spec={
#         "x_label": "Historical Site Type",
#         "y_label": "Technique",
#         "title": "Historical Site Type X Technique",
#         "rotation": 45,
#     },
#     save_name="3.3",
# )


# heatmap(
#     dataset=DATASET_SOFTWARE_STACKED,
#     fields=["software_category", "software", "technique"],
#     filter_pre=["software_category", "software"],
#     filter_pre_sep=None,
#     filter_values=["software != "],
#     filter_count="count >= 5",
#     filter_count_sep=None,
#     x_axis="software",
#     y_axis="count",
#     z_axis="technique",
#     cmap="viridis",
#     labels_color="white",
#     coloring_field="software_category",
#     bar_numbers=True,
#     labels_extra="software_category",
#     labels_spec={
#         "x_label": "",
#         "y_label": "Technique",
#         "title": "Software X Technique",
#         "rotation": 45,
#     },
#     save_name="4.2",
# )


# heatmap(
#     dataset=DATASET,
#     fields=["software_modeling", "software_data"],
#     filter_pre=None,
#     filter_pre_sep=[["software_modeling"], ["software_data"]],
#     filter_values=["software_modeling != ", "software_data != "],
#     filter_count=None,
#     filter_count_sep=["count >= 5", "count >= 5"],
#     x_axis="software_modeling",
#     y_axis="count",
#     z_axis="software_data",
#     cmap="viridis",
#     labels_color="white",
#     coloring_field="software_category",
#     bar_numbers=True,
#     labels_extra=None,
#     labels_spec={
#         "x_label": "Software Modeling",
#         "y_label": "Software Data",
#         "title": "Software Modeling X Software Data",
#         "rotation": 45,
#     },
#     save_name="4.3",
# )


# heatmap(
#     dataset=DATASET,
#     fields=["software_modeling", "software_render"],
#     filter_pre=None,
#     filter_pre_sep=[["software_modeling"], ["software_render"]],
#     filter_values=["software_modeling != ", "software_render != "],
#     filter_count=None,
#     filter_count_sep=["count >= 5", "count >= 3"],
#     x_axis="software_modeling",
#     y_axis="count",
#     z_axis="software_render",
#     cmap="viridis",
#     labels_color="white",
#     coloring_field="software_category",
#     bar_numbers=True,
#     labels_extra=None,
#     labels_spec={
#         "x_label": "Software Modeling",
#         "y_label": "Software Render",
#         "title": "Software Modeling X Software Render",
#         "rotation": 45,
#     },
#     save_name="4.4",
# )


scatter(
    dataset=DATASET_COUNTRY_MAPPED,
    fields=["continent", "country", "historical_site_type"],
    filter_values=None,
    filter_count=None,
    x_axis="country",
    y_axis="count",
    z_axis="historical_site_type",
    coloring_field="continent",
    color_mapping=True,
    grids=True,
    labels_spec={
        "x_label": "Country",
        "y_label": "Historical Site Type",
        "title": "Country X Historical Site Type",
        "rotation": 45,
    },
    save_name="5.1",
)
