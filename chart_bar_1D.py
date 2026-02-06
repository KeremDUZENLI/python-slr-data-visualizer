from data.maps import COUNTRY_TO_CONTINENT
from input._1_read import read_dataset
from input._2_prepare import group_dataset_by_fields, map_dataset_column
from build_setup import bar_1D


DATASET = read_dataset(csv_path="data/dataset.csv")
DATASET_SOFTWARE_STACKED = group_dataset_by_fields(
    datasets=[
        (
            DATASET,
            {"software": "software_data", "year": "year", "technique": "technique"},
        ),
        (
            DATASET,
            {"software": "software_modeling", "year": "year", "technique": "technique"},
        ),
        (
            DATASET,
            {"software": "software_render", "year": "year", "technique": "technique"},
        ),
    ],
    stack_by={"software_category": "software"},
    axes=["software_category", "software", "year", "technique"],
)
DATASET_COUNTRY_MAPPED = map_dataset_column(
    dataset=DATASET,
    field_from="country",
    field_to="continent",
    mapping=COUNTRY_TO_CONTINENT,
)


bar_1D(
    dataset=DATASET,
    fields=["year"],
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis=None,
    orientation="v",
    coloring_field="year",
    color_mapping=False,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_extra=None,
    labels_spec={
        "x_label": "Year",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "year",
            "coloring_field": "year",
            "legend_spec": {
                "title": "Year",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="1.0",
)


bar_1D(
    dataset=DATASET_SOFTWARE_STACKED,
    fields=["software_category", "software"],
    filter_values=["software != "],
    filter_count="count >= 5",
    x_axis="software",
    y_axis="count",
    z_axis="software_category",
    orientation="h",
    coloring_field="software_category",
    color_mapping=True,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_extra="software_category",
    labels_spec={
        "x_label": "",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "software_category",
            "coloring_field": "software_category",
            "legend_spec": {
                "title": "Software Category",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
        {
            "source": "custom",
            "values": ["Custom A", "Custom B", "Custom C"],
            "colors_map": {
                "Custom A": "#ff0000",
                "Custom B": "#008000",
                "Custom C": "#0000ff",
            },
            "legend_spec": {
                "title": "Custom Legend",
                "loc": "lower left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "upper",
        },
    ],
    save_name="4.1",
)


bar_1D(
    dataset=DATASET_COUNTRY_MAPPED,
    fields=["continent"],
    filter_values=None,
    filter_count=None,
    x_axis="continent",
    y_axis="count",
    z_axis=None,
    orientation="v",
    coloring_field="continent",
    color_mapping=False,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_extra=None,
    labels_spec={
        "x_label": "Continents",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
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
    save_name="5.0",
)
