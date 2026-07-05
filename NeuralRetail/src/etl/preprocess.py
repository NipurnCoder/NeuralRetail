import pandas as pd

print("Loading dataset...")

df = pd.read_csv(
    "data/raw/online_retail.csv",
    encoding="latin1"
)

print("Original Shape:")
print(df.shape)

df.drop_duplicates(inplace=True)

df.dropna(
    subset=['CustomerID'],
    inplace=True
)

df['InvoiceDate'] = pd.to_datetime(
    df['InvoiceDate']
)

df['Sales'] = (
    df['Quantity']
    *
    df['UnitPrice']
)

print("\nAfter Cleaning:")
print(df.shape)

df.to_csv(

    'data/processed/clean.csv',

    index=False

)

print("\nSaved Successfully")

print(df.head())