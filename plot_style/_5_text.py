def text_clean_labels(texts, type="title"):
    for text in texts:
        text.set_text(_text_clean(text.get_text(), version=type))


def text_clean_legend(legend, type="title"):
    for text in legend.get_texts():
        text.set_text(_text_clean(text.get_text(), version=type))
    return legend


def _text_clean(name, version="title"):
    text = str(name).replace("_", " ").strip()

    if version == "title":
        return text.title()
    if version == "upper":
        return text.upper()
    if version == "original":
        return text
