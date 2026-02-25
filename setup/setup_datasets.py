from config.maps import COUNTRY_TO_CONTINENT, TECHNIQUE_TO_TECHNIQUESUB
from input._1_read import read_dataset
from input._2_prepare import (
    group_dataset_by_fields,
    map_dataset_column,
    map_dataset_hierarchy,
)


DATASET = read_dataset(csv_path="data/dataset.example.csv")
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
DATASET_TECHNIQUE_HIERARCHY = map_dataset_hierarchy(
    dataset=DATASET,
    field_parent="technique",
    field_child="technique_sub",
    mapping=TECHNIQUE_TO_TECHNIQUESUB,
)
