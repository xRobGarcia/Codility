import numpy as np
import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {"cat": ["x", "y", "x"] * 10000, "val": np.random.rand(30000)}
    )

    df["cat"] = df["cat"].astype("category")
    filtered = df.query("val > 0.9")

    print("Filtered rows:", len(filtered))


if __name__ == "__main__":
    main()
