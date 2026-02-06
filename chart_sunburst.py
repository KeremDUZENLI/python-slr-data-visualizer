from input._1_read import read_dataset
from build_setup import sunburst


DATASET = read_dataset(csv_path="data/dataset.csv")


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
    pie_borders=False,
    labels_spec={
        "title": "Historical Site Type & Sub-Type Distribution",
    },
    size=(1000, 1000),
)
