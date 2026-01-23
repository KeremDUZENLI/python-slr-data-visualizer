def text_clean_labels(texts, version="title"):
    for text in texts:
        text.set_text(_text_clean(text.get_text(), version=version))


def text_clean_legend(legend, version="title"):
    for text in legend.get_texts():
        text.set_text(_text_clean(text.get_text(), version=version))
    return legend


def _text_clean(name, version="title"):
    text = str(name).replace("_", " ").strip()

    if version == "title":
        return text.title()
    if version == "upper":
        return text.upper()
    if version == "original":
        return text
