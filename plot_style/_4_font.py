def apply_font_plot(ax, fonts):
    apply_font_title(ax, fonts.get("title"))
    apply_font_xlabel(ax, fonts.get("xlabel"))
    apply_font_ylabel(ax, fonts.get("ylabel"))
    apply_font_xticks(ax, fonts.get("xticks"))
    apply_font_yticks(ax, fonts.get("yticks"))
    apply_font_labels(ax, fonts.get("labels_bar_numbers"), gid="labels_bar_numbers")
    apply_font_labels(ax, fonts.get("labels_extra"), gid="labels_extra")


def apply_font_legend(legend, fonts):
    apply_font_legend_title(legend, fonts.get("legend_title"))
    apply_font_legend_text(legend, fonts.get("legend_text"))


def apply_font_title(ax, font):
    _apply_font_to_text(ax.title, font)


def apply_font_xlabel(ax, font):
    _apply_font_to_text(ax.xaxis.label, font)


def apply_font_ylabel(ax, font):
    _apply_font_to_text(ax.yaxis.label, font)


def apply_font_xticks(ax, font):
    for txt in ax.get_xticklabels():
        _apply_font_to_text(txt, font)


def apply_font_yticks(ax, font):
    for txt in ax.get_yticklabels():
        _apply_font_to_text(txt, font)


def apply_font_labels(ax, font, gid):
    for txt in getattr(ax, "texts", []):
        get_gid = getattr(txt, "get_gid", None)
        if callable(get_gid) and get_gid() == gid:
            _apply_font_to_text(txt, font)


def apply_font_legend_title(legend, font):
    _apply_font_to_text(legend.get_title(), font)


def apply_font_legend_text(legend, font):
    for text in legend.get_texts():
        _apply_font_to_text(text, font)


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
