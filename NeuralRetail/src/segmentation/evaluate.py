import pandas as pd

df = pd.read_csv(

'data/processed/segments.csv'

)

summary = df.groupby(

'Segment'

).agg(

{

'Recency':'mean',

'Frequency':'mean',

'Monetary':'mean'

}

)

print(summary)

summary.to_csv(

'data/processed/segment_summary.csv'

)