def create_legend(ax, handles, title="", loc="best"):
    legend = ax.legend(
        handles=handles,
        title=title,
        loc=loc,
        bbox_to_anchor=(1, 0, 0.3, 1),
        borderaxespad=0.5,
        mode="expand",
        framealpha=0.5,
        # frameon=False,
    )

    ax.add_artist(legend)
    return legend
