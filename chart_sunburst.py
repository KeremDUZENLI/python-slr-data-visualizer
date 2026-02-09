from config.maps import TECHNIQUE_TO_TECHNIQUESUB
from input._1_read import read_dataset
from input._2_prepare import map_dataset_hierarchy
from build_setup import sunburst


DATASET = read_dataset(csv_path="data/dataset.csv")
DATASET_TECHNIQUE_HIERARCHY = map_dataset_hierarchy(
    dataset=DATASET,
    field_parent="technique",
    field_child="technique_sub",
    mapping=TECHNIQUE_TO_TECHNIQUESUB,
)


sunburst(
    dataset=DATASET,
    fields=["historical_site_type", "historical_site_type_sub"],
    filter_values=None,
    filter_count=None,
    x_axis="historical_site_type",
    y_axis="count",
    z_axis="historical_site_type_sub",
    coloring_field_inner="historical_site_type",
    coloring_field_outer="historical_site_type_sub",
    labels_color_inner="white",
    labels_color_outer="black",
    labels_hide_percent=2,
    pie_borders=False,
    labels_spec={
        "title": "",
    },
    size=(1000, 1000),
)


sunburst(
    dataset=DATASET_TECHNIQUE_HIERARCHY,
    fields=["technique", "technique_sub"],
    filter_values=None,
    filter_count=None,
    x_axis="technique",
    y_axis="count",
    z_axis="technique_sub",
    coloring_field_inner="technique",
    coloring_field_outer="technique_sub",
    labels_color_inner="white",
    labels_color_outer="black",
    labels_hide_percent=2,
    pie_borders=False,
    labels_spec={
        "title": "",
    },
    size=(1000, 1000),
)
