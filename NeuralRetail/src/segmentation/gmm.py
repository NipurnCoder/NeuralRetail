import pandas as pd

from sklearn.mixture import GaussianMixture

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

gmm = GaussianMixture(

n_components=6,

random_state=42

)

labels = gmm.fit_predict(

X

)

df['GMM'] = labels

df.to_csv(

'data/processed/gmm.csv',

index=False

)

print(

df['GMM'].value_counts()

)