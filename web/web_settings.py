import streamlit as st
import ast, json, copy

from web.tools import get_defaults

DEFAULTS = get_defaults()


def settings_web():
    st.title("⚙️ Settings")
    st.info("💡 Changes made here apply immediately to Chart Creation")

    tab_colors, tab_fonts_plot, tab_fonts_legend, tab_prisma = st.tabs(
        [
            "🎨 Colors",
            "🔤 Fonts (Plot)",
            "🔤 Fonts (Legend)",
            "💠 Prisma Style",
        ]
    )

    with tab_colors:
        st.write("**Chart Colors**")
        cfg_colors = json.dumps(st.session_state["cfg_colors"], indent=4)
        txt_colors = st.text_area(
            "Colors Config", value=cfg_colors, height=500, key="txt_colors"
        )

        co1, co2 = st.columns([0.2, 0.8])
        with co1:
            if st.button("💾 Save Colors"):
                try:
                    st.session_state["cfg_colors"] = ast.literal_eval(txt_colors)
                    st.session_state["config_msg"] = (
                        "success",
                        "✅ Colors updated successfully!",
                    )
                    st.rerun()
                except Exception as e:
                    st.session_state["config_msg"] = (
                        "error",
                        f"❌ Invalid format: {e}",
                    )
                    st.rerun()
        with co2:
            st.button(
                "🔄 Reset Colors",
                on_click=_reset_to_default,
                args=(
                    "cfg_colors",
                    "txt_colors",
                    "COLORS",
                    "Colors reset to default.",
                ),
            )

    with tab_fonts_plot:
        st.write("**Plot Fonts**")
        cfg_fonts_plot = json.dumps(st.session_state["cfg_fonts_plot"], indent=4)
        txt_fonts_plot = st.text_area(
            "Plot Fonts Config", value=cfg_fonts_plot, height=500, key="txt_fonts_plot"
        )

        fo1, fo2 = st.columns([0.2, 0.8])
        with fo1:
            if st.button("💾 Save Plot Fonts"):
                try:
                    st.session_state["cfg_fonts_plot"] = ast.literal_eval(
                        txt_fonts_plot
                    )
                    st.session_state["config_msg"] = (
                        "success",
                        "✅ Plot Fonts updated successfully!",
                    )
                    st.rerun()
                except Exception as e:
                    st.session_state["config_msg"] = (
                        "error",
                        f"❌ Invalid format: {e}",
                    )
                    st.rerun()
        with fo2:
            st.button(
                "🔄 Reset Plot Fonts",
                on_click=_reset_to_default,
                args=(
                    "cfg_fonts_plot",
                    "txt_fonts_plot",
                    "FONTS_PLOT",
                    "Plot Fonts reset to default.",
                ),
            )

    with tab_fonts_legend:
        st.write("**Legend Fonts**")
        cfg_fonts_legend = json.dumps(st.session_state["cfg_fonts_legend"], indent=4)
        txt_fonts_legend = st.text_area(
            "Legend Fonts Config",
            value=cfg_fonts_legend,
            height=500,
            key="txt_fonts_legend",
        )

        fl1, fl2 = st.columns([0.2, 0.8])
        with fl1:
            if st.button("💾 Save Legend Fonts"):
                try:
                    st.session_state["cfg_fonts_legend"] = ast.literal_eval(
                        txt_fonts_legend
                    )
                    st.session_state["config_msg"] = (
                        "success",
                        "✅ Legend Fonts updated successfully!",
                    )
                    st.rerun()
                except Exception as e:
                    st.session_state["config_msg"] = (
                        "error",
                        f"❌ Invalid format: {e}",
                    )
                    st.rerun()
        with fl2:
            st.button(
                "🔄 Reset Legend Fonts",
                on_click=_reset_to_default,
                args=(
                    "cfg_fonts_legend",
                    "txt_fonts_legend",
                    "FONTS_LEGEND",
                    "Legend Fonts reset to default.",
                ),
            )

    with tab_prisma:
        st.write("**Prisma Diagram Styles**")
        cfg_prisma = json.dumps(st.session_state["cfg_prisma"], indent=4)
        txt_prisma = st.text_area(
            "Prisma Styles Config", value=cfg_prisma, height=500, key="txt_prisma"
        )

        p1, p2 = st.columns([0.2, 0.8])
        with p1:
            if st.button("💾 Save Prisma Style"):
                try:
                    st.session_state["cfg_prisma"] = ast.literal_eval(txt_prisma)
                    st.session_state["config_msg"] = (
                        "success",
                        "✅ Prisma Style updated successfully!",
                    )
                    st.rerun()
                except Exception as e:
                    st.session_state["config_msg"] = (
                        "error",
                        f"❌ Invalid format: {e}",
                    )
                    st.rerun()
        with p2:
            st.button(
                "🔄 Reset Prisma Style",
                on_click=_reset_to_default,
                args=(
                    "cfg_prisma",
                    "txt_prisma",
                    "STYLE_PRISMA",
                    "Prisma Style reset to default.",
                ),
            )
    st.divider()

    if "config_msg" in st.session_state:
        msg_type, msg_text = st.session_state["config_msg"]
        if msg_type == "success":
            st.success(msg_text)
        elif msg_type == "warning":
            st.warning(msg_text)
        elif msg_type == "error":
            st.error(msg_text)
        del st.session_state["config_msg"]


def _reset_to_default(state_key, widget_key, default_key, message):
    default_data = DEFAULTS[default_key]
    st.session_state[state_key] = copy.deepcopy(default_data)
    st.session_state[widget_key] = json.dumps(default_data, indent=4)
    st.session_state["config_msg"] = ("warning", message)
