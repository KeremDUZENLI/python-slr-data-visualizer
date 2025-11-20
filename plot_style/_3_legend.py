def create_legend(ax, handles, title, loc, font=None):
    legend = ax.legend(
        handles=handles,
        title=title,
        loc=loc,
        fontsize=font.get("size") if font else None,
        title_fontsize=font.get("size") + 1 if font else None,
    )

    if font:
        for text in legend.get_texts():
            if "family" in font:
                text.set_fontfamily(font["family"])
            if "weight" in font:
                text.set_fontweight(font["weight"])

        title_text = legend.get_title()
        if "family" in font:
            title_text.set_fontfamily(font["family"])
        if "weight" in font:
            title_text.set_fontweight(font["weight"])

    ax.add_artist(legend)
