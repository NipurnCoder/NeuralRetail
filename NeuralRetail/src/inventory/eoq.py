import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/processed/clean.csv"
)

inventory = df.groupby(
    "StockCode"
).agg({

"Quantity":"sum"

}).reset_index()

inventory.rename(

columns={

"Quantity":"AnnualDemand"

},

inplace=True

)

inventory["OrderingCost"] = 50

inventory["HoldingCost"] = 5

inventory["EOQ"] = np.sqrt(

(

2

*

inventory["AnnualDemand"]

*

inventory["OrderingCost"]

)

/

inventory["HoldingCost"]

)

inventory.to_csv(

"data/processed/inventory_metrics.csv",

index=False

)

print()

print(inventory.head())

print()

print("EOQ Completed")