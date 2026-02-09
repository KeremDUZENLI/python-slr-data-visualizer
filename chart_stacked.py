from setup.setup_datasets import DATASET, DATASET_SOFTWARE_STACKED
from setup.setup_functions import stacked


stacked(
    dataset=DATASET,
    fields=["year", "platform"],
    filter_pre=None,
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis="platform",
    orientation="area",
    coloring_field="platform",
    stack_order=["XR", "MR", "AR", "VR"],
    stack_borders=False,
    bar_numbers=False,
    grids=True,
    labels_spec={
        "x_label": "Year",
        "y_label": "Number of Studies",
        "title": "Platform Adoption Over Time",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "platform",
            "coloring_field": "platform",
            "legend_spec": {
                "title": "Platform",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "upper",
        },
    ],
    save_name="2_3_Platforms_Adoptation_Area",
)


stacked(
    dataset=DATASET,
    fields=["year", "platform"],
    filter_pre=None,
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis="platform",
    orientation="v",
    coloring_field="platform",
    stack_order=["XR", "MR", "AR", "VR"],
    stack_borders=False,
    bar_numbers=False,
    grids=True,
    labels_spec={
        "x_label": "Year",
        "y_label": "Number of Studies",
        "title": "Platform Adoption Over Time",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "platform",
            "coloring_field": "platform",
            "legend_spec": {
                "title": "Platform",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "upper",
        },
    ],
    save_name="2_3_Platforms_Adoptation",
)


stacked(
    dataset=DATASET_SOFTWARE_STACKED,
    fields=["software_category", "software", "year"],
    filter_pre=["software_category", "software"],
    filter_values=["software != "],
    filter_count="count >= 10",
    x_axis="year",
    y_axis="count",
    z_axis="software",
    orientation="area",
    coloring_field="software",
    stack_order=None,
    stack_borders=False,
    bar_numbers=False,
    grids=True,
    labels_spec={
        "x_label": "Year",
        "y_label": "Number of Studies",
        "title": "Software Adoption Over Time",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "software",
            "coloring_field": "software",
            "legend_spec": {
                "title": "Software",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
        {
            "source": "dataset",
            "values": "software_category",
            "coloring_field": "software_category",
            "legend_spec": {
                "title": "Software Category",
                "loc": "lower left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="4_5_Year_Software_Adoptation_Area",
)
