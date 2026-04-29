# Data

## Figure 1 from Jiang et al. (2024)

We take Figure 1 from this paper:

Jiang, X., Pan, X., Yang, H., Zhang, W., & Chen, X. (2024). A fast and robust two‐point ray tracing method in layered vertical transversely isotropic media with strong anisotropy. *Geophysical Prospecting*, 73(3), 861–873. <https://doi.org/10.1111/1365-2478.13585>

The figure is in `input/figure.jpg`.

Figure caption from the paper:

A schematic diagram illustrates the ray paths of direct waves and reflected waves in layered vertical transversely isotropic (VTI) media $z^{(k)}$ and $\Delta Z_k$, respectively, represent the $k$-th layer depth and thickness. $[\alpha_0, \beta_0, \epsilon, \delta, \gamma]$ are the $k$-th layer Thomsen anisotropic parameters. One source in layer $e$ and one receiver on the surface are shown. The ray paths of the direct waves travel from the $e$-th layer to the surface, whereas the ray paths of the reflected wave involve reflection from the $n$-th interface. The different coloured paths represent different wave types: red for quasi-P (qP) wave, blue for quasi-SV (qSV) wave and black for quasi-SH (qSH) wave. $X$ denotes the horizontal offset between the source and the receiver, $\Delta X_k$ represents the $k$-th layer horizontal ray path.

The paper itself is in `input/paper.pdf` for local reading.

## Additional Details

- $z$ levels ($z^{(0)}, z^{(1)}, z^{(k-1)}, z^{(k)}, z^{(e-1), z^{(e)}}, z^{(n-1)}, z^{(n)}$) represent the depths of the layer interfaces.
- Layers between these $z^{(1)}$ and $z^{(k)}$, and between $z^{(k)}$ and $z^{(e-1)}$, and between $z^{(e)}$ and $z^{(n-1)}$ are denoted by double tildas in the figure, indicating that there may be multiple layers in these regions.
- The source marked as a star-like blast is located at $x = 0$ in the $e$-th layer, which means it is between the depths of $z^{(e-1)}$ and $z^{(e)}$.
- The receiver marked as triangle pointing down is located at the surface, which corresponds to a depth of 0 m ($z^{(0)}$). The horizontal offset $X$ is the distance between the source and receiver along the horizontal axis.
- qP ray path is shown in red, qSV ray path is shown in blue, and qSH ray path is shown in black. The direct waves travel from the source to the receiver, while the reflected waves involve reflection from the $n$-th interface.

