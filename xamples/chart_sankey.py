from setup.setup_datasets import DATASET
from setup.setup_functions import sankey


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
    links_color="source",
    links_opacity=0.1,
    labels_color="black",
    labels_spec={
        "title1": "STUDY FOCUS",
        "title2": "HISTORICAL SITE TYPE",
        "title3": "TECHNIQUE",
    },
    size=(1000, 750),
)
