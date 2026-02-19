from setup.setup_datasets import (
    DATASET,
    DATASET_SOFTWARE_STACKED,
    DATASET_COUNTRY_MAPPED,
)
from setup.setup_functions import bar_1D


bar_1D(
    dataset=DATASET,
    fields=["year"],
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis=None,
    orientation="vertical",
    coloring_field="year",
    bar_borders=False,
    bar_numbers=False,
    grids=True,
    color_mapping=False,
    labels_extra=None,
    labels_spec={
        "title": "Total Studies Per Year",
        "x_label": "Year",
        "y_label": "Number of Studies",
        "rotation": 45,
    },
    legends_config=None,
    save_name="1_0_Total_Studies_Per_Year",
)


bar_1D(
    dataset=DATASET_SOFTWARE_STACKED,
    fields=["software_category", "software"],
    filter_values=["software != "],
    filter_count="count >= 5",
    x_axis="software",
    y_axis="count",
    z_axis="software_category",
    orientation="horizontal",
    coloring_field="software_category",
    bar_borders=False,
    bar_numbers=False,
    grids=True,
    color_mapping=True,
    labels_extra="software_category",
    labels_spec={
        "title": "Software Usage by Category",
        "x_label": "",
        "y_label": "Number of Studies",
        "rotation": 45,
    },
    legends_config=None,
    save_name="4_1_Software_Category",
)


bar_1D(
    dataset=DATASET_COUNTRY_MAPPED,
    fields=["continent"],
    filter_values=None,
    filter_count=None,
    x_axis="continent",
    y_axis="count",
    z_axis=None,
    orientation="vertical",
    coloring_field="continent",
    bar_borders=False,
    bar_numbers=False,
    grids=True,
    color_mapping=False,
    labels_extra=None,
    labels_spec={
        "title": "Studies Per Continent",
        "x_label": "Continents",
        "y_label": "Number of Studies",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "continent",
            "coloring_field": "continent",
            "legend_spec": {
                "title": "Continents",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="5_0_Continent_Studies",
)
