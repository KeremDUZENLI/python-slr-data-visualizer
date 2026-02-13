import streamlit as st
import ast, json, os

from config.maps import (
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


def data_preparation_web():
    st.title("🛠️ Step 1: Data Preparation")

    m1, m2 = st.columns([0.7, 0.3])
    with m1:
        upload_file = st.file_uploader("Upload csv", type="csv")
    with m2:
        st.write("")
        st.write("")
        st.write("")
        load_example = st.button("Load dataset.example.csv", use_container_width=True)

    if upload_file:
        file_name = upload_file.name
        if file_name not in st.session_state["data_versions"]:
            temp_path = "temp.csv"
            with open(temp_path, "wb") as field:
                field.write(upload_file.getbuffer())

            st.session_state["data_versions"][file_name] = read_dataset(
                csv_path=temp_path
            )
            os.remove(temp_path)
            st.success(f"✅ Loaded: {file_name}")

    if load_example:
        file_name = "dataset.example.csv"
        example_path = "data/dataset.example.csv"

        if file_name not in st.session_state["data_versions"]:
            st.session_state["data_versions"][file_name] = read_dataset(
                csv_path=example_path
            )
            st.success(f"✅ Loaded: {file_name}")
        elif file_name in st.session_state["data_versions"]:
            st.warning(f"⚠️ Already Loaded: {file_name}")
        else:
            st.error(f"❌ Not Loaded: {file_name}")
    st.divider()

    if st.session_state["data_versions"]:
        input_name = st.selectbox(
            "Select csv", options=list(st.session_state["data_versions"].keys())
        )
        DATASET = st.session_state["data_versions"][input_name]
        st.divider()

        st.write("**Data Manipulation**")
        fields_all = list(DATASET.keys())
        tab_group, tab_map, tab_hier = st.tabs(
            [
                "1️⃣ Group Dataset by Fields",
                "2️⃣ Map Dataset Column",
                "3️⃣ Map Dataset Hierarchy",
            ]
        )

        with tab_group:
            m1, m2 = st.columns(2)

            field_name_new = m1.text_input("Field Name New", "software")
            category_name = m1.text_input("Category Name", "software_category")
            fields_to_combine = m2.multiselect(
                f"Fields to combine into '{field_name_new}'", options=fields_all
            )
            fields_other = m2.multiselect("Fields to insert", options=fields_all)

            save_name_group = st.text_input(
                label="Save As",
                value="dataset_grouped",
                key="name_group",
            )

            if st.button("💾 Save Changes", key="btn_save_group"):
                datasets_with_maps = []
                for field in fields_to_combine:
                    map = {field_name_new: field}
                    for field_other in fields_other:
                        map[field_other] = field_other
                    datasets_with_maps.append((DATASET, map))

                result = group_dataset_by_fields(
                    datasets=datasets_with_maps,
                    stack_by={category_name: field_name_new},
                    axes=[category_name, field_name_new] + fields_other,
                )
                st.session_state["data_versions"][save_name_group] = result
                st.session_state["data_manipulation_msg"] = (
                    f"✅ Saved dataset: {save_name_group}"
                )
                st.session_state["preview_dataset"] = save_name_group
                st.rerun()

        with tab_map:
            m1, m2 = st.columns(2)

            field_from = m1.selectbox("Field From", fields_all)
            field_to = m2.text_input("Field To", "continent")
            map_mode = m1.selectbox("Mapping", ["COUNTRY_TO_CONTINENT", "Custom"])

            mapping = {}
            if map_mode == "COUNTRY_TO_CONTINENT":
                map_country = json.dumps(COUNTRY_TO_CONTINENT, indent=4)
                txt_country = st.text_area(
                    "View/Edit Map", value=map_country, height=250
                )
                try:
                    mapping = ast.literal_eval(txt_country)
                except:
                    st.error("❌ Invalid Dictionary Format")
            if map_mode == "Custom":
                txt_example = (
                    '{\n    "USA": "North America",\n    "Germany": "Europe"\n}'
                )
                txt_country = st.text_area("Custom Map", value=txt_example, height=250)
                try:
                    mapping = ast.literal_eval(txt_country)
                except:
                    st.error("❌ Invalid Dictionary Format")

            save_name_map = st.text_input(
                label="Save As",
                value="dataset_mapped_by_col",
                key="name_map",
            )

            if st.button("💾 Save Changes", key="btn_save_map"):
                if mapping:
                    result = map_dataset_column(
                        dataset=DATASET,
                        field_from=field_from,
                        field_to=field_to,
                        mapping=mapping,
                    )
                    st.session_state["data_versions"][save_name_map] = result
                    st.session_state["data_manipulation_msg"] = (
                        f"✅ Saved dataset: {save_name_map}"
                    )
                    st.session_state["preview_dataset"] = save_name_map
                    st.rerun()

        with tab_hier:
            m1, m2 = st.columns(2)

            field_parent = m1.selectbox("Parent Field", fields_all)
            field_child = m2.selectbox("Child Field", fields_all)
            hier_mode = m1.selectbox("Mapping", ["TECHNIQUE_TO_TECHNIQUESUB", "Custom"])

            mapping = {}
            if hier_mode == "TECHNIQUE_TO_TECHNIQUESUB":
                map_hier = json.dumps(TECHNIQUE_TO_TECHNIQUESUB, indent=4)
                txt_hier = st.text_area("View/Edit Map", value=map_hier, height=250)
                try:
                    mapping = ast.literal_eval(txt_hier)
                except:
                    st.error("❌ Invalid Dictionary Format")
            if hier_mode == "Custom":
                txt_example = '{\n    "Parent": ["Child1", "Child2"]\n}'
                txt_hier = st.text_area("Custom Map", value=txt_example, height=250)
                try:
                    mapping = ast.literal_eval(txt_hier)
                except:
                    st.error("❌ Invalid Dictionary Format")

            save_name_hier = st.text_input(
                label="Save As",
                value="dataset_mapped_by_hier",
                key="name_hier",
            )

            if st.button("💾 Save Changes", key="btn_save_hier"):
                if mapping:
                    result = map_dataset_hierarchy(
                        dataset=DATASET,
                        field_parent=field_parent,
                        field_child=field_child,
                        mapping=mapping,
                    )
                    st.session_state["data_versions"][save_name_hier] = result
                    st.session_state["data_manipulation_msg"] = (
                        f"✅ Saved dataset: {save_name_hier}"
                    )
                    st.session_state["preview_dataset"] = save_name_hier
                    st.rerun()
        st.divider()

        st.write("**Preview**")
        if "data_manipulation_msg" in st.session_state:
            st.success(st.session_state["data_manipulation_msg"])
            del st.session_state["data_manipulation_msg"]
        if "preview_dataset" in st.session_state:
            preview_name = st.session_state["preview_dataset"]
            if preview_name in st.session_state["data_versions"]:
                st.dataframe(
                    st.session_state["data_versions"][preview_name],
                    use_container_width=True,
                )
