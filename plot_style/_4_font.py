def apply_font_plot(ax, fonts):
    if hasattr(ax, "update_layout"):
        title_font = fonts.get("title")
        plotly_title = {}

        if title_font:
            if "family" in title_font:
                plotly_title["family"] = title_font["family"]
            if "size" in title_font:
                plotly_title["size"] = title_font["size"]
        if plotly_title:
            ax.update_layout(title_font=plotly_title)
        if ax.data:
            for trace in ax.data:
                if trace.type == "sunburst":
                    _apply_fonts_sunburst(trace, fonts)
        return

    _apply_font_to_text(ax.title, fonts.get("title"))
    _apply_font_to_text(ax.xaxis.label, fonts.get("xlabel"))
    _apply_font_to_text(ax.yaxis.label, fonts.get("ylabel"))

    for txt in ax.get_xticklabels():
        _apply_font_to_text(txt, fonts.get("xticks"))
    for txt in ax.get_yticklabels():
        _apply_font_to_text(txt, fonts.get("yticks"))

    for txt in getattr(ax, "texts", []):
        get_gid = getattr(txt, "get_gid", None)
        gid = get_gid() if callable(get_gid) else None

        if not gid:
            continue

        if gid == "pie_label":
            _apply_font_to_text(txt, fonts.get("pie_label"))
        if gid == "pie_label_inner":
            _apply_font_to_text(txt, fonts.get("pie_label_inner"))
        if gid == "pie_label_outer":
            _apply_font_to_text(txt, fonts.get("pie_label_outer"))

        if gid == "labels_height_numbers":
            _apply_font_to_text(txt, fonts.get("labels_height_numbers"))
        if gid == "labels_heatmap_numbers":
            _apply_font_to_text(txt, fonts.get("labels_heatmap_numbers"))
        if gid == "labels_extra":
            _apply_font_to_text(txt, fonts.get("labels_extra"))


def apply_font_legend(legend, fonts):
    _apply_font_to_text(legend.get_title(), fonts.get("legend_title"))

    for text in legend.get_texts():
        _apply_font_to_text(text, fonts.get("legend_text"))


def _apply_font_to_text(text, font):
    if not font:
        return

    if "size" in font:
        text.set_fontsize(font["size"])
    if "family" in font:
        text.set_fontfamily(font["family"])
    if "weight" in font:
        text.set_fontweight(font["weight"])
    if "style" in font:
        text.set_fontstyle(font["style"])
    if "stretch" in font:
        text.set_fontstretch(font["stretch"])


def _apply_font_to_dict(dict, font):
    if not font:
        return

    if "size" in font:
        dict["size"] = font["size"]
    if "family" in font:
        dict["family"] = font["family"]
    if "weight" in font:
        dict["weight"] = font["weight"]
    if "style" in font:
        dict["style"] = font["style"]


def _apply_fonts_sunburst(trace, fonts):
    font_inner = {}
    font_outer = {}

    _apply_font_to_dict(font_inner, fonts.get("sunburst_label_inner"))
    _apply_font_to_dict(font_outer, fonts.get("sunburst_label_outer"))

    if not font_inner:
        _apply_font_to_dict(font_inner, fonts.get("sunburst_label"))
    if not font_outer:
        _apply_font_to_dict(font_outer, fonts.get("sunburst_label"))

    sizes = []
    families = []
    templates = []

    base_fmt = trace.texttemplate
    parents = trace.parents
    for parent in parents:
        if parent == "":
            style = font_inner
        else:
            style = font_outer

        sizes.append(style.get("size"))
        families.append(style.get("family"))

        fmt = base_fmt
        if style.get("weight") == "bold":
            fmt = f"<b>{fmt}</b>"
        if style.get("style") == "italic":
            fmt = f"<i>{fmt}</i>"

        templates.append(fmt)

    trace.update(
        insidetextfont=dict(size=sizes, family=families), texttemplate=templates
    )
