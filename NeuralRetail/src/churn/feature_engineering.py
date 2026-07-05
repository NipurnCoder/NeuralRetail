import pandas as pd

df = pd.read_csv(
    "data/processed/rfm.csv"
)

# Simple churn definition

df["Churn"] = (

df["Recency"]

>

90

).astype(int)

df.to_csv(

"data/processed/churn_data.csv",

index=False

)

print()

print(df.head())

print()

print(

df["Churn"].value_counts()

)