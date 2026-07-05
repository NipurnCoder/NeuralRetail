import pandas as pd

df = pd.read_csv(

"data/processed/inventory_metrics.csv"

)

service_factor = 1.65

lead_time = 7

std_dev = 15

df["SafetyStock"] = (

service_factor

*

std_dev

*

(lead_time**0.5)

)

df.to_csv(

"data/processed/inventory_metrics.csv",

index=False

)

print()

print(df.head())

print()

print("Safety Stock Added")