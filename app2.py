import ast
import os
import streamlit as st

from config.maps import COUNTRY_TO_CONTINENT, TECHNIQUE_TO_TECHNIQUESUB
from input._1_read import read_dataset
from input._2_prepare import (
    group_dataset_by_fields,
    map_dataset_column,
    map_dataset_hierarchy,
)


st.set_page_config(layout="wide", page_title="SLR Data Visualizer")
st.title("SLR Data Visualization Tool")

uploaded_file = st.file_uploader("Upload Dataset (CSV)", type="csv")
if uploaded_file:
    # ---------------------------------------------------------
    # read_dataset
    # ---------------------------------------------------------
    temp_path = "temp_dataset.csv"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    DATASET = read_dataset(csv_path=temp_path)
    os.remove(temp_path)

    tab_group, tab_map, tab_hierarchy = st.tabs(
        [
            "1️⃣ Group Dataset by Fields",
            "2️⃣ Map Dataset Column",
            "3️⃣ Map Dataset Hierarchy",
        ]
    )

    # ---------------------------------------------------------
    # 1) group_dataset_by_fields
    # ---------------------------------------------------------
    with tab_group:
        st.header("Group Dataset by Fields")

        col1, col2 = st.columns(2)

        with col1:
            field_name_new = st.text_input("Field Name New (software)")
            category_name = st.text_input("Category Name (software_category)")

        fields_all = list(DATASET.keys())

        with col2:
            fields_to_combine = st.multiselect(
                f"Fields to combine into '{field_name_new}'",
                options=fields_all,
            )
            fields_other = st.multiselect(
                "Fields to insert",
                options=fields_all,
            )

        if st.button("Group Dataset", key="btn_group_dataset_by_fields"):
            dataset_and_maps = []

            for field in fields_to_combine:
                mapping_option = {}
                mapping_option[field_name_new] = field

                for field_other in fields_other:
                    mapping_option[field_other] = field_other

                dataset_and_maps.append((DATASET, mapping_option))

            axes = [category_name, field_name_new] + fields_other
            DATASET_STACKED = group_dataset_by_fields(
                datasets=dataset_and_maps,
                stack_by={category_name: field_name_new},
                axes=axes,
            )

            st.divider()
            st.subheader(f"✅ Group Dataset by Fields: {category_name}")

            m1, m2 = st.columns(2)
            m1.metric("Rows (Original)", len(DATASET[fields_all[0]]))
            m2.metric("Rows (Stacked)", len(DATASET_STACKED[category_name]))

            st.dataframe(DATASET_STACKED, use_container_width=True)

    # ---------------------------------------------------------
    # 2) map_dataset_column
    # ---------------------------------------------------------
    with tab_map:
        st.header("Map Dataset Column")

        col1, col2 = st.columns(2)

        with col1:
            field_from = st.selectbox(
                "Field From)",
                options=fields_all,
                index=0,
            )
            field_to = st.text_input(
                "Field To",
            )

        with col2:
            mapping_option = st.selectbox(
                "Select Mapping Dictionary",
                ["COUNTRY_TO_CONTINENT", "Create New Map"],
            )
            mapping_dict = {}

        if mapping_option == "COUNTRY_TO_CONTINENT":
            mapping_dict = COUNTRY_TO_CONTINENT
        if mapping_option == "Create New Map":
            st.caption("Write your mapper below:")
            mapping_example = """{
    "USA": "North America",
    "Germany": "Europe",
    "Japan": "Asia",
}"""
            mapping_input = st.text_area(
                "Custom Dictionary",
                value=mapping_example,
                height=200,
            )
            try:
                if mapping_input.strip():
                    mapping_dict = ast.literal_eval(mapping_input)
            except Exception as e:
                st.error(f"Error parsing dictionary: {e}")

        if st.button("Apply Mapping", key="btn_map_dataset_column"):
            DATASET_MAPPED = map_dataset_column(
                dataset=DATASET,
                field_from=field_from,
                field_to=field_to,
                mapping=mapping_dict,
            )

            st.divider()
            st.subheader(f"✅ Map Dataset Column: {field_to}")

            m1, m2 = st.columns(2)
            m1.metric("Rows (Original)", len(DATASET[fields_all[0]]))
            m2.metric("Rows (Mapped)", len(DATASET_MAPPED[field_to]))

            st.dataframe(DATASET_MAPPED, use_container_width=True)

    # ---------------------------------------------------------
    # 3) map_dataset_hierarchy
    # ---------------------------------------------------------
    with tab_hierarchy:
        st.header("Map Hierarchy")

        col1, col2 = st.columns(2)

        with col1:
            field_parent = st.selectbox(
                "Field Parent",
                options=fields_all,
                index=0,
            )
            field_child = st.selectbox(
                "Field Child",
                options=fields_all,
                index=1,
            )

        with col2:
            hierarchy_option = st.selectbox(
                "Select Hierarchy Map",
                ["TECHNIQUE_TO_TECHNIQUESUB", "Create New Map"],
            )
            hierarchy_dict = {}

        # Handle Map Logic
        if hierarchy_option == "TECHNIQUE_TO_TECHNIQUESUB":
            hierarchy_dict = TECHNIQUE_TO_TECHNIQUESUB
        if hierarchy_option == "Create New Map":
            st.caption("Define valid children for each parent:")
            hierarchy_example = """{
    "3D Scanning": [
        "Laser Scanning", 
        "RGB-D Imaging", 
        "Real-Time Volumetric Capture",
    ],
    "Image-Based Techniques": [
        "Photogrammetry", 
        "Spherical Imaging",
    ],
}"""
            hierarchy_input = st.text_area(
                "Hierarchy Dictionary",
                value=hierarchy_example,
                height=200,
            )
            try:
                if hierarchy_input.strip():
                    hierarchy_dict = ast.literal_eval(hierarchy_input)
            except Exception as e:
                st.error(f"Error parsing dictionary: {e}")

        if st.button("Apply Mapping", key="btn_hierarchy"):
            DATASET_HIERARCHY = map_dataset_hierarchy(
                dataset=DATASET,
                field_parent=field_parent,
                field_child=field_child,
                mapping=hierarchy_dict,
            )

            st.divider()
            st.subheader(f"✅ Map Dataset Hierarchy: {field_parent} -> {field_child}")

            m1, m2 = st.columns(2)
            m1.metric("Rows (Original)", len(DATASET[fields_all[0]]))
            m2.metric("Rows (Hierarchy)", len(DATASET_HIERARCHY[field_parent]))

            st.dataframe(DATASET_HIERARCHY, use_container_width=True)
