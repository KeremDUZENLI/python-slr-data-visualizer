from data.maps import (
    COUNTRY_TO_CONTINENT,
    TECHNIQUE_TO_TECHNIQUESUB,
)

from input._1_read import (
    read_dataset,
)
from input._2_prepare import (
    group_dataset_by_fields,
    map_dataset_column,
    map_dataset_hierarchy,
)

from setup import (
    ### bar_1D ###
    _1_0,
    _4_1,
    _5_0,
    ### bar_2D ###
    _1_1,
    _2_1,
    _3_4,
    ### stacked ###
    _2_3_area,
    _2_3_bar,
    _4_5_area,
    ### pie ###
    _1_3,
    ### pie_nested ###
    _1_4,
    _3_2,
    ### heatmap ###
    _3_3,
    _4_2,
    _4_3,
    _4_4,
    ### scatter ###
    _5_1,
    ### sunburst ###
    _1_4_S,
    ### sankey ###
    _3_1,
    ### map ###
    _5_2,
    ### prisma ###
    _0_1,
)


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


#############################################
#################### bar_1D #################
#############################################
# _1_0(DATASET)
# _4_1(DATASET_SOFTWARE_STACKED)
# _5_0(DATASET_COUNTRY_MAPPED)


#############################################
#################### bar_2D #################
#############################################
# _1_1(DATASET)
# _2_1(DATASET)
# _3_4(DATASET)


#############################################
#################### pie ####################
#############################################
# _1_3(DATASET)


#############################################
################# pie_nested ################
#############################################
# _1_4(DATASET)
# _3_2(DATASET_TECHNIQUE_HIERARCHY)


#############################################
################## stacked ##################
#############################################
# _2_3_area(DATASET)
# _2_3_bar(DATASET)
# _4_5_area(DATASET_SOFTWARE_STACKED)


#############################################
################## heatmap ##################
#############################################
# _3_3(DATASET)
# _4_2(DATASET_SOFTWARE_STACKED)
# _4_3(DATASET)
# _4_4(DATASET)


#############################################
################## scatter ##################
#############################################
# _5_1(DATASET_COUNTRY_MAPPED)


#############################################
################## sunburst #################
#############################################
# _1_4_S(DATASET)


#############################################
################### sankey ##################
#############################################
# _3_1(DATASET)


#############################################
#################### map ####################
#############################################
# _5_2(DATASET)


#############################################
################## prisma ###################
#############################################
# _0_1(DATASET)


##############################################
################## refactor ##################
##############################################

from setup import bar_1D


bar_1D(
    dataset=DATASET,
    fields=["year"],
    filter_values=None,
    filter_count=None,
    x_axis="year",
    y_axis="count",
    z_axis=None,
    orientation="v",
    color_field="year",
    color_mapping=False,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_extra=None,
    labels_spec={
        "x_label": "Year",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "year",
            "legend_spec": {
                "title": "Year",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
        },
    ],
    save_name="1.0",
)


bar_1D(
    dataset=DATASET_SOFTWARE_STACKED,
    fields=["software_category", "software"],
    filter_values=["software != "],
    filter_count="count >= 5",
    x_axis="software",
    y_axis="count",
    z_axis="software_category",
    orientation="h",
    color_field="software_category",
    color_mapping=True,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_extra="software_category",
    labels_spec={
        "x_label": "",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "software_category",
            "legend_spec": {
                "title": "Software Category",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
        },
        {
            "source": "custom",
            "values": ["Custom A", "Custom B", "Custom C"],
            "colors_map": {
                "Custom A": "#ff0000",
                "Custom B": "#008000",
                "Custom C": "#0000ff",
            },
            "legend_spec": {
                "title": "Custom Legend",
                "loc": "lower left",
                "bbox": (1, 0, 0.3, 1),
            },
        },
    ],
    save_name="4.1",
)


bar_1D(
    dataset=DATASET_COUNTRY_MAPPED,
    fields=["continent"],
    filter_values=None,
    filter_count=None,
    x_axis="continent",
    y_axis="count",
    z_axis=None,
    orientation="v",
    color_field="continent",
    color_mapping=False,
    bar_borders=False,
    bar_numbers=True,
    grids=True,
    labels_extra=None,
    labels_spec={
        "x_label": "Continents",
        "y_label": "Number of Studies",
        "title": "Studies Per Year",
        "rotation": 45,
    },
    legends_config=[
        {
            "source": "dataset",
            "values": "continent",
            "legend_spec": {
                "title": "Continents",
                "loc": "upper left",
                "bbox": (1, 0, 0.3, 1),
            },
        },
    ],
    save_name="5.0",
)
