from input._1_read import read_dataset
from build_setup import pie_nested


DATASET = read_dataset(csv_path="data/dataset.csv")


pie_nested(
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
    pie_borders=False,
    labels_spec={
        "title": "Historical Site Type & Sub-Type Distribution",
    },
    save_name="1.4",
)


pie_nested(
    dataset=DATASET,
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
    pie_borders=False,
    labels_spec={
        "title": "Technique & Sub-Technique Distribution",
    },
    save_name="3.2",
)
