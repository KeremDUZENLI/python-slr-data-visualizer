from input._1_read import read_dataset
from build_setup import bar_2D


DATASET = read_dataset(csv_path="data/dataset.csv")


bar_2D(
    dataset=DATASET,
    fields=["historical_site_type", "year"],
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis="historical_site_type",
    orientation="v",
    coloring_field="historical_site_type",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_spec={
        "x_label": "Year",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "historical_site_type",
            "coloring_field": "historical_site_type",
            "legend_spec": {
                "title": "Historical Site Type",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="1_1_Years_Publications",
)


bar_2D(
    dataset=DATASET,
    fields=["platform", "device"],
    filter_values=None,
    filter_count=None,
    x_axis="platform",
    y_axis="count",
    z_axis="device",
    orientation="v",
    coloring_field="device",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_spec={
        "x_label": "Platform",
        "y_label": "Number of Studies",
        "title": "Distribution of Devices Across Platforms",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "device",
            "coloring_field": "device",
            "legend_spec": {
                "title": "Device",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="2.1",
)


bar_2D(
    dataset=DATASET,
    fields=["technique", "study_focus"],
    filter_values=None,
    filter_count=None,
    x_axis="technique",
    y_axis="count",
    z_axis="study_focus",
    orientation="v",
    coloring_field="study_focus",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_spec={
        "x_label": "Technique",
        "y_label": "Number of Studies",
        "title": "Techniques Used in Study Focus",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "study_focus",
            "coloring_field": "study_focus",
            "legend_spec": {
                "title": "Study Focus",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="3.4",
)
