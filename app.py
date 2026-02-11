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
    e1, e2 = st.columns([0.7, 0.3])
    with e1:
        upload_file = st.file_uploader("Upload csv", type="csv")
    with e2:
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
            e1, e2 = st.columns(2)

            field_name_new = e1.text_input("Field Name New", "software")
            category_name = e1.text_input("Category Name", "software_category")
            fields_to_combine = e2.multiselect(
                f"Fields to combine into '{field_name_new}'", options=fields_all
            )
            fields_other = e2.multiselect("Fields to insert", options=fields_all)

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
            e1, e2 = st.columns(2)

            field_from = e1.selectbox("Field From", fields_all)
            field_to = e2.text_input("Field To", "continent")
            map_mode = e1.selectbox("Mapping", ["COUNTRY_TO_CONTINENT", "Custom"])

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
            e1, e2 = st.columns(2)
            field_parent = e1.selectbox("Parent Field", fields_all)
            field_child = e2.selectbox("Child Field", fields_all)
            hier_mode = e1.selectbox("Mapping", ["TECHNIQUE_TO_TECHNIQUESUB", "Custom"])

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

        st.write("🝖 Filter Values (e.g., software != ' ')")
        if "filter_values_num" not in st.session_state:
            st.session_state["filter_values_num"] = 1

        filter_values = []
        for i in range(st.session_state["filter_values_num"]):
            a1, a2, a3 = st.columns(3)

            f_v_field = a1.selectbox(
                f"Field {i+1}", options=fields_available, key=f"field_{i}"
            )
            f_v_values = a3.text_input(f"Value", key=f"values_{i}")
            f_v_operation = a2.selectbox(
                f"Operation",
                options=["==", "!=", ">=", ">", "<=", "<", "="],
                key=f"operation_{i}",
            )

            if f_v_values:
                filter_values.append(f"{f_v_field} {f_v_operation} {f_v_values}")

        aa1, aa2, _, _ = st.columns([1, 1, 2, 2])
        if aa1.button("➕ Add"):
            st.session_state["filter_values_num"] += 1
            st.rerun()
        if aa2.button("➖ Remove") and st.session_state["filter_values_num"] > 1:
            st.session_state["filter_values_num"] -= 1
            st.rerun()

        apply_filter_values = st.checkbox(
            "**Apply Filter Values**", value=False, key="apply_filter_values"
        )

        st.write("🝖 Filter Count (e.g., count >= 5)")
        b1, b2, b3 = st.columns(3)
        f_c_field = b1.selectbox("Field", options=["count"])
        f_c_value = b3.number_input("Value", min_value=0, value=0, step=1)
        f_c_operation = b2.selectbox(
            "Operation", options=["==", "!=", ">=", ">", "<=", "<", "="]
        )
        filter_count = f"{f_c_field} {f_c_operation} {f_c_value}"
        apply_filter_count = st.checkbox(
            "**Apply Filter Count**", value=False, key="apply_filter_count"
        )

        c1, c2, c3 = st.columns(3)
        x_axis = c1.selectbox("X-axis", options=fields_available)
        y_axis = c2.selectbox("Y-axis", options=["count"])
        z_axis = c3.selectbox("Z-axis (Optional)", options=[None] + fields_available)

        d1, d2 = st.columns(2)
        orientation = d1.selectbox("Orientation", options=["v", "h"])
        coloring_field = d2.selectbox("Coloring Field", options=fields_available)

        e1, e2, e3, e4 = st.columns(4)
        color_mapping = e1.checkbox("Color Mapping", value=False)
        bar_borders = e2.checkbox("Bar Borders", value=False)
        bar_numbers = e3.checkbox("Bar Numbers", value=True)
        grids = e4.checkbox("Grids", value=True)

        if st.button("Generate Chart"):
            fig = bar_1D(
                dataset=dataset_selected,
                fields=[fields],
                filter_values=filter_values if apply_filter_values else None,
                filter_count=filter_count if apply_filter_count else None,
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
