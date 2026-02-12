import ast
import json
import io
import os
import streamlit as st

# --- Local Imports ---
from config.maps import COUNTRY_TO_CONTINENT, TECHNIQUE_TO_TECHNIQUESUB
from input._1_read import read_dataset
from input._2_prepare import (
    group_dataset_by_fields,
    map_dataset_column,
    map_dataset_hierarchy,
)
from setup.setup_functions import bar_1D

# --- Page Config ---
st.set_page_config(layout="wide", page_title="Data Visualizer")

# --- Session State Init ---
if "data_versions" not in st.session_state:
    st.session_state["data_versions"] = {}

# --- Navigation ---
st.sidebar.title("Navigator")
step = st.sidebar.radio("Go to Step:", ["1. Data Preparation", "2. Chart Creation"])
st.sidebar.divider()

# ==============================================================================
# STEP 1: DATA PREPARATION
# ==============================================================================
if step == "1. Data Preparation":
    st.title("🛠️ Step 1: Data Preparation")

    # 1. Upload / Load Section
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

    # 2. Manipulation Workbench
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

        # --- Tab: Grouping ---
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
                st.rerun()

        # --- Tab: Mapping ---
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
                    st.rerun()

        # --- Tab: Hierarchy ---
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

            if st.button("Save Changes", key="btn_save_hier"):
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
                    st.rerun()

