import matplotlib.pyplot as plt


def draw_plot(width, height):
    fig, ax = plt.subplots(figsize=(width, height))

    return fig, ax


def show_plot():
    plt.tight_layout()
    plt.show()


def save_plot(fig, name, legends=None, extra_artists=None):
    if legends is None:
        legends = []
    if extra_artists is None:
        extra_artists = []
    all_artists = legends + extra_artists

    fig.savefig(
        f"figure/{name}.png",
        dpi=300,
        bbox_inches="tight",
        bbox_extra_artists=all_artists,
    )
