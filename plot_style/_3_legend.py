def legend_create(ax, handles, legend_spec, **kwargs):
    legend = ax.legend(
        handles=handles,
        title=legend_spec.get("title", ""),
        loc=legend_spec.get("loc", "best"),
        bbox_to_anchor=legend_spec.get("bbox", (1, 0, 0.3, 1)),
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
    cbar = ax.figure.colorbar(im, ax=ax, label=title)
    cbar.outline.set_visible(False)


def legend_create_mapbar(ax, title=""):
    ax.update_traces(
        colorbar=dict(
            title=title,
            thickness=15,
            len=0.9,
            x=1.02,
            y=0.5,
            ypad=0,
            ticks="outside",
        )
    )

    return ax
