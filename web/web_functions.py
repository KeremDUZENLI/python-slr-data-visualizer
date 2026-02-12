import streamlit as st


def bar_1D_web(fields_available):
    params = {}

    st.write("**Fields**")
    selected_fields = st.multiselect(
        "Select Fields",
        options=fields_available,
        key="bar_1d_fields",
    )
    params["fields"] = selected_fields
    st.divider()

    st.write("**Filter Values**")
    if "bar_1d_filter_values_num" not in st.session_state:
        st.session_state["bar_1d_filter_values_num"] = 1

    filter_values = []
    for i in range(st.session_state["bar_1d_filter_values_num"]):
        a1, a2, a3 = st.columns(3)

        f_v_field = a1.selectbox(
            f"Field {i+1}",
            options=selected_fields,
            key=f"bar_1d_fv_field_{i}",
        )
        f_v_operation = a2.selectbox(
            "Operation",
            ["==", "!=", ">=", ">", "<=", "<", "="],
            key=f"bar_1d_fv_op_{i}",
        )
        f_v_values = a3.text_input(
            "Value",
            value=" ",
            key=f"bar_1d_fv_val_{i}",
        )
        if f_v_values:
            filter_values.append(f"{f_v_field} {f_v_operation} {f_v_values}")

    aa1, aa2, _, _ = st.columns([1, 1, 2, 2])
    if aa1.button("➕ Add", key="bar_1d_add_fv"):
        st.session_state["bar_1d_filter_values_num"] += 1
        st.rerun()
    if (
        aa2.button("➖ Remove", key="bar_1d_rem_fv")
        and st.session_state["bar_1d_filter_values_num"] > 1
    ):
        st.session_state["bar_1d_filter_values_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox(
        "Apply Filter Values",
        key="bar_1d_app_fv",
    )
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    b1, b2, b3 = st.columns(3)
    f_c_field = b1.selectbox(
        "Field",
        ["count"],
        key="bar_1d_fc_f",
    )
    f_c_operation = b2.selectbox(
        "Operation",
        ["==", "!=", ">=", ">", "<=", "<", "="],
        key="bar_1d_fc_o",
    )
    f_c_value = b3.number_input(
        "Value",
        min_value=0,
        value=0,
        step=1,
        key="bar_1d_fc_v",
    )

    apply_filter_count = st.checkbox("Apply Filter Count", key="bar_1d_app_fc")
    params["filter_count"] = (
        f"{f_c_field} {f_c_operation} {f_c_value}" if apply_filter_count else None
    )
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis", options=selected_fields, key="bar_1d_x")
    params["y_axis"] = c2.selectbox("Y-axis", options=["count"], key="bar_1d_y")
    params["z_axis"] = c3.selectbox(
        "Z-axis (Optional)", options=[None] + selected_fields, key="bar_1d_z"
    )
    st.divider()

    st.write("**Other Options**")
    d1, d2 = st.columns(2)
    params["orientation"] = d1.selectbox(
        "Orientation",
        ["vertical", "horizontal"],
        key="bar_1d_orient",
    )
    params["coloring_field"] = d2.selectbox(
        "Coloring Field",
        options=selected_fields,
        key="bar_1d_color",
    )
    st.divider()

    st.write("**Graph Options**")
    e1, e2, e3, e4 = st.columns(4)
    params["color_mapping"] = e1.checkbox(
        "Color Mapping",
        False,
        key="bar_1d_color_mapping",
    )
    params["bar_borders"] = e2.checkbox(
        "Bar Borders",
        False,
        key="bar_1d_bar_borders",
    )
    params["bar_numbers"] = e3.checkbox(
        "Bar Numbers",
        True,
        key="bar_1d_bar_num",
    )
    params["grids"] = e4.checkbox(
        "Grids",
        True,
        key="bar_1d_grid",
    )
    st.divider()

    st.write("**Extras**")
    f1, _, _ = st.columns(3)
    params["labels_extra"] = f1.selectbox(
        "Labels Extra",
        options=[None] + selected_fields,
        key="bar_1d_labels_extra",
    )
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        g1, g2, g3, g4 = st.columns(4)
        title = g1.text_input("Chart Title", key="bar_1d_lbl_t")
        xlabel = g2.text_input("X-axis Label", key="bar_1d_lbl_x")
        ylabel = g3.text_input("Y-axis Label", key="bar_1d_lbl_y")
        rotation = g4.number_input(
            "Label Rotation",
            min_value=0,
            max_value=360,
            value=45,
            step=5,
            key="bar_1d_lbl_r",
        )
        labels_spec = {
            "title": title,
            "x_label": xlabel,
            "y_label": ylabel,
            "rotation": rotation,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="bar_1d_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Legends**")
    with st.expander("Legend Labels", expanded=False):
        h1, h2, h3, h4 = st.columns(4)
        l_source = h1.selectbox(
            "Source",
            options=["dataset", "custom"],
            key="bar_1d_leg_src",
        )
        l_values = h2.selectbox(
            "Labels Values",
            options=selected_fields,
            key="bar_1d_leg_val",
        )
        l_coloring_field = h3.selectbox(
            "Coloring Field",
            options=selected_fields,
            key="bar_1d_leg_col",
        )
        l_casetype = h4.selectbox(
            "Case Type",
            options=["title", "upper", "original"],
            key="bar_1d_leg_case",
        )

        i1, i2 = st.columns(2)
        l_title = i1.text_input(
            "Legend Title",
            key="bar_1d_leg_t",
        )
        l_loc = i2.selectbox(
            "Legend Location",
            options=["upper left", "upper right", "lower left", "lower right"],
            key="bar_1d_leg_l",
        )

        st.caption("**BBox Anchor (Advanced Positioning)**: (x, y, width, height)")
        j1, j2, j3, j4 = st.columns(4)
        bbox_x = j1.number_input(
            "X (Horizontal)",
            value=1.00,
            step=0.05,
            key="bar_1d_bx",
        )
        bbox_y = j2.number_input(
            "Y (Vertical)",
            value=1.00,
            step=0.05,
            key="bar_1d_by",
        )
        bbox_w = j3.number_input(
            "Width",
            value=0.30,
            step=0.05,
            key="bar_1d_bw",
        )
        bbox_h = j4.number_input(
            "Height",
            value=1.00,
            step=0.05,
            key="bar_1d_bh",
        )

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
        "Apply Legends Config",
        value=False,
        key="bar_1d_app_leg",
    )
    params["legends_config"] = legends_config if apply_legends_config else None

    used_fields = [params["x_axis"]]
    if params["z_axis"]:
        used_fields.append(params["z_axis"])
    if params["coloring_field"]:
        used_fields.append(params["coloring_field"])
    if params["labels_extra"]:
        used_fields.append(params["labels_extra"])
    if apply_legends_config:
        if l_values:
            used_fields.append(l_values)
        if l_coloring_field:
            used_fields.append(l_coloring_field)

    params["fields"] = list(set(params["fields"] + used_fields))

    return params
