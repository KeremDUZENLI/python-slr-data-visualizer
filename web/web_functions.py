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
                options=["upper right", "lower right"],
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
        else:
            stack_order = None

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
                options=["upper right", "lower right"],
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
        else:
            stack_order = None

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
                options=["upper right", "lower right"],
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


def pie_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="pie_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "pie_fv_num" not in st.session_state:
        st.session_state["pie_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["pie_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"pie_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"pie_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"pie_fv_v_{i}")
        if v.strip():
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="pie_add"):
        st.session_state["pie_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="pie_rem") and st.session_state["pie_fv_num"] > 1:
        st.session_state["pie_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="pie_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="pie_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="pie_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="pie_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="pie_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2 = st.columns(2)
    params["x_axis"] = c1.selectbox("X-axis (Slices)", params["fields"], key="pie_x")
    params["y_axis"] = c2.selectbox("Y-axis (Values)", ["count"], key="pie_y")
    st.divider()

    st.write("**Other Options**")
    c1, c2 = st.columns(2)
    params["coloring_field"] = c1.selectbox(
        "Coloring Field", params["fields"], key="pie_color"
    )
    params["labels_color"] = c2.text_input(
        "Labels Color (e.g., white, black)", value="white", key="pie_lbl_col"
    )
    st.divider()

    st.write("**Graph Options**")
    params["pie_borders"] = st.checkbox("Pie Borders", True, key="pie_b")
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        title = st.text_input("Chart Title", key="pie_lbl_t")
        labels_spec = {
            "title": title,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="pie_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}

    params["save_name"] = None

    potential_fields = [
        params["x_axis"],
        params["coloring_field"],
    ]

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def pie_nested_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="pien_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "pien_fv_num" not in st.session_state:
        st.session_state["pien_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["pien_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"pien_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"pien_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"pien_fv_v_{i}")
        if v.strip():
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="pien_add"):
        st.session_state["pien_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="pien_rem") and st.session_state["pien_fv_num"] > 1:
        st.session_state["pien_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="pien_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="pien_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="pien_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="pien_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="pien_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis (Inner)", params["fields"], key="pien_x")
    params["y_axis"] = c2.selectbox("Y-axis (Values)", ["count"], key="pien_y")
    params["z_axis"] = c3.selectbox("Z-axis (Outer)", params["fields"], key="pien_z")
    st.divider()

    st.write("**Coloring Options**")
    c1, c2 = st.columns(2)
    params["coloring_field_inner"] = c1.selectbox(
        "Coloring Field (Inner)", params["fields"], key="pien_col_in"
    )
    params["coloring_field_outer"] = c2.selectbox(
        "Coloring Field (Outer)", params["fields"], key="pien_col_out"
    )

    c3, c4 = st.columns(2)
    params["labels_color_inner"] = c3.text_input(
        "Labels Color (Inner)", value="white", key="pien_lbl_col_in"
    )
    params["labels_color_outer"] = c4.text_input(
        "Labels Color (Outer)", value="black", key="pien_lbl_col_out"
    )
    st.divider()

    st.write("**Graph Options**")
    c1, c2 = st.columns(2)
    params["pie_borders"] = c1.checkbox("Pie Borders", False, key="pien_b")
    params["labels_hide_percent"] = c2.number_input(
        "Hide Labels < (%)", min_value=0, value=2, step=1, key="pien_hide_pct"
    )
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        title = st.text_input("Chart Title", key="pien_lbl_t")
        labels_spec = {
            "title": title,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="pien_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}

    params["save_name"] = None

    potential_fields = [
        params["x_axis"],
        params["z_axis"],
        params["coloring_field_inner"],
        params["coloring_field_outer"],
    ]

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def heatmap_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="hm_fields"
    )
    st.divider()

    st.write("**Filter Pre**")
    st.caption("Fields to filter before counting (Optional)")
    use_sep = st.checkbox(
        "Use Separated Pre-Filters (e.g., for X and Z independently)",
        value=False,
        key="hm_use_sep",
    )

    if use_sep:
        params["filter_pre"] = None
        c1, c2 = st.columns(2)
        pre1 = c1.multiselect("Filter Pre 1", options=params["fields"], key="hm_pre_1")
        pre2 = c2.multiselect("Filter Pre 2", options=params["fields"], key="hm_pre_2")
        params["filter_pre_sep"] = [pre1, pre2] if pre1 and pre2 else None
    else:
        params["filter_pre_sep"] = None
        params["filter_pre"] = st.multiselect(
            "Filter Pre Fields", options=params["fields"], key="hm_filter_pre"
        )
    st.divider()

    st.write("**Filter Values**")
    if "hm_fv_num" not in st.session_state:
        st.session_state["hm_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["hm_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"hm_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"hm_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"hm_fv_v_{i}")
        if v.strip():
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="hm_add"):
        st.session_state["hm_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="hm_rem") and st.session_state["hm_fv_num"] > 1:
        st.session_state["hm_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="hm_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    if use_sep:
        c1, c2 = st.columns(2)
        f1 = c1.selectbox("Field 1", ["count"], key="hm_fc_f1")
        o1 = c1.selectbox(
            "Operation 1", ["==", "!=", ">=", ">", "<=", "<", "="], key="hm_fc_o1"
        )
        v1 = c1.number_input("Value 1", min_value=0, value=0, step=1, key="hm_fc_v1")

        f2 = c2.selectbox("Field 2", ["count"], key="hm_fc_f2")
        o2 = c2.selectbox(
            "Operation 2", ["==", "!=", ">=", ">", "<=", "<", "="], key="hm_fc_o2"
        )
        v2 = c2.number_input("Value 2", min_value=0, value=0, step=1, key="hm_fc_v2")

        apply_filter_count = st.checkbox("Apply Filter Count", key="hm_app_fc")
        params["filter_count"] = None
        params["filter_count_sep"] = (
            [f"{f1} {o1} {v1}", f"{f2} {o2} {v2}"] if apply_filter_count else None
        )
    else:
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox("Field", ["count"], key="hm_fc_f")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="hm_fc_o"
        )
        v = c3.number_input("Value", min_value=0, value=0, step=1, key="hm_fc_v")

        apply_filter_count = st.checkbox("Apply Filter Count", key="hm_app_fc")
        params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
        params["filter_count_sep"] = None
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis (Rows)", params["fields"], key="hm_x")
    params["y_axis"] = c2.selectbox("Y-axis", ["count"], key="hm_y")
    params["z_axis"] = c3.selectbox("Z-axis (Columns)", params["fields"], key="hm_z")
    st.divider()

    st.write("**Other Options**")
    c1, c2, c3 = st.columns(3)
    params["cmap"] = c1.text_input("Colormap (e.g., BuGn)", value="BuGn", key="hm_cmap")
    params["coloring_field"] = c2.selectbox(
        "Coloring Field (Optional)", [None] + params["fields"], key="hm_color"
    )
    params["labels_color"] = c3.text_input(
        "Labels Color", value="auto", key="hm_lbl_col"
    )
    st.divider()

    st.write("**Graph Options & Extras**")
    c1, c2, c3 = st.columns(3)
    params["border"] = c1.checkbox("Matrix Borders", False, key="hm_b")
    params["matrix_numbers"] = c2.checkbox("Matrix Numbers", True, key="hm_n")
    params["labels_extra"] = c3.selectbox(
        "Labels Extra", [None] + params["fields"], key="hm_le"
    )
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        c1, c2, c3, c4 = st.columns(4)
        title = c1.text_input("Chart Title", key="hm_lbl_t")
        xlabel = c2.text_input("X-axis Label", key="hm_lbl_x")
        ylabel = c3.text_input("Y-axis Label", key="hm_lbl_y")
        rotation = c4.number_input(
            "Label Rotation",
            min_value=0,
            max_value=360,
            value=45,
            step=5,
            key="hm_lbl_r",
        )

        labels_spec = {
            "title": title,
            "x_label": xlabel,
            "y_label": ylabel,
            "rotation": rotation,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="hm_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}

    params["save_name"] = None

    potential_fields = [
        params["x_axis"],
        params["z_axis"],
        params["coloring_field"],
        params["labels_extra"],
    ]
    if params["filter_pre"]:
        potential_fields.extend(params["filter_pre"])
    if params["filter_pre_sep"]:
        potential_fields.extend(params["filter_pre_sep"][0])
        potential_fields.extend(params["filter_pre_sep"][1])

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def scatter_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="sct_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "sct_fv_num" not in st.session_state:
        st.session_state["sct_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["sct_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"sct_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"sct_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"sct_fv_v_{i}")
        if v.strip():
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="sct_add"):
        st.session_state["sct_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="sct_rem") and st.session_state["sct_fv_num"] > 1:
        st.session_state["sct_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="sct_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="sct_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="sct_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="sct_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="sct_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis", params["fields"], key="sct_x")
    params["y_axis"] = c2.selectbox("Y-axis", ["count"], key="sct_y")
    params["z_axis"] = c3.selectbox("Z-axis", params["fields"], key="sct_z")
    st.divider()

    st.write("**Other Options**")
    c1, c2 = st.columns(2)
    params["coloring_field"] = c1.selectbox(
        "Coloring Field", params["fields"], key="sct_color"
    )
    st.divider()

    st.write("**Graph Options**")
    c1, c2 = st.columns(2)
    params["grids"] = c1.checkbox("Grids", True, key="sct_g")
    params["color_mapping"] = c2.checkbox("Color Mapping", False, key="sct_cm")
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        c1, c2, c3, c4 = st.columns(4)
        title = c1.text_input("Chart Title", key="sct_lbl_t")
        xlabel = c2.text_input("X-axis Label", key="sct_lbl_x")
        ylabel = c3.text_input("Y-axis Label", key="sct_lbl_y")
        rotation = c4.number_input(
            "Label Rotation",
            min_value=0,
            max_value=360,
            value=45,
            step=5,
            key="sct_lbl_r",
        )

        labels_spec = {
            "title": title,
            "x_label": xlabel,
            "y_label": ylabel,
            "rotation": rotation,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="sct_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Legends**")
    if "sct_leg_num" not in st.session_state:
        st.session_state["sct_leg_num"] = 1

    legends_config = []
    for i in range(st.session_state["sct_leg_num"]):
        with st.expander(f"Legend {i+1}", expanded=False):
            c1, c2, c3, c4 = st.columns(4)
            l_source = c1.selectbox(
                "Source",
                options=["dataset", "custom", "bubble"],
                key=f"sct_leg_src_{i}",
            )
            l_values = c2.selectbox(
                "Labels Values", options=params["fields"], key=f"sct_leg_val_{i}"
            )
            l_coloring_field = c3.selectbox(
                "Coloring Field", options=params["fields"], key=f"sct_leg_col_{i}"
            )
            l_casetype = c4.selectbox(
                "Case Type",
                options=["title", "upper", "original"],
                key=f"sct_leg_case_{i}",
            )

            c11, c12 = st.columns(2)
            l_title = c11.text_input("Legend Title", key=f"sct_leg_t_{i}")
            l_loc = c12.selectbox(
                "Legend Location",
                options=["upper left", "upper right", "lower left", "lower right"],
                key=f"sct_leg_l_{i}",
            )

            st.caption("**BBox Anchor (Advanced Positioning)**: (x, y, width, height)")
            j1, j2, j3, j4 = st.columns(4)
            bbox_x = j1.number_input("X", value=1.00, step=0.05, key=f"sct_bx_{i}")
            bbox_y = j2.number_input("Y", value=0.00, step=0.05, key=f"sct_by_{i}")
            bbox_w = j3.number_input("Width", value=0.30, step=0.05, key=f"sct_bw_{i}")
            bbox_h = j4.number_input("Height", value=1.00, step=0.05, key=f"sct_bh_{i}")

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
    if l_btn1.button("➕ Add", key="sct_add_leg"):
        st.session_state["sct_leg_num"] += 1
        st.rerun()
    if (
        l_btn2.button("➖ Remove", key="sct_rem_leg")
        and st.session_state["sct_leg_num"] > 1
    ):
        st.session_state["sct_leg_num"] -= 1
        st.rerun()

    apply_legends_config = st.checkbox(
        "Apply Legends Config", value=False, key="sct_app_leg"
    )
    params["legends_config"] = legends_config if apply_legends_config else None

    params["save_name"] = None

    potential_fields = [
        params["x_axis"],
        params["z_axis"],
        params["coloring_field"],
    ]
    if params["legends_config"]:
        for leg in params["legends_config"]:
            if leg["source"] != "bubble":
                potential_fields.append(leg["values"])
                potential_fields.append(leg["coloring_field"])

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def sunburst_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="sb_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "sb_fv_num" not in st.session_state:
        st.session_state["sb_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["sb_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"sb_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"sb_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"sb_fv_v_{i}")
        if v.strip():
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="sb_add"):
        st.session_state["sb_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="sb_rem") and st.session_state["sb_fv_num"] > 1:
        st.session_state["sb_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="sb_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="sb_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="sb_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="sb_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="sb_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("X-axis (Inner)", params["fields"], key="sb_x")
    params["y_axis"] = c2.selectbox("Y-axis (Values)", ["count"], key="sb_y")
    params["z_axis"] = c3.selectbox("Z-axis (Outer)", params["fields"], key="sb_z")
    st.divider()

    st.write("**Coloring Options**")
    c1, c2 = st.columns(2)
    params["coloring_field_inner"] = c1.selectbox(
        "Coloring Field (Inner)", params["fields"], key="sb_col_in"
    )
    params["coloring_field_outer"] = c2.selectbox(
        "Coloring Field (Outer)", params["fields"], key="sb_col_out"
    )

    c3, c4 = st.columns(2)
    params["labels_color_inner"] = c3.text_input(
        "Labels Color (Inner)", value="white", key="sb_lbl_col_in"
    )
    params["labels_color_outer"] = c4.text_input(
        "Labels Color (Outer)", value="black", key="sb_lbl_col_out"
    )
    st.divider()

    st.write("**Graph Options**")
    c1, c2 = st.columns(2)
    params["pie_borders"] = c1.checkbox("Pie Borders", False, key="sb_b")
    params["labels_hide_percent"] = c2.number_input(
        "Hide Labels < (%)", min_value=0, value=2, step=1, key="sb_hide_pct"
    )
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        title = st.text_input("Chart Title", key="sb_lbl_t")
        labels_spec = {
            "title": title,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="sb_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Size**")
    c1, c2 = st.columns(2)
    w = c1.number_input("Width", min_value=100, value=1000, step=50, key="sb_w")
    h = c2.number_input("Height", min_value=100, value=1000, step=50, key="sb_h")
    params["size"] = (w, h)

    params["show_plot"] = False

    potential_fields = [
        params["x_axis"],
        params["z_axis"],
        params["coloring_field_inner"],
        params["coloring_field_outer"],
    ]

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def sankey_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="snk_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "snk_fv_num" not in st.session_state:
        st.session_state["snk_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["snk_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"snk_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"snk_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"snk_fv_v_{i}")
        if v.strip():
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="snk_add"):
        st.session_state["snk_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="snk_rem") and st.session_state["snk_fv_num"] > 1:
        st.session_state["snk_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="snk_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="snk_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="snk_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="snk_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="snk_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes (Flow Levels)**")
    c1, c2, c3 = st.columns(3)
    params["x_axis"] = c1.selectbox("Level 1 (Source)", params["fields"], key="snk_x")
    params["y_axis"] = c2.selectbox("Level 2 (Middle)", params["fields"], key="snk_y")
    params["z_axis"] = c3.selectbox("Level 3 (Target)", params["fields"], key="snk_z")
    st.divider()

    st.write("**Node & Link Options**")
    c1, c2, c3, c4 = st.columns(4)
    params["nodes_pad"] = c1.number_input(
        "Nodes Pad", min_value=0, value=15, step=1, key="snk_np"
    )
    params["nodes_thickness"] = c2.number_input(
        "Nodes Thickness", min_value=1, value=20, step=1, key="snk_nt"
    )
    links_color = c3.selectbox(
        "Links Color Mode", options=["source", "target", "custom"], key="snk_lc_mode"
    )
    if links_color == "custom":
        params["links_color"] = c3.text_input(
            "Enter Color", value="lightgray", key="snk_lc_custom"
        )
    else:
        params["links_color"] = links_color

    params["links_opacity"] = c4.number_input(
        "Links Opacity", min_value=0.0, max_value=1.0, value=0.1, step=0.1, key="snk_lo"
    )
    st.divider()

    st.write("**Labels**")
    params["labels_color"] = st.text_input(
        "Labels Color", value="black", key="snk_lbl_c"
    )

    with st.expander("Chart Labels (Headers)", expanded=False):
        c1, c2, c3 = st.columns(3)
        t1 = c1.text_input("Title 1 (Level 1)", key="snk_t1")
        t2 = c2.text_input("Title 2 (Level 2)", key="snk_t2")
        t3 = c3.text_input("Title 3 (Level 3)", key="snk_t3")
        labels_spec = {
            "title1": t1,
            "title2": t2,
            "title3": t3,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="snk_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Size**")
    c1, c2 = st.columns(2)
    w = c1.number_input("Width", min_value=100, value=1000, step=50, key="snk_w")
    h = c2.number_input("Height", min_value=100, value=750, step=50, key="snk_h")
    params["size"] = (w, h)

    params["show_plot"] = False

    potential_fields = [
        params["x_axis"],
        params["y_axis"],
        params["z_axis"],
    ]

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def worldmap_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="wm_fields"
    )
    st.divider()

    st.write("**Filter Values**")
    if "wm_fv_num" not in st.session_state:
        st.session_state["wm_fv_num"] = 1

    filter_values = []
    for i in range(st.session_state["wm_fv_num"]):
        c1, c2, c3 = st.columns(3)
        f = c1.selectbox(f"Field {i+1}", params["fields"], key=f"wm_f_{i}")
        o = c2.selectbox(
            "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"wm_o_{i}"
        )
        v = c3.text_input("Value", value=" ", key=f"wm_fv_v_{i}")
        if v.strip():
            filter_values.append(f"{f} {o} {v}")

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="wm_add"):
        st.session_state["wm_fv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="wm_rem") and st.session_state["wm_fv_num"] > 1:
        st.session_state["wm_fv_num"] -= 1
        st.rerun()

    apply_filter_values = st.checkbox("Apply Filter Values", key="wm_af")
    params["filter_values"] = filter_values if apply_filter_values else None
    st.divider()

    st.write("**Filter Count**")
    c1, c2, c3 = st.columns(3)
    f = c1.selectbox("Field", ["count"], key="wm_fc_f")
    o = c2.selectbox(
        "Operation", ["==", "!=", ">=", ">", "<=", "<", "="], key="wm_fc_o"
    )
    v = c3.number_input("Value", min_value=0, value=0, step=1, key="wm_fc_v")

    apply_filter_count = st.checkbox("Apply Filter Count", key="wm_app_fc")
    params["filter_count"] = f"{f} {o} {v}" if apply_filter_count else None
    st.divider()

    st.write("**Axes**")
    c1, c2 = st.columns(2)
    params["x_axis"] = c1.selectbox("X-axis (Countries)", params["fields"], key="wm_x")
    params["y_axis"] = c2.selectbox("Y-axis (Values)", ["count"], key="wm_y")
    st.divider()

    st.write("**Coloring & Options**")
    c1, c2 = st.columns(2)
    params["cmap"] = c1.text_input(
        "Colormap (e.g., YlOrRd)", value="YlOrRd", key="wm_cmap"
    )
    params["labels_color"] = c2.text_input(
        "Labels Color", value="black", key="wm_lbl_col"
    )

    c3, c4 = st.columns(2)
    params["borders"] = c3.checkbox("Show Borders", True, key="wm_b")
    params["frame"] = c4.checkbox("Show Frame", True, key="wm_f")
    st.divider()

    st.write("**Labels**")
    with st.expander("Chart Labels", expanded=False):
        title = st.text_input("Chart Title", key="wm_lbl_t")
        labels_spec = {
            "title": title,
        }

    apply_labels_spec = st.checkbox("Apply Labels Spec", False, key="wm_app_lbl")
    params["labels_spec"] = labels_spec if apply_labels_spec else {}
    st.divider()

    st.write("**Size**")
    c1, c2 = st.columns(2)
    w = c1.number_input("Width", min_value=100, value=1000, step=50, key="wm_w")
    h = c2.number_input("Height", min_value=100, value=500, step=50, key="wm_h")
    params["size"] = (w, h)

    params["show_plot"] = False

    potential_fields = [
        params["x_axis"],
    ]

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params


def prisma_web(dataset, fields_available):
    params = {}
    params["dataset"] = dataset

    st.write("**Fields**")
    params["fields"] = st.multiselect(
        "Select Fields", options=fields_available, key="prm_fields"
    )
    st.divider()

    # ---------------- MANUAL VALUES ----------------
    st.write("**Manual Values**")
    if "prm_mv_num" not in st.session_state:
        st.session_state["prm_mv_num"] = 1

    manual_values = {}
    for i in range(st.session_state["prm_mv_num"]):
        c1, c2 = st.columns(2)
        k = c1.text_input(f"Key {i+1}", key=f"prm_mvk_{i}")
        v = c2.number_input(
            f"Value {i+1}", min_value=0, value=0, step=1, key=f"prm_mvv_{i}"
        )
        if k.strip():
            manual_values[k.strip()] = v

    c11, c12, _, _ = st.columns([1, 1, 2, 2])
    if c11.button("➕ Add", key="prm_mv_add"):
        st.session_state["prm_mv_num"] += 1
        st.rerun()
    if c12.button("➖ Remove", key="prm_mv_rem") and st.session_state["prm_mv_num"] > 1:
        st.session_state["prm_mv_num"] -= 1
        st.rerun()

    apply_mv = st.checkbox("Apply Manual Values", key="prm_app_mv")
    params["manual_values"] = manual_values if apply_mv else {}
    st.divider()

    # ---------------- FILTER SEQUENCE ----------------
    st.write("**Calculated Values (Filter Sequence)**")
    if "prm_fs_num" not in st.session_state:
        st.session_state["prm_fs_num"] = 1

    filter_seq = []
    for i in range(st.session_state["prm_fs_num"]):
        c1, c2, c3, c4 = st.columns(4)
        k = c1.text_input(f"Key {i+1}", key=f"prm_fsk_{i}")
        f = c2.selectbox(f"Field {i+1}", params["fields"], key=f"prm_fsf_{i}")
        o = c3.selectbox(
            "Op", ["==", "!=", ">=", ">", "<=", "<", "="], key=f"prm_fso_{i}"
        )
        v = c4.text_input(f"Value {i+1}", value=" ", key=f"prm_fsv_{i}")
        if k.strip() and v.strip():
            filter_seq.append({"key": k.strip(), "filter": f"{f} {o} {v}"})

    c21, c22, _, _ = st.columns([1, 1, 2, 2])
    if c21.button("➕ Add", key="prm_fs_add"):
        st.session_state["prm_fs_num"] += 1
        st.rerun()
    if c22.button("➖ Remove", key="prm_fs_rem") and st.session_state["prm_fs_num"] > 1:
        st.session_state["prm_fs_num"] -= 1
        st.rerun()

    apply_fs = st.checkbox("Apply Filter Sequence", key="prm_app_fs")
    params["filter_seq"] = filter_seq if apply_fs else None
    st.divider()

    # ---------------- LABELS SPEC ----------------
    st.write("**Labels Spec**")
    st.caption("Use `{key}` to insert dynamic values (e.g., `(n = {search})`)")
    if "prm_lbl_num" not in st.session_state:
        st.session_state["prm_lbl_num"] = 1

    labels_spec = {}
    for i in range(st.session_state["prm_lbl_num"]):
        c1, c2 = st.columns([1, 3])
        k = c1.text_input(f"Node Key {i+1}", key=f"prm_lblk_{i}")
        v = c2.text_area(f"Label Text {i+1}", key=f"prm_lblv_{i}", height=68)
        if k.strip() and v.strip():
            labels_spec[k.strip()] = v.strip()

    c31, c32, _, _ = st.columns([1, 1, 2, 2])
    if c31.button("➕ Add", key="prm_lbl_add"):
        st.session_state["prm_lbl_num"] += 1
        st.rerun()
    if (
        c32.button("➖ Remove", key="prm_lbl_rem")
        and st.session_state["prm_lbl_num"] > 1
    ):
        st.session_state["prm_lbl_num"] -= 1
        st.rerun()

    apply_lbl = st.checkbox("Apply Labels Spec", key="prm_app_lbl")
    params["labels_spec"] = labels_spec if apply_lbl else {}
    st.divider()

    # ---------------- FLOW CONFIG ----------------
    st.write("**Flow Config (Main Edges)**")
    if "prm_flw_num" not in st.session_state:
        st.session_state["prm_flw_num"] = 1

    flow_config = []
    for i in range(st.session_state["prm_flw_num"]):
        c1, c2 = st.columns(2)
        src = c1.text_input(f"Source Node {i+1}", key=f"prm_flws_{i}")
        tgt = c2.text_input(f"Target Node {i+1}", key=f"prm_flwt_{i}")
        if src.strip() and tgt.strip():
            flow_config.append((src.strip(), tgt.strip()))

    c41, c42, _, _ = st.columns([1, 1, 2, 2])
    if c41.button("➕ Add", key="prm_flw_add"):
        st.session_state["prm_flw_num"] += 1
        st.rerun()
    if (
        c42.button("➖ Remove", key="prm_flw_rem")
        and st.session_state["prm_flw_num"] > 1
    ):
        st.session_state["prm_flw_num"] -= 1
        st.rerun()

    apply_flw = st.checkbox("Apply Flow Config", key="prm_app_flw")
    params["flow_config"] = flow_config if apply_flw else []
    st.divider()

    # ---------------- NOTES CONFIG ----------------
    st.write("**Notes Config (Optional Edges)**")
    if "prm_not_num" not in st.session_state:
        st.session_state["prm_not_num"] = 1

    notes_config = []
    for i in range(st.session_state["prm_not_num"]):
        c1, c2 = st.columns(2)
        src = c1.text_input(f"Source Node {i+1}", key=f"prm_nots_{i}")
        tgt = c2.text_input(f"Note Node {i+1}", key=f"prm_nott_{i}")
        if src.strip() and tgt.strip():
            notes_config.append((src.strip(), tgt.strip()))

    c51, c52, _, _ = st.columns([1, 1, 2, 2])
    if c51.button("➕ Add", key="prm_not_add"):
        st.session_state["prm_not_num"] += 1
        st.rerun()
    if (
        c52.button("➖ Remove", key="prm_not_rem")
        and st.session_state["prm_not_num"] > 1
    ):
        st.session_state["prm_not_num"] -= 1
        st.rerun()

    apply_not = st.checkbox("Apply Notes Config", key="prm_app_not")
    params["notes_config"] = notes_config if apply_not else None
    st.divider()

    # ---------------- STYLE GROUPS ----------------
    st.write("**Style Groups**")
    st.caption(
        "Enter node keys separated by commas (e.g., `search, screening, eligible`)"
    )
    sg_main = st.text_area("Main Nodes (box_main)", key="prm_sg_m")
    sg_exc = st.text_area("Excluded Nodes (box_excluded)", key="prm_sg_e")
    sg_not = st.text_area("Note Nodes (note)", key="prm_sg_n")

    style_groups = {}
    if sg_main.strip():
        style_groups["box_main"] = [x.strip() for x in sg_main.split(",") if x.strip()]
    if sg_exc.strip():
        style_groups["box_excluded"] = [
            x.strip() for x in sg_exc.split(",") if x.strip()
        ]
    if sg_not.strip():
        style_groups["note"] = [x.strip() for x in sg_not.split(",") if x.strip()]

    apply_sg = st.checkbox("Apply Style Groups", key="prm_app_sg")
    params["style_groups"] = style_groups if apply_sg else None

    params["save_name"] = None

    potential_fields = []
    if params.get("filter_seq"):
        for step in params["filter_seq"]:
            fld = step["filter"].split()[0]
            if fld in fields_available:
                potential_fields.append(fld)

    active_fields = [f for f in potential_fields if f is not None]
    params["fields"] = list(set(params["fields"] + active_fields))

    return params
