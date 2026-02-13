import streamlit as st

from config.config import (
    COLORS,
    FONTS_PLOT,
    FONTS_LEGEND,
    STYLE_PRISMA,
)


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


def get_defaults():
    return {
        "COLORS": COLORS,
        "FONTS_PLOT": FONTS_PLOT,
        "FONTS_LEGEND": FONTS_LEGEND,
        "STYLE_PRISMA": STYLE_PRISMA,
    }
