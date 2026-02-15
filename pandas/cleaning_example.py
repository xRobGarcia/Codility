import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "name": [" Ana ", "BOB", None],
            "age": ["34", "n/a", "29"],
            "email": ["ana@example.com", "bob@EXAMPLE.com", "c@x.com"],
        }
    )

    df["name"] = df["name"].str.strip().str.title()
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["age"] = df["age"].fillna(df["age"].median())
    df["email"] = df["email"].str.lower()

    print(df)


if __name__ == "__main__":
    main()
