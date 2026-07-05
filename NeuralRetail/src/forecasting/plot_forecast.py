import pandas as pd
import matplotlib.pyplot as plt

forecast = pd.read_csv(

'data/processed/forecast.csv'

)

plt.figure(

figsize=(14,7)

)

plt.plot(

forecast['ds'],

forecast['yhat']

)

plt.xticks(rotation=45)

plt.title(

'Sales Forecast'

)

plt.savefig(

'reports/forecast.png'

)

plt.show()