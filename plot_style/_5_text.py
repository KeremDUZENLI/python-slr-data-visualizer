def update_text_labels(texts, version="title"):
    for text in texts:
        text.set_text(_clean_label(text.get_text(), version=version))


def update_text_legend(legend, version="title"):
    for text in legend.get_texts():
        text.set_text(_clean_label(text.get_text(), version=version))
    return legend


def _clean_label(name, version="title"):
    text = str(name).replace("_", " ").strip()

    if version == "title":
        return text.title()
    if version == "upper":
        return text.upper()
    if version == "original":
        return text
