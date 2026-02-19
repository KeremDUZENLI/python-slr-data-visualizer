from setup.setup_datasets import DATASET
from setup.setup_functions import prisma


prisma(
    dataset=DATASET,
    fields=[
        "year",
        "country",
        "study_focus",
        "historical_site_type",
        "historical_site_type_sub",
        "device",
    ],
    manual_values={
        "search": 798,
        "duplicates": 315,
        "screening": 483,
        "excluded": 368,
    },
    filter_seq=[],
    labels_spec={
        "search": "Identification\nStudies identified via\nsystematic search\n(n = {search})",
        "duplicates": "Duplicates & non-relevant\nrecords removed\n(n = {duplicates})",
        "screening": "Screening\nStudies after deduplication\n(n = {screening})",
        "excluded": "Studies excluded (score < 4.5)\n(n = {excluded})",
        "eligible": "Included\nStudies included in quantitative\nand qualitative synthesis\n(n = {eligible})",
        # Notes
        "note1": "Step 1 - Exclusions:\n• Duplicate records\n• Non-peer-reviewed\n• Purely theoretical/Book abstracts",
        "note2": "Step 2 - Evaluation Criteria:\n• Case study or real-world implementation\n• Focus on Historical Reconstruction\n• Integration of VR/AR/MR/XR\n• Use of advanced capture (Laser, Photogrammetry, HBIM)\n• Software tools explicitly specified",
    },
    flow_config=[
        ("search", "duplicates"),
        ("duplicates", "screening"),
        ("screening", "excluded"),
        ("screening", "eligible"),
    ],
    notes_config=[
        ("duplicates", "note1"),
        ("screening", "note2"),
    ],
    style_groups={
        "box_main": ["search", "screening", "eligible"],
        "box_excluded": ["duplicates", "excluded"],
        "note": ["note1", "note2"],
    },
    save_name="0_1_PRISMA",
)
