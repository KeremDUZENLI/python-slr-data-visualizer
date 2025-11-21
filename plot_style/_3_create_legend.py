def create_legend(ax, handles, title, loc):
    legend = ax.legend(
        handles=handles,
        title=title,
        loc=loc,
    )

    ax.add_artist(legend)
    return legend
