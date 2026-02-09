from data.maps import COUNTRY_TO_CONTINENT
from input._1_read import read_dataset
from input._2_prepare import map_dataset_column
from build_setup import scatter


DATASET = read_dataset(csv_path="data/dataset.csv")
DATASET_COUNTRY_MAPPED = map_dataset_column(
    dataset=DATASET,
    field_from="country",
    field_to="continent",
    mapping=COUNTRY_TO_CONTINENT,
)


scatter(
    dataset=DATASET_COUNTRY_MAPPED,
    fields=["continent", "country", "historical_site_type"],
    filter_values=None,
    filter_count=None,
    x_axis="country",
    y_axis="count",
    z_axis="historical_site_type",
    coloring_field="continent",
    color_mapping=True,
    grids=True,
    labels_spec={
        "x_label": "Country",
        "y_label": "Historical Site Type",
        "title": "Country X Historical Site Type",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "bubble",
            "legend_spec": {
                "title": "Frequency",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
        },
        {
            "source": "dataset",
            "values": "continent",
            "coloring_field": "continent",
            "legend_spec": {
                "title": "Region",
                "loc": "lower left",
                "bbox": (1, 0, 0.3, 1),
            },
            "casetype": "title",
        },
    ],
    save_name="5_1_Country_Site",
)
