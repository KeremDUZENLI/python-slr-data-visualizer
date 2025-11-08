from src.tools import read_dataset
from setup import (
    chart_bar,
    chart_bar_group,
    chart_pie,
)


PATH = "data/dataset.csv"
DATASET = read_dataset(csv_path=PATH)


# 1_0 # BAR CHART # X:Year/Y:Count
chart_bar(
    dataset=DATASET,
    fields=["year"],
    x_axis="year",
    y_axis="count",
    x_label="Year",
    y_label="Number of Publications",
    title="Timeline of Publications (2015-2024)",
    orientation="v",
    filter_value=None,
    filter_count=None,
)


# 1_1 # BAR CHART GROUP # X:Year_HST/Y:Count
chart_bar_group(
    dataset=DATASET,
    fields=["year", "historical_site_type"],
    x_axis="year",
    y_axis="count",
    x_label="Year",
    y_label="Number of Publications",
    title="Timeline of Publications by Historical Site Categories (2015-2024)",
    orientation="v",
    grp_axis="historical_site_type",
    filter_value=None,
    filter_count=None,
)


# 1_2 # BAR CHART GROUP # X:Year_BS/Y:Count
chart_bar_group(
    dataset=DATASET,
    fields=["year", "historical_site_type_sub"],
    x_axis="year",
    y_axis="count",
    x_label="Year",
    y_label="Number of Publications",
    title="Timeline of Publications by Building Categories (2015-2024)",
    orientation="v",
    grp_axis="historical_site_type_sub",
    filter_value="historical_site_type=Building",
    filter_count=None,
)


# 1_3 # BAR CHART # X:Study Focus/Y:Count
chart_bar(
    dataset=DATASET,
    fields=["study_focus"],
    x_axis="study_focus",
    y_axis="count",
    x_label="Study Focus",
    y_label="Number of Publications",
    title="Study Focus Distribution",
    orientation="v",
    filter_value=None,
    filter_count=None,
)

chart_pie(
    dataset=DATASET,
    fields=["study_focus"],
    count="count",
    title="Study Focus Distribution",
    filter_value=None,
    filter_count=None,
)
