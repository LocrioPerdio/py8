import sys
import numpy as np
import numpy.typing as npt
import pandas as pd
import matplotlib.pyplot as plt
import importlib.metadata


def check_dependencies() -> None:
    try:
        version = importlib.metadata.version("pandas")
        if version == "2.1.0":
            print("[OK] pandas (2.1.0) - Data manipulation ready")
        else:
            print(f"[KO] pandas version: {version}. Needed '2.1.0'")
    except importlib.metadata.PackageNotFoundError:
        print("[KO] pandas package not found")
    try:
        version = importlib.metadata.version("numpy")
        if version == "1.25.0":
            print("[OK] numpy (1.25.0) - Numerical computation ready")
        else:
            print(f"[KO] numpy version: {version}. Needed '1.25.0'")
    except importlib.metadata.PackageNotFoundError:
            print("[KO] numpy package not found")
    try:
        version = importlib.metadata.version("matplotlib")
        if version == "3.7.2":
            print("[OK] matplotlib (3.7.2) - Visualization ready")
        else:
            print(f"[KO] matplotlib version: {version}. Needed '3.7.2'")
    except importlib.metadata.PackageNotFoundError:
        print("[KO] numpy package not found")


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")
    try:
        check_dependencies()
    except Exception:
        sys.exit()
    print("\n Analyzing Matrix data...")
    matrix_data: npt.NDArray = np.sort(
        np.random.choice(2000, 1000, replace=False))
    print("Processing 1000 data points...")
    df: pd.DataFrame = pd.DataFrame({"matrix_data": matrix_data})
    print("Generating visualization...\n")
    df.plot()
    print("Analysis complete!")
    file: str = "matrix_analysis.png"
    plt.savefig(file)
    print(f"Results saved to: {file}")


if __name__ == "__main__":
    main()
