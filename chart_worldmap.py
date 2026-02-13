from setup.setup_datasets import DATASET
from setup.setup_functions import worldmap


worldmap(
    dataset=DATASET,
    fields=["country"],
    filter_values=None,
    filter_count=None,
    x_axis="country",
    y_axis="count",
    labels_color="black",
    cmap="YlOrRd",
    borders=True,
    frame=True,
    labels_spec={
        "title": "Geographical Distribution of Studies",
    },
    size=(1000, 500),
)
