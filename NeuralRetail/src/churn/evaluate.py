import pandas as pd

from sklearn.metrics import classification_report

from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier

df = pd.read_csv(

'data/processed/churn_data.csv'

)

X = df[[

'Recency',

'Frequency',

'Monetary'

]]

y = df['Churn']

X_train,X_test,y_train,y_test = train_test_split(

X,

y,

test_size=0.2,

random_state=42

)

model = XGBClassifier()

model.fit(

X_train,

y_train

)

pred = model.predict(

X_test

)

print(

classification_report(

y_test,

pred

)

)