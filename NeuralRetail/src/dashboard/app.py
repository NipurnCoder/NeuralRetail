import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image
import datetime

st.set_page_config(

page_title="NeuralRetail",

page_icon="🧠",

layout="wide"

)

BASE_DIR = Path(__file__).resolve().parents[2]

REPORTS = BASE_DIR / "reports"

####################################################

def show_image(name):

    path = REPORTS / name

    if path.exists():

        try:

            img = Image.open(path)

            st.image(

                img,

                use_container_width=True

            )

        except:

            st.warning(

                f"Unable to load {name}"

            )

    else:

        st.warning(

            f"{name} not found"

        )

####################################################

def load_csv(name):

    path = REPORTS / name

    if path.exists():

        return pd.read_csv(path)

    return None

####################################################

st.markdown("""

<style>

.stApp{

background:#030712;

color:white;

}

[data-testid="stSidebar"]{

background:#111827;

}

.block-container{

padding-top:1rem;

padding-left:2rem;

padding-right:2rem;

}

h1{

color:#60A5FA;

font-weight:700;

}

h2{

color:white;

}

footer{

visibility:hidden;

}

</style>

""",

unsafe_allow_html=True)

####################################################

st.title(

"🧠 NeuralRetail Analytics"

)

st.sidebar.title(

"🛒 NeuralRetail"

)

st.sidebar.caption(

"AI Powered Retail Intelligence"

)

st.sidebar.success(

"Production Ready"

)

st.sidebar.markdown("---")

module = st.sidebar.radio(

"Navigation",

[

"Overview",

"Forecasting",

"Segmentation",

"Churn",

"Inventory",

"Monitoring",

"About"

]

)

####################################################

if module=="Overview":

    st.header(

        "Executive Dashboard"

    )

    c1,c2,c3,c4,c5=st.columns(5)

    c1.metric(

        "Revenue",

        "$8.9M",

        "+12%"

    )

    c2.metric(

        "Customers",

        "4372",

        "+8%"

    )

    c3.metric(

        "Forecast Accuracy",

        "89%"

    )

    c4.metric(

        "Segments",

        "6"

    )

    c5.metric(

        "Savings",

        "$18K"

    )

    st.divider()

    st.subheader(

        "Platform Features"

    )

    st.info(

"""

Forecasting

Segmentation

Churn Analytics

Inventory Optimization

Monitoring

Business Intelligence

"""

)

####################################################

elif module=="Forecasting":

    st.header(

        "Demand Forecasting"

    )

    a,b,c=st.columns(3)

    a.metric(

        "MAPE",

        "10.4%"

    )

    b.metric(

        "Accuracy",

        "89%"

    )

    c.metric(

        "Horizon",

        "30 Days"

    )

    st.divider()

    show_image(

        "forecast.png"

    )

    forecast = load_csv(

        "future_30_days.csv"

    )

    if forecast is not None:

        st.subheader(

            "Forecast Table"

        )

        st.dataframe(

            forecast,

            use_container_width=True

        )

        st.download_button(

            "Download Forecast",

            forecast.to_csv(

                index=False

            ),

            file_name="forecast.csv"

        )

    with st.expander(

        "Forecast Insights"

    ):

        st.write(

"""

Positive demand trend observed.

Forecast generated using Prophet.

Confidence intervals available.

30-day horizon complete.

"""

)

####################################################

elif module=="Segmentation":

    st.header(

        "Customer Segmentation"

    )

    c1,c2,c3=st.columns(3)

    c1.metric(

        "Customers",

        "4372"

    )

    c2.metric(

        "Segments",

        "6"

    )

    c3.metric(

        "Silhouette",

        "0.516"

    )

    st.divider()

    show_image(

        "segments.png"

    )

    data = pd.DataFrame({

        "Segment":[

            "Champions",

            "Loyal",

            "Potential",

            "Premium",

            "At Risk",

            "Lost"

        ],

        "Customers":[

            521,

            834,

            1150,

            433,

            912,

            522

        ]

    })

    st.dataframe(

        data,

        use_container_width=True

    )

####################################################

elif module=="Churn":

    st.header(

        "Customer Churn"

    )

    a,b,c=st.columns(3)

    a.metric(

        "High Risk",

        "20"

    )

    b.metric(

        "Average Risk",

        "85%"

    )

    c.metric(

        "AUC",

        "0.94"

    )

    st.divider()

    show_image(

        "shap_summary.png"

    )

    st.warning(

"""

Recommended Actions

Loyalty Programs

Email Campaigns

Discount Coupons

Retention Strategies

"""

)

####################################################

elif module=="Inventory":

    st.header(

        "Inventory Optimization"

    )

    a,b,c,d=st.columns(4)

    a.metric(

        "SKUs",

        "36"

    )

    b.metric(

        "Lead Time",

        "10 Days"

    )

    c.metric(

        "Savings",

        "$18K"

    )

    d.metric(

        "Reduction",

        "32%"

    )

    st.divider()

    show_image(

        "abc_chart.png"

    )

    st.success(

"""

Inventory Summary

EOQ Complete

Safety Stock Added

ROP Calculated

ABC Analysis Complete

Savings Estimated

$18K

"""

)

####################################################

elif module=="Monitoring":

    st.header(

        "Monitoring Center"

    )

    a,b,c=st.columns(3)

    a.metric(

        "Drift",

        "0.22"

    )

    b.metric(

        "Stockouts",

        "13"

    )

    c.metric(

        "Churn Spike",

        "19%"

    )

    st.divider()

    monitor = pd.DataFrame({

        "Metric":[

            "Drift",

            "Stockouts",

            "Weekly Avg",

            "Churn"

        ],

        "Value":[

            0.22,

            13,

            10,

            "19%"

        ]

    })

    st.dataframe(

        monitor,

        use_container_width=True

    )

    st.success(

        "System Healthy"

    )

    st.caption(

        f"Updated : {datetime.datetime.now()}"

    )

####################################################

elif module=="About":

    st.header(

        "About NeuralRetail"

    )

    st.markdown("""

### AI Powered Retail Analytics Platform

Modules

✔ Forecasting

✔ Segmentation

✔ Churn

✔ Inventory

✔ Monitoring

### Tech Stack

Python

Pandas

Scikit Learn

Prophet

PostgreSQL

Streamlit

Matplotlib

### Architecture

Raw Data

↓

ETL

↓

Feature Engineering

↓

Segmentation

↓

Forecasting

↓

Churn

↓

Inventory

↓

PostgreSQL

↓

Dashboard

### Deployment

Streamlit Cloud

### Developer

NIPURN

""")

####################################################

st.markdown("---")

st.caption(

"NeuralRetail © 2026"

)

st.caption(

"Developed by NIPURN"

)