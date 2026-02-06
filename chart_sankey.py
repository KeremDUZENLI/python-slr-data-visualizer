from input._1_read import read_dataset
from build_setup import sankey


DATASET = read_dataset(csv_path="data/dataset.csv")


sankey(
    dataset=DATASET,
    fields=["study_focus", "historical_site_type", "technique"],
    filter_values=None,
    filter_count=None,
    x_axis="study_focus",
    y_axis="historical_site_type",
    z_axis="technique",
    nodes_pad=15,
    nodes_thickness=20,
    links_color="gray",
    links_opacity=0.25,
    labels_color="black",
    labels_spec={
        "title": "Workflow: Study Focus -> Site -> Technique",
    },
    size=(1000, 1000),
)
