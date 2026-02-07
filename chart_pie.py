from input._1_read import read_dataset
from build_setup import pie


DATASET = read_dataset(csv_path="data/dataset.csv")


pie(
    dataset=DATASET,
    fields=["study_focus"],
    filter_values=None,
    filter_count=None,
    x_axis="study_focus",
    y_axis="count",
    coloring_field="study_focus",
    labels_color="white",
    pie_borders=True,
    labels_spec={
        "title": "Study Focus Distribution",
    },
    save_name="1_3_StudyFocus",
)
