def font_apply_plot(ax, fonts):
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
                    _font_apply_sunburst(trace, fonts)
                if trace.type == "sankey":
                    _font_apply_sankey(trace, fonts)
        return

    _font_apply_to_text(ax.title, fonts.get("title"))
    _font_apply_to_text(ax.xaxis.label, fonts.get("xlabel"))
    _font_apply_to_text(ax.yaxis.label, fonts.get("ylabel"))

    for txt in ax.get_xticklabels():
        _font_apply_to_text(txt, fonts.get("xticks"))
    for txt in ax.get_yticklabels():
        _font_apply_to_text(txt, fonts.get("yticks"))

    for txt in getattr(ax, "texts", []):
        get_gid = getattr(txt, "get_gid", None)
        gid = get_gid() if callable(get_gid) else None

        if not gid:
            continue

        if gid == "pie_label":
            _font_apply_to_text(txt, fonts.get("pie_label"))
        if gid == "pie_label_inner":
            _font_apply_to_text(txt, fonts.get("pie_label_inner"))
        if gid == "pie_label_outer":
            _font_apply_to_text(txt, fonts.get("pie_label_outer"))

        if gid == "labels_height_numbers":
            _font_apply_to_text(txt, fonts.get("labels_height_numbers"))
        if gid == "labels_heatmap_numbers":
            _font_apply_to_text(txt, fonts.get("labels_heatmap_numbers"))
        if gid == "labels_extra":
            _font_apply_to_text(txt, fonts.get("labels_extra"))


def font_apply_legend(legend, fonts):
    if hasattr(legend, "update_layout"):
        if legend.data:
            for trace in legend.data:
                if trace.type == "choropleth":
                    _font_apply_choropleth_legend(trace, fonts)
        return

    _font_apply_to_text(legend.get_title(), fonts.get("legend_title"))

    for text in legend.get_texts():
        _font_apply_to_text(text, fonts.get("legend_text"))


def _font_apply_to_text(text, font):
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


def _font_apply_to_dict(dict, font):
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


def _font_apply_sunburst(trace, fonts):
    font_inner = {}
    font_outer = {}

    _font_apply_to_dict(font_inner, fonts.get("sunburst_label_inner"))
    _font_apply_to_dict(font_outer, fonts.get("sunburst_label_outer"))

    if not font_inner:
        _font_apply_to_dict(font_inner, fonts.get("sunburst_label"))
    if not font_outer:
        _font_apply_to_dict(font_outer, fonts.get("sunburst_label"))

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


def _font_apply_sankey(trace, fonts):
    font_style = {}
    _font_apply_to_dict(font_style, fonts.get("sankey_label"))

    plotly_font = {}
    if "size" in font_style:
        plotly_font["size"] = font_style["size"]
    if "family" in font_style:
        plotly_font["family"] = font_style["family"]

    labels = trace.node.label
    new_labels = []

    for label in labels:
        fmt = label
        if font_style.get("weight") == "bold":
            fmt = f"<b>{fmt}</b>"
        if font_style.get("style") == "italic":
            fmt = f"<i>{fmt}</i>"
        new_labels.append(fmt)

    trace.update(textfont=plotly_font)
    trace.node.update(label=new_labels)


def _font_apply_choropleth_legend(trace, fonts):
    title_style = {}
    tick_style = {}
    _font_apply_to_dict(title_style, fonts.get("legend_title"))
    _font_apply_to_dict(tick_style, fonts.get("legend_text"))

    plotly_title_font = {}
    if "size" in title_style:
        plotly_title_font["size"] = title_style["size"]
    if "family" in title_style:
        plotly_title_font["family"] = title_style["family"]

    plotly_tick_font = {}
    if "size" in tick_style:
        plotly_tick_font["size"] = tick_style["size"]
    if "family" in tick_style:
        plotly_tick_font["family"] = tick_style["family"]

    label = trace.colorbar.title.text
    if label:
        fmt = label
        if title_style.get("weight") == "bold":
            fmt = f"<b>{fmt}</b>"
        if title_style.get("style") == "italic":
            fmt = f"<i>{fmt}</i>"
        trace.colorbar.title.text = fmt

    trace.colorbar.update(title_font=plotly_title_font, tickfont=plotly_tick_font)
