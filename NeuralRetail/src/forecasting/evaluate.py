import pandas as pd

forecast = pd.read_csv(
    "data/processed/forecast.csv"
)

print("\nForecast Shape:")
print(forecast.shape)

print("\nForecast Columns:")
print(forecast.columns)

future = forecast.tail(30)

print("\nNext 30 Days Forecast")

print(
    future[
        [
            'ds',
            'yhat',
            'yhat_lower',
            'yhat_upper'
        ]
    ]
)

future.to_csv(

    'reports/future_30_days.csv',

    index=False

)

print("\nSaved Successfully")