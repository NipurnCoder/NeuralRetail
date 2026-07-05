import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(

"data/processed/abc_analysis.csv"

)

counts = df["Category"].value_counts()

plt.figure(

figsize=(8,5)

)

counts.plot(

kind='bar'

)

plt.title(

"ABC Analysis"

)

plt.savefig(

"reports/abc_chart.png"

)

plt.show()