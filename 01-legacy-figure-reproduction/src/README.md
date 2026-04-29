# Figure Reproduction Workflow

This folder contains a deterministic Matplotlib approximation of Figure 1 from
Jiang et al. (2024). The script draws the figure as editable geometry rather
than extracting numerical data from the paper, because the target is a schematic
of ray paths in layered VTI media.

## Run

Create the requested environment from the exercise root:

```powershell
conda env create -f environment.yml
conda activate exercise_1_legacy_figure_reproduction
python src/reproduce_figure.py
```

The script writes numbered images into `output/`:

- `figure_###.png`: reproduced schematic
- `comparison_###.png`: target figure beside the reproduced schematic

Existing output files are not overwritten.

## Assumptions and Approximations

- The original paper figure is conceptual, so all coordinates are approximate
  hand-tuned layer/interface and ray-path coordinates.
- Direct-wave and reflected-wave ray paths are drawn with the correct relative
  colors: red for qP, blue for qSV, and black for qSH.
- The source is placed at `x = 0` between `z^(e-1)` and `z^(e)`, and the
  receiver is placed on the surface at horizontal offset `X`.
- The layer stack, skipped-layer symbols, `Delta X_k`, `Delta Z_k`, Thomsen
  parameter annotation, source marker, receiver marker, axes, and legend are
  included to preserve the semantic content of the target.
- The geometry is not intended to reproduce the paper's ray-tracing method or
  numerical results.
