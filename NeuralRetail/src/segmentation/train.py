import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv(
    "data/processed/rfm.csv"
)

features = [

    "Recency",
    "Frequency",
    "Monetary"

]

X = df[features]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = KMeans(

    n_clusters=6,

    random_state=42

)

model.fit(X_scaled)

labels = model.labels_

score = silhouette_score(

    X_scaled,

    labels

)

print()

print("Silhouette Score")

print(score)

df["Segment"] = labels

joblib.dump(

    model,

    "models/kmeans.pkl"

)

joblib.dump(

    scaler,

    "models/scaler.pkl"

)

df.to_csv(

    "data/processed/segments.csv",

    index=False

)

print()

print("Segmentation Completed")