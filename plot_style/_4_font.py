def apply_font_plot(ax, fonts):
    _apply_font_to_text(ax.title, fonts.get("title"))
    _apply_font_to_text(ax.xaxis.label, fonts.get("xlabel"))
    _apply_font_to_text(ax.yaxis.label, fonts.get("ylabel"))

    for txt in ax.get_xticklabels():
        _apply_font_to_text(txt, fonts.get("xticks"))
    for txt in ax.get_yticklabels():
        _apply_font_to_text(txt, fonts.get("yticks"))

    for txt in ax.texts:
        gid = txt.get_gid()

        if gid == "pielabel":
            _apply_font_to_text(txt, fonts.get("pielabel"))
        if gid == "pielabel_inner":
            _apply_font_to_text(txt, fonts.get("pielabel_inner"))
        if gid == "pielabel_outer":
            _apply_font_to_text(txt, fonts.get("pielabel_outer"))

    for txt in getattr(ax, "texts", []):
        get_gid = getattr(txt, "get_gid", None)

        if callable(get_gid) and get_gid() == "labels_bar_numbers":
            _apply_font_to_text(txt, fonts.get("labels_bar_numbers"))
        if callable(get_gid) and get_gid() == "labels_extra":
            _apply_font_to_text(txt, fonts.get("labels_extra"))


def apply_font_legend(legend, fonts):
    _apply_font_to_text(legend.get_title(), fonts.get("legend_title"))

    for text in legend.get_texts():
        _apply_font_to_text(text, fonts.get("legend_text"))


def _apply_font_to_text(text, font):
    if not font:
        return

    if "family" in font:
        text.set_fontfamily(font["family"])
    if "size" in font:
        text.set_fontsize(font["size"])
    if "weight" in font:
        text.set_fontweight(font["weight"])
    if "style" in font:
        text.set_fontstyle(font["style"])
    if "stretch" in font:
        text.set_fontstretch(font["stretch"])
