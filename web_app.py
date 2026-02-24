import streamlit as st

import setup.setup_functions as setup_module
from setup.setup_functions import (
    bar_1D,
    bar_2D,
    stacked,
    pie,
    pie_nested,
    heatmap,
    scatter,
    sunburst,
    sankey,
    worldmap,
    prisma,
)

from web.tools import (
    initialize_state,
    inject_config_to_module,
    save_config,
    load_config,
    save_chart,
)
from web.web_datasets import (
    data_preparation_web,
)
from web.web_functions import (
    bar_1D_web,
    bar_2D_web,
    stacked_web,
    pie_web,
    pie_nested_web,
    heatmap_web,
    scatter_web,
    sunburst_web,
    sankey_web,
    worldmap_web,
    prisma_web,
)
from web.web_settings import (
    settings_web,
)

# ==============================================================================
# 0. PAGE CONFIG & STATE INIT
# ==============================================================================
st.set_page_config(layout="wide", page_title="Data Visualizer")
st.sidebar.title("Navigator")
step = st.sidebar.radio(
    "Go to Step:", ["1. Data Preparation", "2. Chart Creation", "3. Settings"]
)
st.sidebar.divider()
initialize_state()

# ==============================================================================
# 1. DATA PREPARATION
# ==============================================================================
if step == "1. Data Preparation":
    data_preparation_web()

# ==============================================================================
# 2. CHART CREATION
# ==============================================================================
if step == "2. Chart Creation":
    st.title("📊 Step 2: Chart Creation")

    if not st.session_state["data_versions"]:
        st.warning("⚠️ No data available. Please go to Data Preparation")
    else:
        dataset = st.sidebar.selectbox(
            "Select Dataset",
            options=list(st.session_state["data_versions"].keys()),
        )
        chart_type = st.sidebar.selectbox(
            "Select Chart",
            options=[
                "bar_1D",
                "bar_2D",
                "stacked",
                "pie",
                "pie_nested",
                "heatmap",
                "scatter",
                "sunburst",
                "sankey",
                "worldmap",
                "prisma",
            ],
        )

        CHARTS = {
            "bar_1D": {"setup": bar_1D, "web": bar_1D_web},
            "bar_2D": {"setup": bar_2D, "web": bar_2D_web},
            "stacked": {"setup": stacked, "web": stacked_web},
            "pie": {"setup": pie, "web": pie_web},
            "pie_nested": {"setup": pie_nested, "web": pie_nested_web},
            "heatmap": {"setup": heatmap, "web": heatmap_web},
            "scatter": {"setup": scatter, "web": scatter_web},
            "sunburst": {"setup": sunburst, "web": sunburst_web},
            "sankey": {"setup": sankey, "web": sankey_web},
            "worldmap": {"setup": worldmap, "web": worldmap_web},
            "prisma": {"setup": prisma, "web": prisma_web},
        }

        dataset_selected = st.session_state["data_versions"][dataset]
        fields_available = list(dataset_selected.keys())

        setup_function = CHARTS[chart_type]["setup"]
        web_function = CHARTS[chart_type]["web"]

        # Chart Header
        st.subheader(f"Dataset: {dataset}")
        st.divider()

        # Chart Parameters
        params_chart = web_function(dataset_selected, fields_available)
        st.divider()

        # Chart Draw
        st.write("**Draw Chart**")
        if st.button("🖌️ Draw Chart"):
            inject_config_to_module(setup_module)

            try:
                fig, legends, extra_artists = setup_function(**params_chart)
                st.session_state["generated_fig"] = fig
                st.session_state["generated_legends"] = legends
                st.session_state["generated_extra_artists"] = extra_artists
            except Exception as e:
                st.error(f"❌ Error: {e}")

        if "generated_fig" in st.session_state:
            fig = st.session_state["generated_fig"]

            if type(fig).__name__ == "Digraph":
                st.graphviz_chart(fig)
            elif type(fig).__module__.startswith("plotly"):
                st.plotly_chart(fig, width="stretch")
            else:
                saved_legends = st.session_state.get("generated_legends", []) or []
                saved_extras = st.session_state.get("generated_extra_artists", []) or []
                all_artists = saved_legends + saved_extras
                st.pyplot(
                    st.session_state["generated_fig"],
                    bbox_inches="tight",
                    bbox_extra_artists=all_artists,
                )
        st.divider()

        # Configs
        st.write("**Configs**")
        c1, c2, c3, c4 = st.columns([3, 2, 3, 2])

        with c1:
            config_name = st.text_input("Config Name", value=f"{chart_type}_config")

        with c2:
            st.write("")
            st.write("")
            st.button(
                "💾 Save Config",
                width="stretch",
                on_click=save_config,
                args=(config_name, chart_type),
            )

        with c3:
            saved_configs = st.session_state.get("saved_configs", {})
            options = list(saved_configs.keys())
            selected_config = st.selectbox("Saved Configs", options=options)

        with c4:
            st.write("")
            st.write("")
            st.button(
                "📂 Load Config",
                width="stretch",
                on_click=load_config,
                args=(selected_config, chart_type, fields_available),
            )

        if "config_action_msg" in st.session_state:
            st.success(st.session_state["config_action_msg"])
            del st.session_state["config_action_msg"]
        st.divider()

        # Save
        st.write("**Save Chart**")
        save_chart()

# ==============================================================================
# 3. SETTINGS
# ==============================================================================
if step == "3. Settings":
    settings_web()
