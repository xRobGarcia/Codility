import pandas as pd


def main() -> None:
    ts = pd.DataFrame(
        {
            "ts": pd.date_range("2025-01-01", periods=5, freq="D"),
            "sales": [10, 12, 9, 14, 18],
        }
    ).set_index("ts")

    weekly = ts.resample("W").sum()
    ts["rolling_3"] = ts["sales"].rolling(3).mean()
    ts["lag_1"] = ts["sales"].shift(1)

    print("Daily with features:")
    print(ts)
    print("\nWeekly sum:")
    print(weekly)


if __name__ == "__main__":
    main()
