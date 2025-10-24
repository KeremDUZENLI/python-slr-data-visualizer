# python-slr-data-visualizer

A Python pipeline for data analysis and visualization of systematic literature reviews (SLR). Includes PRISMA flows, networks, timelines, sunbursts, and heatmaps for reproducible academic workflows.

```bash
dataset.example = [
    (
        0,  # field_0: Unique identifier for the entity (integer, e.g., study ID, project ID)
        0,  # field_1: Numeric attribute (e.g., year, timestamp, or other quantitative value)
        "",  # field_2: Categorical attribute (e.g., location, category, or group)
        "",  # field_3: Primary focus or type (e.g., study focus, project type; used for network connections)
        "",  # field_4: Main category or type (e.g., domain, subject, or entity type)
        "",  # field_5: Subcategory or subtype (e.g., specific classification within the main category)
        [],  # field_6: List of primary attributes (e.g., platforms, methods; used for network connections)
        [],  # field_7: List of secondary attributes (e.g., devices, tools, or resources)
        [],  # field_8: List of techniques or approaches (e.g., methodologies; used for network connections)
        [],  # field_9: List of specific techniques or sub-approaches (e.g., detailed methods or processes)
        [],  # field_10: List of tools or resources for data collection (e.g., software, instruments)
        [],  # field_11: List of tools or resources for processing (e.g., modeling or analysis tools)
        [],  # field_12: List of tools or resources for output (e.g., visualization or rendering tools)
    ),
    # Add more entries as needed, following the same 13-field structure
]
```
