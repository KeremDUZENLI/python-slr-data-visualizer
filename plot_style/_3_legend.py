def legend_create(ax, handles, title="", loc="best", bbox=None, **kwargs):
    if bbox is None:
        bbox = (1, 0, 0.3, 1)

    legend = ax.legend(
        handles=handles,
        title=title,
        loc=loc,
        bbox_to_anchor=bbox,
        borderaxespad=0.5,
        mode="expand",
        framealpha=0.5,
        # frameon=False,
        **kwargs,
    )

    ax.add_artist(legend)
    return legend


def legend_create_colorbar(ax, title=""):
    im = ax.images[0]
    ax.figure.colorbar(im, ax=ax, label=title)
