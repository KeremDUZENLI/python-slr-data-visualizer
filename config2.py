def _1_0():
    _1_0_bar_chart = prepare_dataset(
        dataset=DATASET,
        fields=["year"],
        filter_values=None,
        filter_count=None,
    )
    print_simple(dataset=_1_0_bar_chart)
    print_counts(dataset=_1_0_bar_chart, decimal=1)


def _1_3():
    _1_3_bar_chart = prepare_dataset(
        dataset=DATASET,
        fields=["study_focus"],
        filter_values=None,
        filter_count=None,
    )
    print_simple(dataset=_1_3_bar_chart)
    print_counts(dataset=_1_3_bar_chart, decimal=1)


def _4_1():
    dataset_grouped = group_dataset_by_fields(
        datasets=[
            (DATASET, {"software": "software_data", "technique": "technique"}),
            (DATASET, {"software": "software_modeling", "technique": "technique"}),
            (DATASET, {"software": "software_render", "technique": "technique"}),
        ],
        stack_by={"software_category": "software"},
        axes=["software_category", "software", "technique"],
    )
    _4_1_bar_chart = prepare_dataset(
        dataset=dataset_grouped,
        fields=["software_category", "software"],
        filter_values=["software != "],
        filter_count="count >= 5",
    )
    print_simple(dataset=_4_1_bar_chart)
    print_counts(dataset=_4_1_bar_chart, decimal=1)
