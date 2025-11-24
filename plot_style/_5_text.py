def update_text_labels(texts):
    for text in texts:
        text.set_text(_clean_label(text.get_text()))


def update_text_legend(legend):
    for text in legend.get_texts():
        text.set_text(_clean_label(text.get_text()))
    return legend


def _clean_label(name):
    return str(name).replace("_", " ").strip().title()
