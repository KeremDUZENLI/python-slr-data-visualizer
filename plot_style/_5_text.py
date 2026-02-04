def text_clean_labels(texts, casetype="title"):
    for text in texts:
        text.set_text(_text_clean(text.get_text(), casetype=casetype))


def text_clean_legend(legend, casetype="title"):
    for text in legend.get_texts():
        text.set_text(_text_clean(text.get_text(), casetype=casetype))
    return legend


def _text_clean(name, casetype="title"):
    text = str(name).replace("_", " ").strip()

    if casetype == "title":
        return text.title()
    if casetype == "upper":
        return text.upper()
    if casetype == "original":
        return text
