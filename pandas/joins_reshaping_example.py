import pandas as pd


def main() -> None:
    left = pd.DataFrame({"id": [1, 2], "city": ["MX", "CDMX"]})
    right = pd.DataFrame({"id": [1, 2], "sales": [100, 200]})

    merged = left.merge(right, on="id")

    wide = pd.DataFrame(
        {"id": [1, 2], "2025_Q1": [10, 20], "2025_Q2": [15, 25]}
    )
    long = wide.melt(id_vars="id", var_name="quarter", value_name="value")

    print("Merged:")
    print(merged)
    print("\nLong:")
    print(long)


if __name__ == "__main__":
    main()
