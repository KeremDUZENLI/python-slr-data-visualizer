from input._1_read import read_dataset
from build_setup import bar_2D


DATASET = read_dataset(csv_path="data/dataset.csv")


bar_2D(
    dataset=DATASET,
    fields=["year", "historical_site_type"],
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis="historical_site_type",
    orientation="v",
    coloring_field="historical_site_type",
    stack_order=None,
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
    fields=["year", "historical_site_type", "historical_site_type_sub"],
    filter_values=["historical_site_type == Building"],
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis="historical_site_type_sub",
    orientation="v",
    coloring_field="historical_site_type_sub",
    stack_order=None,
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
    orientation="v",
    coloring_field="device",
    stack_order=["HMD", "PC", "Mobile", "Immersive Display"],
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
    orientation="v",
    coloring_field="device",
    stack_order=["HMD", "PC", "Mobile", "Immersive Display"],
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_spec={
        "x_label": "Platform",
        "y_label": "Number of Studies",
        "title": "Distribution of Devices Across Platforms in Religious Buildings",
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
    orientation="v",
    coloring_field="study_focus",
    stack_order=None,
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
