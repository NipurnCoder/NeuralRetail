import pandas as pd

df = pd.read_csv(
    "data/processed/inventory_metrics.csv"
)

lead_time = 7

daily_demand = (
    df["AnnualDemand"] / 365
)

df["ROP"] = (
    daily_demand * lead_time
    + df["SafetyStock"]
)

df.to_csv(
    "data/processed/inventory_metrics.csv",
    index=False
)

print(df.head())

print("\nROP Added Successfully")