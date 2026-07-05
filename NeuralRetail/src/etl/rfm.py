import pandas as pd

df = pd.read_csv(

'data/processed/clean.csv'

)

df['InvoiceDate'] = pd.to_datetime(

df['InvoiceDate']

)

snapshot = df['InvoiceDate'].max()

rfm = df.groupby(

'CustomerID'

).agg(

{

'InvoiceDate':

lambda x:

(snapshot - x.max()).days,

'InvoiceNo':'count',

'Sales':'sum'

}

)

rfm.columns=[

'Recency',

'Frequency',

'Monetary'

]

rfm.reset_index(

inplace=True

)

rfm.to_csv(

'data/processed/rfm.csv',

index=False

)

print(rfm.head())

print()

print(rfm.shape)