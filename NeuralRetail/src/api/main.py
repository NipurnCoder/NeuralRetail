from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="NeuralRetail API",
    version="1.0"
)

@app.get("/")
def home():

    return {

        "message":"NeuralRetail Running"

    }


@app.get("/health")
def health():

    return {

        "status":"OK"

    }


@app.get("/forecast")
def forecast():

    df = pd.read_csv(

        "reports/future_30_days.csv"

    )

    return df.to_dict(

        orient="records"

    )


@app.get("/segments")
def segments():

    df = pd.read_csv(

        "data/processed/rfm_segments.csv"

    )

    return df.head(

        100

    ).to_dict(

        orient="records"

    )


@app.get("/inventory")
def inventory():

    df = pd.read_csv(

        "data/processed/inventory_metrics.csv"

    )

    return df.to_dict(

        orient="records"

    )


@app.get("/churn")
def churn():

    df = pd.read_csv(

        "data/processed/churn_data.csv"

    )

    return df.head(

        100

    ).to_dict(

        orient="records"

    )