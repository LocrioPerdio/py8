import sys
import numpy as np
import numpy.typing as npt
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:

    matrix_x: npt.NDArray = np.sort(np.random.normal(50, 10, 1000))
    matrix_y: npt.NDArray = np.sort(np.random.choice(2000, 1000, replace=False))
    df: pd.DataFrame = pd.DataFrame({"level": matrix_x, "damage": matrix_y})
    df.plot(x="level", y="damage")
    plt.savefig("test")


if __name__ == "__main__":
    main()
