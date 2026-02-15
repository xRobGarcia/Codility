import pandas as pd


def main() -> None:
    df = pd.DataFrame({"team": ["A", "A", "B", "B"], "score": [10, 20, 7, 12]})

    summary = df.groupby("team")["score"].agg(["mean", "max"])

    df["team_avg"] = df.groupby("team")["score"].transform("mean")
    df["zscore"] = df.groupby("team")["score"].transform(
        lambda s: (s - s.mean()) / s.std()
    )

    print("Summary:")
    print(summary)
    print("\nWith features:")
    print(df)


if __name__ == "__main__":
    main()
