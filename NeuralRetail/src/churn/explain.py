import pandas as pd
import shap
import joblib

model = joblib.load(

"models/churn.pkl"

)

df = pd.read_csv(

"data/processed/churn_data.csv"

)

X = df[[

"Recency",

"Frequency",

"Monetary"

]]

explainer = shap.TreeExplainer(

model

)

values = explainer.shap_values(

X

)

shap.summary_plot(

values,

X,

show=False

)

import matplotlib.pyplot as plt

plt.savefig(

"reports/shap_summary.png"

)

print(

"SHAP plot saved"

)