"""Reproduce a schematic approximation of Jiang et al. (2024) Figure 1.

The original figure is conceptual, so this script uses fixed geometry rather
than recovered data. The goal is to make every approximation explicit and easy
to edit.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input"
OUTPUT = ROOT / "output"


@dataclass(frozen=True)
class Ray:
    name: str
    color: str
    direct: list[tuple[float, float]]
    reflected: list[tuple[float, float]]


LAYERS = [
    (0.0, r"$z^{(0)}$"),
    (1.0, r"$z^{(1)}$"),
    (2.0, r"$z^{(k-1)}$"),
    (3.0, r"$z^{(k)}$"),
    (4.0, r"$z^{(e-1)}$"),
    (5.0, r"$z^{(e)}$"),
    (6.0, r"$z^{(n-1)}$"),
    (7.0, r"$z^{(n)}$"),
]

SOURCE = (0.0, 4.4)
RECEIVER = (8.0, 0.0)

RAYS = [
    Ray(
        name="qP",
        color="#d7191c",
        direct=[SOURCE, (0.7, 4.0), (1.7, 3.4), (2.5, 3.0), (5.4, 1.0), RECEIVER],
        reflected=[
            SOURCE,
            (0.55, 5.0),
            (1.75, 7.0),
            (2.75, 6.0),
            (4.0, 5.0),
            (5.25, 4.0),
            (6.15, 3.0),
            (6.8, 2.0),
            (7.45, 1.0),
            RECEIVER,
        ],
    ),
    Ray(
        name="qSV",
        color="#2b83ba",
        direct=[SOURCE, (0.95, 4.0), (2.05, 3.4), (3.05, 3.0), (5.65, 1.0), RECEIVER],
        reflected=[
            SOURCE,
            (0.85, 5.0),
            (2.35, 7.0),
            (3.25, 6.0),
            (4.45, 5.0),
            (5.65, 4.0),
            (6.45, 3.0),
            (7.0, 2.0),
            (7.62, 1.0),
            RECEIVER,
        ],
    ),
    Ray(
        name="qSH",
        color="#111111",
        direct=[SOURCE, (1.25, 4.0), (2.45, 3.4), (3.55, 3.0), (6.0, 1.0), RECEIVER],
        reflected=[
            SOURCE,
            (1.25, 5.0),
            (2.95, 7.0),
            (4.0, 6.0),
            (5.05, 5.0),
            (6.0, 4.0),
            (6.75, 3.0),
            (7.2, 2.0),
            (7.78, 1.0),
            RECEIVER,
        ],
    ),
]


def next_numbered_path(prefix: str, suffix: str = ".png") -> Path:
    OUTPUT.mkdir(exist_ok=True)
    used = sorted(OUTPUT.glob(f"{prefix}_*{suffix}"))
    if not used:
        return OUTPUT / f"{prefix}_001{suffix}"

    last_number = max(int(path.stem.rsplit("_", 1)[-1]) for path in used)
    return OUTPUT / f"{prefix}_{last_number + 1:03d}{suffix}"


def draw_arrowed_path(
    ax: plt.Axes,
    points: list[tuple[float, float]],
    color: str,
    *,
    linestyle: str = "-",
    linewidth: float = 1.4,
    arrow_indices: tuple[int, ...] = (1, 3, 5),
) -> None:
    xs, ys = zip(*points)
    ax.plot(xs, ys, color=color, linestyle=linestyle, linewidth=linewidth)

    for segment_index in arrow_indices:
        if segment_index >= len(points):
            continue
        x0, y0 = points[segment_index - 1]
        x1, y1 = points[segment_index]
        start = (x0 + 0.58 * (x1 - x0), y0 + 0.58 * (y1 - y0))
        end = (x0 + 0.72 * (x1 - x0), y0 + 0.72 * (y1 - y0))
        ax.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops=dict(arrowstyle="-|>", color=color, lw=linewidth, mutation_scale=11),
        )


def draw_dimension(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    label: str,
    label_xy: tuple[float, float],
    *,
    color: str = "#111111",
    fontsize: int = 16,
) -> None:
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(arrowstyle="<->", color=color, lw=1.25, shrinkA=0, shrinkB=0),
    )
    ax.text(*label_xy, label, color=color, ha="center", va="center", fontsize=fontsize)


def draw_source(ax: plt.Axes) -> None:
    x, y = SOURCE
    ax.scatter(
        [x],
        [y],
        marker=(14, 1, 0),
        s=430,
        facecolor="0.65",
        edgecolor="0.1",
        linewidth=1.1,
        zorder=5,
    )
    ax.text(x + 0.75, y + 0.1, "Source", fontsize=18, ha="left", va="center")


def draw_receiver(ax: plt.Axes) -> None:
    x, y = RECEIVER
    ax.scatter(
        [x],
        [y - 0.18],
        marker="v",
        s=500,
        facecolor="0.55",
        edgecolor="0.1",
        linewidth=1.2,
        zorder=6,
    )
    ax.text(x + 0.42, y - 0.2, "Receiver", fontsize=18, ha="left", va="center")


def draw_layers(ax: plt.Axes) -> None:
    for depth, label in LAYERS:
        ax.hlines(depth, -1.1, 11.1, color="#111111", linewidth=1.8)
        ax.text(-1.35, depth, label, fontsize=15, ha="right", va="center")

    for y in (1.55, 3.55, 5.55):
        ax.text(0.0, y, r"$\approx$", fontsize=46, rotation=90, ha="center", va="center")


def draw_axes(ax: plt.Axes) -> None:
    ax.annotate("", xy=(11.2, 0.0), xytext=(-0.05, 0.0), arrowprops=dict(arrowstyle="-|>", lw=2.2))
    ax.annotate("", xy=(0.0, 8.1), xytext=(0.0, -0.6), arrowprops=dict(arrowstyle="-|>", lw=2.2))
    ax.text(11.25, 0.0, r"$x$", fontsize=30, ha="left", va="center")
    ax.text(0.0, 8.25, r"$z$", fontsize=30, ha="center", va="top")


def draw_annotations(ax: plt.Axes) -> None:
    draw_dimension(ax, (SOURCE[0], -0.27), (RECEIVER[0], -0.27), r"$X$", (4.0, -0.47), fontsize=18)
    ax.vlines([SOURCE[0], RECEIVER[0]], -0.42, 0.0, colors="#111111", linewidth=1.2)

    draw_dimension(ax, (1.65, 1.85), (3.6, 1.85), r"$\Delta X_k$", (2.62, 1.68), color="#d7191c")
    ax.vlines([1.65, 3.6], 1.75, 3.0, colors="#d7191c", linewidth=1.2)

    draw_dimension(ax, (1.65, 2.0), (1.65, 3.0), r"$\Delta Z_k$", (1.33, 2.5), color="#d7191c")
    draw_dimension(ax, (9.2, 2.0), (9.2, 3.0), r"$\Delta Z_k$", (8.92, 2.5), fontsize=16)
    ax.text(9.35, 2.5, r"$[\alpha_0,\beta_0,\epsilon,\delta,\lambda]_k$", fontsize=16, ha="left", va="center")


def draw_rays(ax: plt.Axes) -> None:
    for ray in RAYS:
        draw_arrowed_path(ax, ray.direct, ray.color, linestyle="--", arrow_indices=(1, 3, 5))
        draw_arrowed_path(ax, ray.reflected, ray.color, linestyle="-", arrow_indices=(1, 3, 5, 7, 9))


def add_legend(ax: plt.Axes) -> None:
    handles = [
        Line2D([0], [0], color=ray.color, lw=1.7, marker=">", markevery=[1], label=ray.name)
        for ray in RAYS
    ]
    ax.legend(
        handles=handles,
        frameon=False,
        fontsize=16,
        loc="upper right",
        bbox_to_anchor=(0.94, 0.94),
        handlelength=3.2,
        handletextpad=0.5,
    )


def build_reproduction() -> plt.Figure:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.linewidth": 0.0,
        }
    )
    fig, ax = plt.subplots(figsize=(11.2, 8.0))
    draw_layers(ax)
    draw_axes(ax)
    draw_rays(ax)
    draw_source(ax)
    draw_receiver(ax)
    draw_annotations(ax)
    add_legend(ax)

    ax.set_xlim(-1.7, 11.5)
    ax.set_ylim(8.45, -0.65)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    fig.tight_layout(pad=0.2)
    return fig


def save_comparison(reproduction_path: Path) -> Path:
    target = mpimg.imread(INPUT / "figure.jpg")
    reproduced = mpimg.imread(reproduction_path)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6.0))
    for ax, image, title in zip(
        axes,
        (target, reproduced),
        ("Target figure from paper", "Reproduced schematic"),
        strict=True,
    ):
        ax.imshow(image)
        ax.set_title(title, fontsize=13)
        ax.axis("off")

    fig.tight_layout()
    comparison_path = next_numbered_path("comparison")
    fig.savefig(comparison_path, dpi=180)
    plt.close(fig)
    return comparison_path


def main() -> None:
    figure = build_reproduction()
    figure_path = next_numbered_path("figure")
    figure.savefig(figure_path, dpi=220, facecolor="white")
    plt.close(figure)

    comparison_path = save_comparison(figure_path)
    print(f"Saved reproduced figure: {figure_path}")
    print(f"Saved comparison figure: {comparison_path}")


if __name__ == "__main__":
    main()
