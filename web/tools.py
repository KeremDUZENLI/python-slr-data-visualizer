import streamlit as st
import copy, io

from config.config import (
    COLORS,
    FONTS_PLOT,
    FONTS_LEGEND,
    STYLE_PRISMA,
)


def get_defaults():
    return {
        "COLORS": COLORS,
        "FONTS_PLOT": FONTS_PLOT,
        "FONTS_LEGEND": FONTS_LEGEND,
        "STYLE_PRISMA": STYLE_PRISMA,
    }


def initialize_state():
    if "data_versions" not in st.session_state:
        st.session_state["data_versions"] = {}

    if "cfg_colors" not in st.session_state:
        st.session_state["cfg_colors"] = COLORS
    if "cfg_fonts_plot" not in st.session_state:
        st.session_state["cfg_fonts_plot"] = FONTS_PLOT
    if "cfg_fonts_legend" not in st.session_state:
        st.session_state["cfg_fonts_legend"] = FONTS_LEGEND
    if "cfg_prisma" not in st.session_state:
        st.session_state["cfg_prisma"] = STYLE_PRISMA


def inject_config_to_module(target_module):
    config_map = {
        "cfg_colors": "COLORS",
        "cfg_fonts_plot": "FONTS_PLOT",
        "cfg_fonts_legend": "FONTS_LEGEND",
        "cfg_prisma": "STYLE_PRISMA",
    }
    for state_key, module_var in config_map.items():
        if state_key in st.session_state:
            setattr(target_module, module_var, st.session_state[state_key])


def save_config(config_name, chart_type):
    if not config_name:
        return

    if "saved_configs" not in st.session_state:
        st.session_state["saved_configs"] = {}

    prefix_map = {
        "bar_1D": "1d_",
        "bar_2D": "2d_",
        "stacked": "stk_",
        "pie": "pie_",
        "pie_nested": "pien_",
        "heatmap": "hm_",
        "scatter": "sct_",
        "sunburst": "sb_",
        "sankey": "snk_",
        "worldmap": "wm_",
        "prisma": "prm_",
    }
    prefix = prefix_map.get(chart_type, "")

    forbidden_substrings = ["add", "rem", "btn"]

    state_to_save = {}
    for k, v in st.session_state.items():
        if k.startswith(prefix):
            if any(sub in k for sub in forbidden_substrings):
                continue

            generic_key = k[len(prefix) :]
            state_to_save[generic_key] = v

    st.session_state["saved_configs"][config_name] = {
        "chart_type": chart_type,
        "state": copy.deepcopy(state_to_save),
    }

    st.session_state["config_action_msg"] = f"Saved: {config_name}"


def load_config(config_name, target_chart_type, fields_available):
    if not config_name or config_name == "Select Config":
        return

    if "saved_configs" not in st.session_state:
        st.session_state["saved_configs"] = {}

    config = st.session_state["saved_configs"].get(config_name)
    if not config:
        return

    state_to_load = config["state"]

    prefix_map = {
        "bar_1D": "1d_",
        "bar_2D": "2d_",
        "stacked": "stk_",
        "pie": "pie_",
        "pie_nested": "pien_",
        "heatmap": "hm_",
        "scatter": "sct_",
        "sunburst": "sb_",
        "sankey": "snk_",
        "worldmap": "wm_",
        "prisma": "prm_",
    }
    target_prefix = prefix_map.get(target_chart_type, "")

    list_field_keys = ["fields", "filter_pre", "pre_1", "pre_2"]
    single_field_exact = [
        "x",
        "y",
        "z",
        "color",
        "col_in",
        "col_out",
        "le",
        "fc_f",
        "fc_f1",
        "fc_f2",
    ]

    forbidden_substrings = ["add", "rem", "btn"]

    for generic_k, v in state_to_load.items():
        if any(sub in generic_k for sub in forbidden_substrings):
            continue

        target_key = target_prefix + generic_k

        if generic_k in list_field_keys:
            if isinstance(v, list):
                st.session_state[target_key] = [f for f in v if f in fields_available]

        elif (
            generic_k in single_field_exact
            or generic_k.startswith("f_")
            or generic_k.startswith("leg_val_")
            or generic_k.startswith("leg_col_")
            or generic_k.startswith("fsf_")
        ):

            if v in fields_available or v in ["count", None]:
                st.session_state[target_key] = v
            else:
                if target_key in st.session_state:
                    del st.session_state[target_key]

        else:
            st.session_state[target_key] = v

    st.session_state["config_action_msg"] = f"Loaded: {config_name}"


def save_chart():
    if "generated_fig" in st.session_state:
        fig = st.session_state["generated_fig"]
        is_plotly = type(fig).__module__.startswith("plotly")
        is_graphviz = type(fig).__name__ == "Digraph"

        s1, s2 = st.columns(2)
        save_filename = s1.text_input("Filename", "chart")

        if is_plotly:
            formats = ["png", "jpg", "svg", "pdf", "html"]
        elif is_graphviz:
            formats = ["png", "pdf", "svg"]
        else:
            formats = ["png", "jpg", "svg", "pdf"]

        save_fileformat = s2.selectbox("Format", formats)

        buffer = io.BytesIO()

        try:
            if is_plotly:
                if save_fileformat == "html":
                    html_bytes = fig.to_html(include_plotlyjs="cdn").encode("utf-8")
                    buffer.write(html_bytes)
                else:
                    fig.write_image(buffer, format=save_fileformat)

            elif is_graphviz:
                raw_bytes = fig.pipe(format=save_fileformat)
                buffer.write(raw_bytes)

            else:
                saved_legends = st.session_state.get("generated_legends", []) or []
                saved_extras = st.session_state.get("generated_extra_artists", []) or []
                all_artists = saved_legends + saved_extras

                fig.savefig(
                    buffer,
                    format=save_fileformat,
                    dpi=300,
                    bbox_inches="tight",
                    bbox_extra_artists=all_artists,
                )

            buffer.seek(0)

            mime_type = (
                "text/html" if save_fileformat == "html" else f"image/{save_fileformat}"
            )

            st.download_button(
                label="💾 Save Chart",
                data=buffer,
                file_name=f"{save_filename}.{save_fileformat}",
                mime=mime_type,
                key=f"dl_btn_{save_fileformat}",
            )

        except ValueError as e:
            if "kaleido" in str(e).lower():
                st.error(
                    "❌ Cannot save Plotly image. 'kaleido' package is missing. Please `pip install kaleido` or save as HTML."
                )
            else:
                st.error(f"❌ Error saving chart: {e}")
        except Exception as e:
            st.error(f"❌ Error saving chart: {e}")

    else:
        st.info("ℹ️ Please generate a chart first to enable downloading.")
