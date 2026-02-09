from setup.setup_datasets import DATASET
from setup.setup_functions import pie


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
