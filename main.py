from input._1_read import (
    read_dataset,
)
from input._2_prepare import (
    group_dataset_by_fields,
)
from setup import (
    _0_0,
    _1_3,
    _4_1,
)


DATASET = read_dataset(csv_path="data/dataset.csv")
DATASET_SOFTWARE = group_dataset_by_fields(
    datasets=[
        (DATASET, {"software": "software_data", "technique": "technique"}),
        (DATASET, {"software": "software_modeling", "technique": "technique"}),
        (DATASET, {"software": "software_render", "technique": "technique"}),
    ],
    stack_by={"software_category": "software"},
    axes=["software_category", "software", "technique"],
)


_0_0(DATASET)
_1_3(DATASET)
_4_1(DATASET_SOFTWARE)
