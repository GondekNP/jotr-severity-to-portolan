from argparse import ArgumentParser
from pathlib import Path
import mypy
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt


def view_cog(path: Path) -> None:

    for path_tif in path.glob("*.tif"):
        with rasterio.open(path_tif) as dataset:
            fig, ax = plt.subplots(figsize=(10, 10))
            show(dataset, ax=ax)

            stem = path_tif.parent.stem

            ax.set_title(stem, fontsize=16)
            plt.savefig(path_tif.with_suffix(".png"), dpi=300, bbox_inches="tight")
            plt.close(fig)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("target_path")

    args = parser.parse_args()

    path = Path(args.target_path)

    print(f"Hello World - We will process {path}")
    view_cog(path)
