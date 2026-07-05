import pandas as pd

from sklearn.cluster import DBSCAN

from sklearn.preprocessing import StandardScaler

df = pd.read_csv(

'data/processed/rfm.csv'

)

X = df[[

'Recency',

'Frequency',

'Monetary'

]]

X = StandardScaler().fit_transform(

X

)

model = DBSCAN(

eps=0.5,

min_samples=10

)

labels = model.fit_predict(

X

)

df['DBSCAN'] = labels

df.to_csv(

'data/processed/dbscan.csv',

index=False

)

print(

df['DBSCAN'].value_counts()

)