import streamlit as st
import io

import setup.setup_functions as setup_module
from setup.setup_functions import (
    bar_1D,
    bar_2D,
    heatmap,
    pie_nested,
    pie,
    prisma,
    sankey,
    scatter,
    stacked,
    sunburst,
    worldmap,
)

from web.tools import (
    initialize_state,
    inject_config_to_module,
)
from web.web_datasets import (
    data_preparation_web,
)
from web.web_functions import (
    bar_1D_web,
    bar_2D_web,
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
            ],
        )

        CHARTS = {
            "bar_1D": {"setup": bar_1D, "web": bar_1D_web},
            "bar_2D": {"setup": bar_2D, "web": bar_2D_web},
        }

        dataset_selected = st.session_state["data_versions"][dataset]
        fields_available = list(dataset_selected.keys())

        setup_function = CHARTS[chart_type]["setup"]
        web_function = CHARTS[chart_type]["web"]

        st.subheader(f"Dataset: {dataset}")
        st.divider()

        # Render Chart UI
        params_chart = web_function(dataset_selected, fields_available)
        st.divider()

        # Draw Logic
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
            saved_legends = st.session_state.get("generated_legends", []) or []
            saved_extras = st.session_state.get("generated_extra_artists", []) or []
            all_artists = saved_legends + saved_extras
            st.pyplot(
                st.session_state["generated_fig"],
                bbox_inches="tight",
                bbox_extra_artists=all_artists,
            )
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
                label="💾 Save Chart",
                data=buffer,
                file_name=f"{save_filename}.{save_fileformat}",
                mime=f"image/{save_fileformat}",
            )
        else:
            st.info("ℹ️ Please generate a chart first to enable downloading.")

# ==============================================================================
# 3. SETTINGS
# ==============================================================================
if step == "3. Settings":
    settings_web()