# ==============================================================================
# STEP 2: CHART CREATION
# ==============================================================================
if step == "2. Chart Creation":
    st.title("📊 Step 2: Chart Creation")

    if not st.session_state["data_versions"]:
        st.warning("⚠️ No data available. Please go to Data Preparation")
    else:
        # 1. Dataset Selection
        dataset = st.sidebar.selectbox(
            "Select Dataset", options=list(st.session_state["data_versions"].keys())
        )
        dataset_selected = st.session_state["data_versions"][dataset]
        fields_available = list(dataset_selected.keys())

        st.subheader(f"Dataset: {dataset}")
        st.divider()

        # 2. Fields Selection
        st.write("**Fields**")
        fields = st.multiselect("Select Fields", options=fields_available)
        st.divider()

        # 3. Filter Values (Dynamic Loop)
        st.write("**Filter Values**")
        if "filter_values_num" not in st.session_state:
            st.session_state["filter_values_num"] = 1

        filter_values = []
        for i in range(st.session_state["filter_values_num"]):
            a1, a2, a3 = st.columns(3)
            # Use 'fields' (selected above) for options
            f_v_field = a1.selectbox(f"Field {i+1}", options=fields, key=f"field_{i}")
            f_v_operation = a2.selectbox(
                f"Operation",
                options=["==", "!=", ">=", ">", "<=", "<", "="],
                key=f"operation_{i}",
            )
            # Default value is a space string
            f_v_values = a3.text_input(f"Value", value=" ", key=f"values_{i}")

            if f_v_values and f_v_values.strip():
                filter_values.append(f"{f_v_field} {f_v_operation} {f_v_values}")

        aa1, aa2, _, _ = st.columns([1, 1, 2, 2])
        if aa1.button("➕ Add"):
            st.session_state["filter_values_num"] += 1
            st.rerun()
        if aa2.button("➖ Remove") and st.session_state["filter_values_num"] > 1:
            st.session_state["filter_values_num"] -= 1
            st.rerun()

        apply_filter_values = st.checkbox(
            "Apply Filter Values", value=False, key="apply_filter_values"
        )
        st.divider()

        # 4. Filter Count
        st.write("**Filter Count**")
        b1, b2, b3 = st.columns(3)
        f_c_field = b1.selectbox("Field", options=["count"])
        f_c_operation = b2.selectbox(
            "Operation", options=["==", "!=", ">=", ">", "<=", "<", "="]
        )
        f_c_value = b3.number_input("Value", min_value=0, value=0, step=1)

        filter_count = f"{f_c_field} {f_c_operation} {f_c_value}"
        apply_filter_count = st.checkbox(
            "Apply Filter Count", value=False, key="apply_filter_count"
        )
        st.divider()

        # 5. Axes Selection
        st.write("**Axes**")
        c1, c2, c3 = st.columns(3)
        x_axis = c1.selectbox("X-axis", options=fields)
        y_axis = c2.selectbox("Y-axis", options=["count"])
        z_axis = c3.selectbox("Z-axis (Optional)", options=[None] + fields)
        st.divider()

        # 6. Other Options
        st.write("**Other Options**")
        d1, d2 = st.columns(2)
        orientation = d1.selectbox("Orientation", options=["v", "h"])
        coloring_field = d2.selectbox("Coloring Field", options=fields)
        st.divider()

        # 7. Graph Options
        st.write("**Graph Options**")
        e1, e2, e3, e4 = st.columns(4)
        color_mapping = e1.checkbox("Color Mapping", value=False)
        bar_borders = e2.checkbox("Bar Borders", value=False)
        bar_numbers = e3.checkbox("Bar Numbers", value=True)
        grids = e4.checkbox("Grids", value=True)
        st.divider()

        # 8. Appearance (Labels & Legend) - GENERIC IMPLEMENTATION
        st.write("**Appearance**")

        # Labels Configuration
        with st.expander("📝 Labels & Titles", expanded=False):
            l1, l2 = st.columns(2)
            l_title = l1.text_input("Chart Title", value=f"Count by {x_axis}")
            l_rot = l2.number_input("X Label Rotation", value=45, step=5)

            l3, l4, l5 = st.columns(3)
            l_xlabel = l3.text_input("X-Axis Label", value=x_axis)
            l_ylabel = l4.text_input("Y-Axis Label", value="Number of Studies")
            labels_extra = l5.selectbox("Extra Labels Field", options=[None] + fields)

            # Construct the Generic labels_spec dictionary
            labels_spec = {
                "title": l_title,
                "x_label": l_xlabel,
                "y_label": l_ylabel,
                "rotation": l_rot,
            }

        # Legends Configuration
        legends_config = None
        with st.expander("De Legend Configuration", expanded=False):
            show_legend = st.checkbox("Show Legend", value=True)

            if show_legend:
                lg1, lg2 = st.columns(2)
                # Defaults to the coloring field or x-axis
                leg_source = coloring_field if coloring_field else x_axis
                leg_title = lg1.text_input("Legend Title", value=leg_source)
                leg_loc = lg2.selectbox(
                    "Location",
                    ["best", "upper left", "upper right", "lower left", "lower right"],
                    index=0,
                )

                use_bbox = st.checkbox("Place Outside (BBox)", value=True)
                bbox_val = (1.05, 1) if use_bbox else None

                # Construct the Generic legends_config list
                legends_config = [
                    {
                        "source": "dataset",
                        "values": leg_source,
                        "coloring_field": leg_source,
                        "legend_spec": {
                            "title": leg_title,
                            "loc": leg_loc,
                            "bbox_to_anchor": bbox_val,
                        },
                        "casetype": "title",
                    }
                ]
        st.divider()

        # 9. Draw Chart Button
        st.write("**Draw Chart**")
        if st.button("Generate Chart"):
            # A. Calculate which fields are actually used (Axes + Coloring + Extra)
            # This prevents passing the entire 'fields' list which breaks aggregation.
            chart_fields = [x_axis]
            if z_axis:
                chart_fields.append(z_axis)
            if coloring_field:
                chart_fields.append(coloring_field)
            if labels_extra:
                chart_fields.append(labels_extra)
            # Remove duplicates
            chart_fields = list(set(chart_fields))

            # B. Prepare Filters
            f_vals_clean = (
                [f.strip() for f in filter_values if f.strip()]
                if apply_filter_values
                else None
            )
            f_count_clean = filter_count if apply_filter_count else None

            # C. Call the bar_1D function
            fig = bar_1D(
                dataset=dataset_selected,
                fields=chart_fields,  # <--- Fixed: Only passing relevant fields
                filter_values=f_vals_clean,
                filter_count=f_count_clean,
                x_axis=x_axis,
                y_axis=y_axis,
                z_axis=z_axis,
                orientation=orientation,
                coloring_field=coloring_field,
                color_mapping=color_mapping,
                bar_borders=bar_borders,
                bar_numbers=bar_numbers,
                grids=grids,
                labels_extra=labels_extra,
                labels_spec=labels_spec,  # <--- Passed dynamically
                legends_config=legends_config,  # <--- Passed dynamically
                save_name=None,
            )

            # D. Display and Store in Session State
            st.pyplot(fig)
            st.session_state["generated_fig"] = fig

        st.divider()

        # 10. Save Chart Section
        st.write("**Save Chart**")
        if "generated_fig" in st.session_state:
            s1, s2 = st.columns(2)
            save_filename = s1.text_input("Filename", "chart")
            file_fmt = s2.selectbox("Format", ["png", "pdf", "svg", "jpg"])

            # Create an in-memory buffer
            buffer = io.BytesIO()

            # Save the figure to the buffer
            st.session_state["generated_fig"].savefig(
                buffer,
                format=file_fmt,
                dpi=300,
                bbox_inches="tight",
            )
            # Rewind buffer
            buffer.seek(0)

            st.download_button(
                label=f"💾 Download {file_fmt.upper()}",
                data=buffer,
                file_name=f"{save_filename}.{file_fmt}",
                mime=f"image/{file_fmt}",
            )
        else:
            st.info("ℹ️ Please generate a chart first to enable downloading.")

        st.divider()
