import pandas as pd

# Multiple aggregations in a pivot table.
df = pd.DataFrame(
    {
        "region": ["Norte", "Norte", "Sur", "Sur", "Sur"],
        "producto": ["A", "B", "A", "A", "B"],
        "ventas": [100, 120, 80, 90, 110],
        "unidades": [10, 12, 8, 9, 11],
    }
)

# Aggregate with sum and mean for multiple value columns.
tabla = pd.pivot_table(
    df,
    values=["ventas", "unidades"],
    index="region",
    columns="producto",
    aggfunc=["sum", "mean"],
    fill_value=0,
)

print(tabla)
