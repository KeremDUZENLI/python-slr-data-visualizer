def text_update_labels(texts, version="title"):
    for text in texts:
        text.set_text(_text_format(text.get_text(), version=version))


def text_update_legend(legend, version="title"):
    for text in legend.get_texts():
        text.set_text(_text_format(text.get_text(), version=version))
    return legend


def _text_format(name, version="title"):
    text = str(name).replace("_", " ").strip()

    if version == "title":
        return text.title()
    if version == "upper":
        return text.upper()
    if version == "original":
        return text
