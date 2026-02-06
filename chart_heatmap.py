from input._1_read import read_dataset
from input._2_prepare import group_dataset_by_fields
from build_setup import heatmap


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


heatmap(
    dataset=DATASET,
    fields=["historical_site_type", "technique"],
    filter_pre=None,
    filter_pre_sep=None,
    filter_values=None,
    filter_count=None,
    filter_count_sep=None,
    x_axis="historical_site_type",
    y_axis="count",
    z_axis="technique",
    cmap="viridis",
    labels_color="white",
    coloring_field=None,
    matrix_numbers=True,
    labels_extra=None,
    labels_spec={
        "x_label": "Historical Site Type",
        "y_label": "Technique",
        "title": "Historical Site Type X Technique",
        "rotation": 45,
    },
    save_name="3.3",
)


heatmap(
    dataset=DATASET_SOFTWARE_STACKED,
    fields=["software_category", "software", "technique"],
    filter_pre=["software_category", "software"],
    filter_pre_sep=None,
    filter_values=["software != "],
    filter_count="count >= 5",
    filter_count_sep=None,
    x_axis="software",
    y_axis="count",
    z_axis="technique",
    cmap="viridis",
    labels_color="white",
    coloring_field="software_category",
    matrix_numbers=True,
    labels_extra="software_category",
    labels_spec={
        "x_label": "",
        "y_label": "Technique",
        "title": "Software X Technique",
        "rotation": 45,
    },
    save_name="4.2",
)


heatmap(
    dataset=DATASET,
    fields=["software_modeling", "software_data"],
    filter_pre=None,
    filter_pre_sep=[["software_modeling"], ["software_data"]],
    filter_values=["software_modeling != ", "software_data != "],
    filter_count=None,
    filter_count_sep=["count >= 5", "count >= 5"],
    x_axis="software_modeling",
    y_axis="count",
    z_axis="software_data",
    cmap="viridis",
    labels_color="white",
    coloring_field="software_category",
    matrix_numbers=True,
    labels_extra=None,
    labels_spec={
        "x_label": "Software Modeling",
        "y_label": "Software Data",
        "title": "Software Modeling X Software Data",
        "rotation": 45,
    },
    save_name="4.3",
)


heatmap(
    dataset=DATASET,
    fields=["software_modeling", "software_render"],
    filter_pre=None,
    filter_pre_sep=[["software_modeling"], ["software_render"]],
    filter_values=["software_modeling != ", "software_render != "],
    filter_count=None,
    filter_count_sep=["count >= 5", "count >= 3"],
    x_axis="software_modeling",
    y_axis="count",
    z_axis="software_render",
    cmap="viridis",
    labels_color="white",
    coloring_field="software_category",
    matrix_numbers=True,
    labels_extra=None,
    labels_spec={
        "x_label": "Software Modeling",
        "y_label": "Software Render",
        "title": "Software Modeling X Software Render",
        "rotation": 45,
    },
    save_name="4.4",
)
