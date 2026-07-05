import pandas as pd

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv(

'data/processed/segments.csv'

)

X = df[[

'Recency',

'Frequency',

'Monetary'

]]

pca = PCA(

n_components=2

)

components = pca.fit_transform(

X

)

plt.figure(

figsize=(10,8)

)

plt.scatter(

components[:,0],

components[:,1],

c=df['Segment']

)

plt.title(

'Customer Segments'

)

plt.savefig(

'reports/segments.png'

)

plt.show()