from setup.setup_datasets import DATASET, DATASET_SOFTWARE_STACKED
from setup.setup_functions import heatmap


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
    cmap="BuGn",
    labels_color="auto",
    coloring_field=None,
    border=False,
    matrix_numbers=True,
    labels_extra=None,
    labels_spec={
        "title": "Historical Site Type X Technique",
        "x_label": "Historical Site Type",
        "y_label": "Technique",
        "rotation": 45,
    },
    save_name="3_3_Site_Technique",
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
    cmap="BuGn",
    labels_color="auto",
    coloring_field="software_category",
    border=False,
    matrix_numbers=True,
    labels_extra="software_category",
    labels_spec={
        "title": "Software X Technique",
        "x_label": "",
        "y_label": "Technique",
        "rotation": 45,
    },
    save_name="4_2_Software_Technique",
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
    cmap="BuGn",
    labels_color="auto",
    coloring_field="software_category",
    border=False,
    matrix_numbers=True,
    labels_extra=None,
    labels_spec={
        "title": "Software Modeling X Software Data",
        "x_label": "Software Modeling",
        "y_label": "Software Data",
        "rotation": 45,
    },
    save_name="4_3_Software_Model_Data",
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
    cmap="BuGn",
    labels_color="auto",
    coloring_field="software_category",
    border=False,
    matrix_numbers=True,
    labels_extra=None,
    labels_spec={
        "title": "Software Modeling X Software Render",
        "x_label": "Software Modeling",
        "y_label": "Software Render",
        "rotation": 45,
    },
    save_name="4_4_Software_Model_Render",
)
