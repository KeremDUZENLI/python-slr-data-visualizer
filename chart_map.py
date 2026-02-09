from input._1_read import read_dataset
from build_setup import worldmap


DATASET = read_dataset(csv_path="data/dataset.csv")


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
