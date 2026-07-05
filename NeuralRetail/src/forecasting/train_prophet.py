import pandas as pd
from prophet import Prophet
import joblib

print("Loading cleaned dataset...")

df = pd.read_csv(
    "data/processed/clean.csv"
)

df['InvoiceDate'] = pd.to_datetime(
    df['InvoiceDate']
)

df['Date'] = df['InvoiceDate'].dt.date

daily = (
    df.groupby('Date')['Sales']
    .sum()
    .reset_index()
)

daily.columns = ['ds', 'y']

daily['ds'] = pd.to_datetime(
    daily['ds']
)

print("Training Prophet Model...")

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)

model.fit(daily)

future = model.make_future_dataframe(
    periods=30
)

forecast = model.predict(
    future
)

forecast.to_csv(
    "data/processed/forecast.csv",
    index=False
)

# Save Prophet model
joblib.dump(
    model,
    "models/prophet.pkl"
)

print("\nForecast generated successfully!")

print("\nLast 5 Forecasted Days:\n")

print(
    forecast[
        [
            'ds',
            'yhat',
            'yhat_lower',
            'yhat_upper'
        ]
    ].tail()
)