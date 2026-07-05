import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.metrics import roc_auc_score

from xgboost import XGBClassifier

df = pd.read_csv(

"data/processed/churn_data.csv"

)

X = df[[

"Recency",

"Frequency",

"Monetary"

]]

y = df["Churn"]

X_train,X_test,y_train,y_test = train_test_split(

X,

y,

test_size=0.2,

random_state=42

)

model = XGBClassifier(

n_estimators=100,

max_depth=4,

learning_rate=0.1,

random_state=42

)

model.fit(

X_train,

y_train

)

pred = model.predict_proba(

X_test

)[:,1]

auc = roc_auc_score(

y_test,

pred

)

print()

print("ROC-AUC")

print(auc)

joblib.dump(

model,

"models/churn.pkl"

)

print()

print("Saved Model")