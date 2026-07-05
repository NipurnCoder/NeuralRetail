import pandas as pd

df = pd.read_csv(

"data/processed/inventory_metrics.csv"

)

df = df.sort_values(

"AnnualDemand",

ascending=False

)

df["Cumulative"] = (

df["AnnualDemand"]

.cumsum()

/

df["AnnualDemand"].sum()

)

def classify(x):

    if x <= 0.80:

        return "A"

    elif x <= 0.95:

        return "B"

    else:

        return "C"

df["Category"] = df["Cumulative"].apply(

classify

)

df.to_csv(

"data/processed/abc_analysis.csv",

index=False

)

print()

print(

df["Category"].value_counts()

)