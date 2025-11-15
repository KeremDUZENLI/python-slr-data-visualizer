from config import (
    chart_bar_1D,
)

chart_bar_1D(
    fields=["year"],
    x_axis="year",
    y_axis="count",
    labels_spec={
        "x_label": "Year",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    orientation="v",
    color_field="year",
    color_axis="x",
    labels_legend={
        "title": "Year",
        "loc": "upper right",
    },
    filter_values=None,
    filter_count=None,
    save_path="figures/0_0.png",
)


chart_bar_1D(
    fields=["study_focus"],
    x_axis="study_focus",
    y_axis="count",
    labels_spec={
        "x_label": "Study Focus",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    orientation="v",
    color_field="study_focus",
    color_axis="x",
    labels_legend={
        "title": "Study Focus",
        "loc": "upper right",
    },
    filter_values=None,
    filter_count=None,
    save_path="figures/1_3.png",
)
