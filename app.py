import ast, os, json
import streamlit as st

from config.maps import COUNTRY_TO_CONTINENT, TECHNIQUE_TO_TECHNIQUESUB
from input._1_read import read_dataset
from input._2_prepare import (
    group_dataset_by_fields,
    map_dataset_column,
    map_dataset_hierarchy,
)
from setup.setup_functions import bar_1D

st.set_page_config(layout="wide", page_title="Data Visualizer")

if "data_versions" not in st.session_state:
    st.session_state["data_versions"] = {}

st.sidebar.title("Navigator")
step = st.sidebar.radio("Go to Step:", ["1. Data Preparation", "2. Chart Creation"])
st.sidebar.divider()

if step == "1. Data Preparation":
    st.title("🛠️ Step 1: Data Preparation")
    c1, c2 = st.columns([0.7, 0.3])
    with c1:
        upload_file = st.file_uploader("Upload csv", type="csv")
    with c2:
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
        else:
            st.error(f"❌ Not Loaded: {file_name}")

    if st.session_state["data_versions"]:
        st.divider()
        st.subheader("Data Manipulation")

        input_name = st.selectbox(
            "Select csv", options=list(st.session_state["data_versions"].keys())
        )
        DATASET = st.session_state["data_versions"][input_name]
        fields_all = list(DATASET.keys())

        tab_group, tab_map, tab_hier = st.tabs(
            [
                "1️⃣ Group Dataset by Fields",
                "2️⃣ Map Dataset Column",
                "3️⃣ Map Dataset Hierarchy",
            ]
        )

        with tab_group:
            c1, c2 = st.columns(2)

            field_name_new = c1.text_input("Field Name New", "software")
            category_name = c1.text_input("Category Name", "software_category")
            fields_to_combine = c2.multiselect(
                f"Fields to combine into '{field_name_new}'", options=fields_all
            )
            fields_other = c2.multiselect("Fields to insert", options=fields_all)

            save_name_group = st.text_input(
                label="Save As",
                value="dataset_grouped",
                key="name_group",
            )

            if st.button("Save Changes", key="btn_save_group"):
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
                st.success(f"✅ Saved dataset: {save_name_group}")
                st.dataframe(result, use_container_width=True)

        with tab_map:
            c1, c2 = st.columns(2)

            field_from = c1.selectbox("Field From", fields_all)
            field_to = c2.text_input("Field To", "continent")
            map_mode = c1.selectbox("Mapping", ["COUNTRY_TO_CONTINENT", "Custom"])

            mapping = {}
            if map_mode == "COUNTRY_TO_CONTINENT":
                example_map = json.dumps(COUNTRY_TO_CONTINENT, indent=4)
                txt = st.text_area("View/Edit Map", value=example_map, height=250)
                try:
                    mapping = ast.literal_eval(txt)
                except:
                    st.error("❌ Invalid Dictionary Format")
            if map_mode == "Custom":
                example_text = (
                    '{\n    "USA": "North America",\n    "Germany": "Europe"\n}'
                )
                txt = st.text_area("Custom Map", value=example_text, height=250)
                try:
                    mapping = ast.literal_eval(txt)
                except:
                    st.error("❌ Invalid Dictionary Format")

            save_name_map = st.text_input(
                label="Save As",
                value="dataset_mapped_by_col",
                key="name_map",
            )

            if st.button("Save Changes", key="btn_save_map"):
                if mapping:
                    result = map_dataset_column(
                        dataset=DATASET,
                        field_from=field_from,
                        field_to=field_to,
                        mapping=mapping,
                    )
                    st.session_state["data_versions"][save_name_map] = result
                    st.success(f"✅ Saved dataset: {save_name_map}")
                    st.dataframe(result, use_container_width=True)

        with tab_hier:
            c1, c2 = st.columns(2)
            field_parent = c1.selectbox("Parent Field", fields_all)
            field_child = c2.selectbox("Child Field", fields_all)
            hier_mode = c1.selectbox("Mapping", ["TECHNIQUE_TO_TECHNIQUESUB", "Custom"])

            mapping = {}
            if hier_mode == "TECHNIQUE_TO_TECHNIQUESUB":
                example_map = json.dumps(TECHNIQUE_TO_TECHNIQUESUB, indent=4)
                txt = st.text_area("View/Edit Map", value=example_map, height=250)
                try:
                    mapping = ast.literal_eval(txt)
                except:
                    st.error("❌ Invalid Dictionary Format")
            if hier_mode == "Custom":
                example_text = '{\n    "Parent": ["Child1", "Child2"]\n}'
                txt = st.text_area("Custom Map", value=example_text, height=250)
                try:
                    mapping = ast.literal_eval(txt)
                except:
                    st.error("❌ Invalid Dictionary Format")

            save_name_hier = st.text_input(
                label="Save As",
                value="dataset_mapped_by_hier",
                key="name_hier",
            )

            if st.button("Save Changes", key="btn_apply_hier"):
                if mapping:
                    result = map_dataset_hierarchy(
                        dataset=DATASET,
                        field_parent=field_parent,
                        field_child=field_child,
                        mapping=mapping,
                    )
                    st.session_state["data_versions"][save_name_hier] = result
                    st.success(f"✅ Saved dataset: {save_name_hier}")
                    st.dataframe(result, use_container_width=True)

if step == "2. Chart Creation":
    st.title("📊 Step 2: Chart Creation")

    if not st.session_state["data_versions"]:
        st.warning("⚠️ No data available. Please go to Data Preparation")
    else:
        dataset = st.sidebar.selectbox(
            "Select Dataset", options=list(st.session_state["data_versions"].keys())
        )
        dataset_selected = st.session_state["data_versions"][dataset]
        fields_available = list(dataset_selected.keys())

        st.subheader(f"Dataset: {dataset}")
        st.divider()

        fields = st.multiselect("Fields", options=fields_available)
        filter_values = st.text_area(
            "Filter Values (e.g., software != ' ')", height=100
        )
        filter_count = st.text_area("Filter Count (e.g., count >= 5)", height=100)
        a1, a2, a3 = st.columns(3)
        x_axis = a1.selectbox("X-axis", options=fields_available)
        y_axis = a2.selectbox("Y-axis", options=["count"])
        z_axis = a3.selectbox("Z-axis (Optional)", options=[None] + fields_available)
        b1, b2 = st.columns(2)
        orientation = b1.selectbox("Orientation", options=["v", "h"])
        coloring_field = b2.selectbox("Coloring Field", options=fields_available)
        c1, c2, c3, c4 = st.columns(4)
        color_mapping = c1.checkbox("Color Mapping", value=False)
        bar_borders = c2.checkbox("Bar Borders", value=False)
        bar_numbers = c3.checkbox("Bar Numbers", value=True)
        grids = c4.checkbox("Grids", value=True)

        if st.button("Generate Chart"):
            fig = bar_1D(
                dataset=dataset_selected,
                fields=[fields],
                filter_values=filter_values,
                filter_count=filter_count,
                x_axis=fields,
                y_axis="count",
                z_axis=None,
                orientation=orientation,
                coloring_field=coloring_field,
                color_mapping=color_mapping,
                bar_borders=bar_borders,
                bar_numbers=bar_numbers,
                grids=grids,
                labels_extra=None,
                labels_spec={
                    "title": "Total Studies Per Year",
                    "x_label": "Year",
                    "y_label": "Number of Studies",
                    "rotation": 45,
                },
                legends_config=None,
                save_name=None,
            )
            st.pyplot(fig)
