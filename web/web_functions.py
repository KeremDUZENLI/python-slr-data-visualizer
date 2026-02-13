import streamlit as st


def bar_1D_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="1d_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "1d_fv_num" not in st.session_state:
        st.session_state["1d_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["1d_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"1d_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"1d_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"1d_v_{i}")
        if v:
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="1d_add"):
        st.session_state["1d_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="1d_rem") and st.session_state["1d_fv_num"] > 1:
        st.session_state["1d_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="1d_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="1d_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="1d_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="1d_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="1d_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis", params["fields"], key="1d_x")
    params["y_axis"] = c2.selectbox("Y-axis", ["count"], key="1d_y")
    params["z_axis"] = c3.selectbox(
        "Z-axis (Optional)", [None] + params["fields"], key="1d_z"
    )
    st.divider()

    st.write("**Other Options**")
    c1, c2 = st.columns(2)
    params["orientation"] = c1.selectbox(
        "Orientation", ["vertical", "horizontal"], key="1d_orient"
    )
    params["coloring_field"] = c2.selectbox(
        "Coloring", params["fields"], key="1d_color"
    )
    st.divider()

    st.write("**Graph Options**")
    c1, c2, c3, c4 = st.columns(4)
    params["bar_borders"] = c1.checkbox("Bar Borders", False, key="1d_b")
    params["bar_numbers"] = c2.checkbox("Bar Numbers", True, key="1d_n")
    params["grids"] = c3.checkbox("Grids", True, key="1d_g")
    params["color_mapping"] = c4.checkbox("Color Mapping", False, key="1d_cm")
    st.divider()

    st.write("**Extras**")
    c1, _, _ = st.columns(3)
    params["labels_extra"] = c1.selectbox(
        "Labels Extra", [None] + params["fields"], key="1d_le"
    )
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        c1, c2, c3, c4 = st.columns(4)
        title = c1.text_input("Chart Title", key="bar_1d_lbl_t")
        xlabel = c2.text_input("X-axis Label", key="bar_1d_lbl_x")
        ylabel = c3.text_input("Y-axis Label", key="bar_1d_lbl_y")
        rotation = c4.number_input(
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

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="1d_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Legends**")
    if "1d_leg_num" not in st.session_state:
        st.session_state["1d_leg_num"] = 1

    legends_config = []
    for i in range(st.session_state["1d_leg_num"]):
        with st.expander(f"Legend {i+1}", expanded=False):
            c1, c2, c3, c4 = st.columns(4)
            l_source = c1.selectbox(
                "Source", options=["dataset", "custom"], key=f"1d_leg_src_{i}"
            )
            l_values = c2.selectbox(
                "Labels Values", options=params["fields"], key=f"1d_leg_val_{i}"
            )
            l_coloring_field = c3.selectbox(
                "Coloring Field", options=params["fields"], key=f"1d_leg_col_{i}"
            )
            l_casetype = c4.selectbox(
                "Case Type",
                options=["title", "upper", "original"],
                key=f"1d_leg_case_{i}",
            )

            c11, c12 = st.columns(2)
            l_title = c11.text_input("Legend Title", key=f"1d_leg_t_{i}")
            l_loc = c12.selectbox(
                "Legend Location",
                options=["upper left", "lower left", "upper right", "lower right"],
                key=f"1d_leg_l_{i}",
            )

            st.caption("**BBox Anchor (Advanced Positioning)**: (x, y, width, height)")
            j1, j2, j3, j4 = st.columns(4)
            bbox_x = j1.number_input("X", value=1.00, step=0.05, key=f"1d_bx_{i}")
            bbox_y = j2.number_input("Y", value=0.00, step=0.05, key=f"1d_by_{i}")
            bbox_w = j3.number_input("Width", value=0.30, step=0.05, key=f"1d_bw_{i}")
            bbox_h = j4.number_input("Height", value=1.00, step=0.05, key=f"1d_bh_{i}")

            legends_config.append(
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
            )

    l_btn1, l_btn2, _, _ = st.columns([1, 1, 2, 2])
    if l_btn1.button("➕ Add", key="1d_add_leg"):
        st.session_state["1d_leg_num"] += 1
        st.rerun()
    if (
        l_btn2.button("➖ Remove", key="1d_rem_leg")
        and st.session_state["1d_leg_num"] > 1
    ):
        st.session_state["1d_leg_num"] -= 1
        st.rerun()

    apply_legends_config = st.checkbox(
        "Apply Legends Config", value=False, key="1d_app_leg"
    )
    params["legends_config"] = legends_config if apply_legends_config else None

    params["save_name"] = None

    potential_fields = [
        params["x_axis"],
        params["z_axis"],
        params["coloring_field"],
        params["labels_extra"],
    ]
    if params["legends_config"]:
        potential_fields.append(params["legends_config"][0]["values"])
        potential_fields.append(params["legends_config"][0]["coloring_field"])

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def bar_2D_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="2d_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "2d_fv_num" not in st.session_state:
        st.session_state["2d_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["2d_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"2d_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"2d_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"2d_fv_v_{i}")
        if v:
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="2d_add"):
        st.session_state["2d_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="2d_rem") and st.session_state["2d_fv_num"] > 1:
        st.session_state["2d_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="2d_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="2d_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="2d_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="2d_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="2d_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis", params["fields"], key="2d_x")
    params["y_axis"] = c2.selectbox("Y-axis", ["count"], key="2d_y")
    params["z_axis"] = c3.selectbox("Z-axis (Grouping)", params["fields"], key="2d_z")
    st.divider()

    st.write("**Other Options**")
    c1, c2 = st.columns(2)
    params["orientation"] = c1.selectbox(
        "Orientation", ["vertical", "horizontal"], key="2d_orient"
    )
    params["coloring_field"] = c2.selectbox(
        "Coloring Field", params["fields"], key="2d_color"
    )
    st.divider()

    st.write("**Graph Options**")
    c1, c2, c3, _ = st.columns(4)
    params["bar_borders"] = c1.checkbox("Bar Borders", False, key="2d_b")
    params["bar_numbers"] = c2.checkbox("Bar Numbers", True, key="2d_n")
    params["grids"] = c3.checkbox("Grids", True, key="2d_g")
    st.divider()

    st.write("**Stack Order**")
    with st.expander("Order of Stacking (for Z-axis)", expanded=False):
        st.caption(
            "Enter values separated by comma (e.g., HMD, PC, Mobile, Immersive Display)"
        )
        stack_order_txt = st.text_area("Order", key="2d_stack")
        if stack_order_txt:
            stack_order = [x.strip() for x in stack_order_txt.split(",")]

    apply_stack_order = st.checkbox("Apply Stack Order", False, key="2d_stack_order")
    params["stack_order"] = stack_order if apply_stack_order else None
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        c1, c2, c3, c4 = st.columns(4)
        title = c1.text_input("Chart Title", key="2d_lbl_t")
        xlabel = c2.text_input("X-axis Label", key="2d_lbl_x")
        ylabel = c3.text_input("Y-axis Label", key="2d_lbl_y")
        rotation = c4.number_input(
            "Label Rotation",
            min_value=0,
            max_value=360,
            value=45,
            step=5,
            key="2d_lbl_r",
        )

        labels_spec = {
            "title": title,
            "x_label": xlabel,
            "y_label": ylabel,
            "rotation": rotation,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="2d_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Legends**")
    if "2d_leg_num" not in st.session_state:
        st.session_state["2d_leg_num"] = 1

    legends_config = []
    for i in range(st.session_state["2d_leg_num"]):
        with st.expander(f"Legend {i+1}", expanded=False):
            c1, c2, c3, c4 = st.columns(4)
            l_source = c1.selectbox(
                "Source", options=["dataset", "custom"], key=f"2d_leg_src_{i}"
            )
            l_values = c2.selectbox(
                "Labels Values", options=params["fields"], key=f"2d_leg_val_{i}"
            )
            l_coloring_field = c3.selectbox(
                "Coloring Field", options=params["fields"], key=f"2d_leg_col_{i}"
            )
            l_casetype = c4.selectbox(
                "Case Type",
                options=["title", "upper", "original"],
                key=f"2d_leg_case_{i}",
            )

            c11, c12 = st.columns(2)
            l_title = c11.text_input("Legend Title", key=f"2d_leg_t_{i}")
            l_loc = c12.selectbox(
                "Legend Location",
                options=["upper left", "lower left", "upper right", "lower right"],
                key=f"2d_leg_l_{i}",
            )

            st.caption("**BBox Anchor (Advanced Positioning)**: (x, y, width, height)")
            j1, j2, j3, j4 = st.columns(4)
            bbox_x = j1.number_input("X", value=1.00, step=0.05, key=f"2d_bx_{i}")
            bbox_y = j2.number_input("Y", value=0.00, step=0.05, key=f"2d_by_{i}")
            bbox_w = j3.number_input("Width", value=0.30, step=0.05, key=f"2d_bw_{i}")
            bbox_h = j4.number_input("Height", value=1.00, step=0.05, key=f"2d_bh_{i}")

            legends_config.append(
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
            )

    l_btn1, l_btn2, _, _ = st.columns([1, 1, 2, 2])
    if l_btn1.button("➕ Add", key="2d_add_leg"):
        st.session_state["2d_leg_num"] += 1
        st.rerun()
    if (
        l_btn2.button("➖ Remove", key="2d_rem_leg")
        and st.session_state["2d_leg_num"] > 1
    ):
        st.session_state["2d_leg_num"] -= 1
        st.rerun()

    apply_legends_config = st.checkbox(
        "Apply Legends Config", value=False, key="2d_app_leg"
    )
    params["legends_config"] = legends_config if apply_legends_config else None

    params["save_name"] = None

    potential_fields = [
        params["x_axis"],
        params["z_axis"],
        params["coloring_field"],
    ]
    if params["legends_config"]:
        potential_fields.append(params["legends_config"][0]["values"])
        potential_fields.append(params["legends_config"][0]["coloring_field"])

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def stacked_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="stk_fields"
    )
    st.divider()

    st.write("**Filter Pre**")
    st.caption("Fields to filter before counting (Optional)")
    params["filter_pre"] = st.multiselect(
        "Filter Pre Fields", options=params["fields"], key="stk_filter_pre"
    )
    st.divider()

    st.write("**Filter Values**")
    if "stk_fv_num" not in st.session_state:
        st.session_state["stk_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["stk_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"stk_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"stk_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"stk_fv_v_{i}")
        if v:
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="stk_add"):
        st.session_state["stk_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="stk_rem") and st.session_state["stk_fv_num"] > 1:
        st.session_state["stk_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="stk_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="stk_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="stk_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="stk_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="stk_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis", params["fields"], key="stk_x")
    params["y_axis"] = c2.selectbox("Y-axis", ["count"], key="stk_y")
    params["z_axis"] = c3.selectbox("Z-axis (Grouping)", params["fields"], key="stk_z")
    st.divider()

    st.write("**Other Options**")
    c1, c2 = st.columns(2)
    params["orientation"] = c1.selectbox(
        "Orientation", ["vertical", "horizontal", "area"], key="stk_orient"
    )
    params["coloring_field"] = c2.selectbox(
        "Coloring Field", params["fields"], key="stk_color"
    )
    st.divider()

    st.write("**Graph Options**")
    c1, c2, c3, _ = st.columns(4)
    params["stack_borders"] = c1.checkbox("Stack Borders", False, key="stk_b")
    params["bar_numbers"] = c2.checkbox("Bar Numbers", True, key="stk_n")
    params["grids"] = c3.checkbox("Grids", True, key="stk_g")
    st.divider()

    st.write("**Stack Order**")
    with st.expander("Order of Stacking (for Z-axis)", expanded=False):
        st.caption("Enter values separated by comma (e.g., XR, MR, AR, VR)")
        stack_order_txt = st.text_area("Order", key="stk_stack")
        if stack_order_txt:
            stack_order = [x.strip() for x in stack_order_txt.split(",")]

    apply_stack_order = st.checkbox("Apply Stack Order", False, key="stk_stack_order")
    params["stack_order"] = stack_order if apply_stack_order else None
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        c1, c2, c3, c4 = st.columns(4)
        title = c1.text_input("Chart Title", key="stk_lbl_t")
        xlabel = c2.text_input("X-axis Label", key="stk_lbl_x")
        ylabel = c3.text_input("Y-axis Label", key="stk_lbl_y")
        rotation = c4.number_input(
            "Label Rotation",
            min_value=0,
            max_value=360,
            value=45,
            step=5,
            key="stk_lbl_r",
        )

        labels_spec = {
            "title": title,
            "x_label": xlabel,
            "y_label": ylabel,
            "rotation": rotation,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="stk_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Legends**")
    if "stk_leg_num" not in st.session_state:
        st.session_state["stk_leg_num"] = 1

    legends_config = []
    for i in range(st.session_state["stk_leg_num"]):
        with st.expander(f"Legend {i+1}", expanded=False):
            c1, c2, c3, c4 = st.columns(4)
            l_source = c1.selectbox(
                "Source", options=["dataset", "custom"], key=f"stk_leg_src_{i}"
            )
            l_values = c2.selectbox(
                "Labels Values", options=params["fields"], key=f"stk_leg_val_{i}"
            )
            l_coloring_field = c3.selectbox(
                "Coloring Field", options=params["fields"], key=f"stk_leg_col_{i}"
            )
            l_casetype = c4.selectbox(
                "Case Type",
                options=["title", "upper", "original"],
                key=f"stk_leg_case_{i}",
            )

            c11, c12 = st.columns(2)
            l_title = c11.text_input("Legend Title", key=f"stk_leg_t_{i}")
            l_loc = c12.selectbox(
                "Legend Location",
                options=["upper left", "lower left", "upper right", "lower right"],
                key=f"stk_leg_l_{i}",
            )

            st.caption("**BBox Anchor (Advanced Positioning)**: (x, y, width, height)")
            j1, j2, j3, j4 = st.columns(4)
            bbox_x = j1.number_input("X", value=1.00, step=0.05, key=f"stk_bx_{i}")
            bbox_y = j2.number_input("Y", value=0.00, step=0.05, key=f"stk_by_{i}")
            bbox_w = j3.number_input("Width", value=0.30, step=0.05, key=f"stk_bw_{i}")
            bbox_h = j4.number_input("Height", value=1.00, step=0.05, key=f"stk_bh_{i}")

            legends_config.append(
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
            )

    l_btn1, l_btn2, _, _ = st.columns([1, 1, 2, 2])
    if l_btn1.button("➕ Add", key="stk_add_leg"):
        st.session_state["stk_leg_num"] += 1
        st.rerun()
    if (
        l_btn2.button("➖ Remove", key="stk_rem_leg")
        and st.session_state["stk_leg_num"] > 1
    ):
        st.session_state["stk_leg_num"] -= 1
        st.rerun()

    apply_legends_config = st.checkbox(
        "Apply Legends Config", value=False, key="stk_app_leg"
    )
    params["legends_config"] = legends_config if apply_legends_config else None

    params["save_name"] = None

    potential_fields = [
        params["x_axis"],
        params["z_axis"],
        params["coloring_field"],
    ]
    if params["filter_pre"]:
        potential_fields.extend(params["filter_pre"])

    if params["legends_config"]:
        for leg in params["legends_config"]:
            potential_fields.append(leg["values"])
            potential_fields.append(leg["coloring_field"])

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params
