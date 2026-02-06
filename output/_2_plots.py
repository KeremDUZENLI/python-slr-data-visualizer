import matplotlib.pyplot as plt
import plotly.graph_objects as go
import graphviz


# ----------------- Matplotlib -----------------


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


# ----------------- Plotly -----------------


def draw_plot_plotly():
    fig = go.Figure()
    return fig


def show_plot_plotly(fig):
    fig.show()


# ----------------- Graphviz -----------------


def draw_plot_graphviz(name, position, splines, nodesep, ranksep):
    dot = graphviz.Digraph(
        filename=name,
        directory="figure",
    )

    dot.attr(
        rankdir=position,
        splines=splines,
        nodesep=nodesep,
        ranksep=ranksep,
    )
    return dot


def show_plot_graphviz(dot):
    dot.view()


def save_plot_graphviz(dot, name):
    output_path = f"{name}"
    dot.render(
        output_path,
        format="png",
        cleanup=True,
    )
