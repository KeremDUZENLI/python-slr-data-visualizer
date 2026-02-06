from input._1_read import read_dataset
from build_setup import prisma


DATASET = read_dataset(csv_path="data/dataset.csv")


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
        "search": 614,
        "duplicates": 256,
        "screening": 358,
        "excluded": 266,
    },
    filter_seq=[
        {"key": "religious", "filter": "historical_site_type_sub == Religious"},
        {"key": "hmd", "filter": "device == HMD"},
        {"key": "final", "filter": "study_focus == Reconstruction"},
    ],
    labels_spec={
        "search": "Studies identified via\nsystematic search\n(n = {search})",
        "duplicates": "Duplicates & non-relevant records removed\n(n = {duplicates})",
        "screening": "Studies after deduplication\n(n = {screening})",
        "excluded": "Studies excluded (score < 4.5)\n(n = {excluded})",
        "eligible": "Studies passing eligibility screening\n(n = {eligible})",
        "religious": "Studies on religious buildings\n(n = {religious})",
        "hmd": "Studies using HMD technology\n(n = {hmd})",
        "final": "Final selected studies:\nReconstruction-focused\n(n = {final})",
        # Notes
        "note1": "Step 1 - Exclusions:\n• Duplicate records\n• Non-peer-reviewed\n• Book chapters",
        "note2": "Step 2 - Screening Criteria:\n• Case study or prototype\n• Historical reconstruction\n• VR/AR/MR/XR integration",
        "note3": "Step 3 - Final Filtering:\n• Religious buildings\n• HMD implementation\n• Reconstruction focus",
    },
    flow_config=[
        ("search", "duplicates"),
        ("duplicates", "screening"),
        ("screening", "excluded"),
        ("screening", "eligible"),
        ("eligible", "religious"),
        ("religious", "hmd"),
        ("hmd", "final"),
    ],
    notes_config=[
        ("duplicates", "note1"),
        ("screening", "note2"),
        ("hmd", "note3"),
    ],
    style_groups={
        "box_main": ["search", "screening", "eligible", "religious", "hmd", "final"],
        "box_excluded": ["duplicates", "excluded"],
        "note": ["note1", "note2", "note3"],
    },
    save_name="0_1_PRISMA",
)
