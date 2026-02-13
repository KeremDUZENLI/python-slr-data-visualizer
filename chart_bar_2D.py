from setup.setup_datasets import DATASET
from setup.setup_functions import bar_2D


bar_2D(
    dataset=DATASET,
    fields=["year", "historical_site_type"],
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis="historical_site_type",
    orientation="vertical",
    coloring_field="historical_site_type",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    stack_order=None,
    labels_spec={
        "title": "Studies Per Year",
        "x_label": "Year",
        "y_label": "Number of Studies",
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
    fields=["year", "historical_site_type", "historical_site_type_sub"],
    filter_values=["historical_site_type == Building"],
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis="historical_site_type_sub",
    orientation="vertical",
    coloring_field="historical_site_type_sub",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    stack_order=None,
    labels_spec={
        "title": "Studies Per Year",
        "x_label": "Year",
        "y_label": "Number of Studies",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "historical_site_type_sub",
            "coloring_field": "historical_site_type_sub",
            "legend_spec": {
                "title": "Building Subcategory",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="1_2_Years_Publications",
)


bar_2D(
    dataset=DATASET,
    fields=["platform", "device"],
    filter_values=None,
    filter_count=None,
    x_axis="platform",
    y_axis="count",
    z_axis="device",
    orientation="vertical",
    coloring_field="device",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    stack_order=["HMD", "PC", "Mobile", "Immersive Display"],
    labels_spec={
        "title": "Distribution of Devices Across Platforms",
        "x_label": "Platform",
        "y_label": "Number of Studies",
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
            "casetype": "original",
        },
    ],
    save_name="2_1_Platforms_Publications",
)


bar_2D(
    dataset=DATASET,
    fields=["platform", "device", "historical_site_type", "historical_site_type_sub"],
    filter_values=[
        "historical_site_type == Building",
        "historical_site_type_sub == Religious",
    ],
    filter_count=None,
    x_axis="platform",
    y_axis="count",
    z_axis="device",
    orientation="vertical",
    coloring_field="device",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    stack_order=["HMD", "PC", "Mobile", "Immersive Display"],
    labels_spec={
        "title": "Distribution of Devices Across Platforms in Religious Buildings",
        "x_label": "Platform",
        "y_label": "Number of Studies",
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
            "casetype": "original",
        },
    ],
    save_name="2_2_Platforms_Publications_Building_Religious",
)


bar_2D(
    dataset=DATASET,
    fields=["technique", "study_focus"],
    filter_values=None,
    filter_count=None,
    x_axis="technique",
    y_axis="count",
    z_axis="study_focus",
    orientation="vertical",
    coloring_field="study_focus",
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    stack_order=None,
    labels_spec={
        "title": "Techniques Used in Study Focus",
        "x_label": "Technique",
        "y_label": "Number of Studies",
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
    save_name="3_4_Technique_StudyFocus",
)
