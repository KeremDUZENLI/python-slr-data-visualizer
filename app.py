import ast, json, io, os
import streamlit as st

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

from setup.setup_functions import (
    bar_1D,
)

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
        elif file_name in st.session_state["data_versions"]:
            st.warning(f"⚠️ Already Loaded: {file_name}")
        else:
            st.error(f"❌ Not Loaded: {file_name}")

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
                st.rerun()

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

        st.write("**Fields**")
        fields = st.multiselect("Select Fields", options=fields_available)
        st.divider()

        st.write("**Filter Values**")
        if "filter_values_num" not in st.session_state:
            st.session_state["filter_values_num"] = 1
        filter_values = []
        for i in range(st.session_state["filter_values_num"]):
            a1, a2, a3 = st.columns(3)

            f_v_field = a1.selectbox(f"Field {i+1}", options=fields, key=f"field_{i}")
            f_v_values = a3.text_input(f"Value", value=" ", key=f"values_{i}")
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
            "Apply Filter Values", value=False, key="apply_filter_values"
        )
        st.divider()

        st.write("**Filter Count**")
        b1, b2, b3 = st.columns(3)
        f_c_field = b1.selectbox("Field", options=["count"])
        f_c_value = b3.number_input("Value", min_value=0, value=0, step=1)
        f_c_operation = b2.selectbox(
            "Operation", options=["==", "!=", ">=", ">", "<=", "<", "="]
        )
        filter_count = f"{f_c_field} {f_c_operation} {f_c_value}"
        apply_filter_count = st.checkbox(
            "Apply Filter Count", value=False, key="apply_filter_count"
        )
        st.divider()

        st.write("**Axes**")
        c1, c2, c3 = st.columns(3)
        x_axis = c1.selectbox("X-axis", options=fields)
        y_axis = c2.selectbox("Y-axis", options=["count"])
        z_axis = c3.selectbox("Z-axis (Optional)", options=[None] + fields)
        st.divider()

        st.write("**Other Options**")
        d1, d2 = st.columns(2)
        orientation = d1.selectbox("Orientation", options=["vertical", "horizontal"])
        coloring_field = d2.selectbox("Coloring Field", options=fields)
        st.divider()

        st.write("**Graph Options**")
        e1, e2, e3, e4 = st.columns(4)
        color_mapping = e1.checkbox("Color Mapping", value=False)
        bar_borders = e2.checkbox("Bar Borders", value=False)
        bar_numbers = e3.checkbox("Bar Numbers", value=True)
        grids = e4.checkbox("Grids", value=True)
        st.divider()

        st.write("**Extras**")
        f1, _, _ = st.columns(3)
        labels_extra = f1.selectbox(f"Labels Extra", options=[None] + fields)
        st.divider()

        st.write("**Labels**")
        with st.expander("Chart Labels", expanded=False):
            g1, g2, g3, g4 = st.columns(4)
            title = g1.text_input("Chart Title")
            xlabel = g2.text_input("X-axis Label")
            ylabel = g3.text_input("Y-axis Label")
            rotation = g4.number_input(
                "Label Rotation", min_value=0, max_value=360, value=45, step=5
            )
            labels_spec = {
                "title": title,
                "x_label": xlabel,
                "y_label": ylabel,
                "rotation": rotation,
            }
        apply_labels_spec = st.checkbox(
            "Apply Labels Spec", value=False, key="apply_labels_spec"
        )
        st.divider()

        st.write("**Legends**")
        with st.expander("Legend Labels", expanded=False):
            h1, h2, h3, h4 = st.columns(4)
            l_source = h1.selectbox(
                "Legend Source",
                options=["dataset", "custom"],
                key="legend_source",
            )
            l_values = h2.selectbox(
                "Labels Values",
                options=fields,
                key="legend_values",
            )
            l_coloring_field = h3.selectbox(
                "Coloring Field",
                options=fields,
                key="legend_coloring_field",
            )
            l_casetype = h4.selectbox(
                "Case Type",
                options=["title", "upper", "original"],
                key="legend_casetype",
            )

            i1, i2, i3 = st.columns(3)
            l_title = i1.text_input("Legend Title")
            l_loc = i2.selectbox(
                "Legend Location",
                options=["upper left", "upper right", "lower left", "lower right"],
                key="legend_loc",
            )

            st.caption("**BBox Anchor (Advanced Positioning)**: (x, y, width, height)")
            j1, j2, j3, j4 = st.columns(4)
            bbox_x = j1.number_input("X (Horizontal)", value=1.00, step=0.05)
            bbox_y = j2.number_input("Y (Vertical)", value=1.00, step=0.05)
            bbox_w = j3.number_input("Width", value=0.30, step=0.05)
            bbox_h = j4.number_input("Height", value=1.00, step=0.05)

            legends_config = [
                {
                    "source": l_source,
                    "values": l_values,
                    "coloring_field": l_coloring_field,
                    "legend_spec": {
                        "title": l_title,
                        "loc": l_loc,
                        "bbox": (bbox_x, bbox_y, bbox_w, bbox_h),
                    },
                    "casetype": l_casetype,
                }
            ]
        apply_legends_config = st.checkbox(
            "Apply Legends Config", value=False, key="apply_legends_config"
        )
        st.divider()

        st.write("**Draw Chart**")
        if st.button("Draw Chart"):
            fig, legends, extra_artists = bar_1D(
                dataset=dataset_selected,
                fields=fields,
                filter_values=filter_values if apply_filter_values else None,
                filter_count=filter_count if apply_filter_count else None,
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
                labels_spec=labels_spec if apply_labels_spec else None,
                legends_config=legends_config if apply_legends_config else None,
                save_name=None,
            )
            st.pyplot(fig)
            st.session_state["generated_fig"] = fig
            st.session_state["generated_legends"] = legends
            st.session_state["generated_extra_artists"] = extra_artists
        st.divider()

        st.write("**Save Chart**")
        if "generated_fig" in st.session_state:
            s1, s2 = st.columns(2)
            save_filename = s1.text_input("Filename", "chart")
            save_fileformat = s2.selectbox("Format", ["png", "jpg", "svg", "pdf"])
            buffer = io.BytesIO()

            saved_legends = st.session_state.get("generated_legends", []) or []
            saved_extras = st.session_state.get("generated_extra_artists", []) or []
            all_artists = saved_legends + saved_extras

            st.session_state["generated_fig"].savefig(
                buffer,
                format=save_fileformat,
                dpi=300,
                bbox_inches="tight",
                bbox_extra_artists=all_artists,
            )
            buffer.seek(0)

            st.download_button(
                label="Save Chart",
                data=buffer,
                file_name=f"{save_filename}.{save_fileformat}",
                mime=f"image/{save_fileformat}",
            )
        else:
            st.info("ℹ️ Please generate a chart first to enable downloading.")
