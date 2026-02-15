import pandas as pd


df = pd.DataFrame(
    {
        "region": ["Norte", "Norte", "Sur", "Sur", "Sur"],
        "producto": ["A", "B", "A", "A", "B"],
        "ventas": [100, 120, 80, 90, 110],
    }
)

tabla = pd.pivot_table(
    df,
    values="ventas",
    index="region",
    columns="producto",
    aggfunc="sum",
    fill_value=0,
)

print(tabla)
