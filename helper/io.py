import os
import csv

COLUMNS = [
    "order",
    "year",
    "country",
    "study_focus",
    "historical_site_type",
    "historical_site_type_sub",
    "platform",
    "device",
    "technique",
    "technique_sub",
    "software_data",
    "software_modeling",
    "software_render",
]


def list_to_csv(data, csv_path, sep=";"):
    os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)

    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)

        for row in data:
            out = []
            for v in row:
                if isinstance(v, (list, tuple)):
                    out.append(sep.join(str(x) for x in v))
                else:
                    out.append(v)
            writer.writerow(out)
