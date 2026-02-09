from setup.setup_datasets import DATASET_COUNTRY_MAPPED
from setup.setup_functions import scatter


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
