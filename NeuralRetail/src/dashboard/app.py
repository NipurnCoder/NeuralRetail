import streamlit as st
import pandas as pd

from pathlib import Path
import os

st.write("Current directory:", os.getcwd())

BASE_DIR = Path(__file__).resolve().parents[2]

st.write("BASE_DIR:", BASE_DIR)

st.write("Reports exists:", (BASE_DIR / "reports").exists())

st.write("Forecast exists:",
         (BASE_DIR / "reports" / "forecast.png").exists())

st.set_page_config(
    page_title="NeuralRetail",
    layout="wide"
)

#################################################
# STYLE
#################################################

st.markdown("""
<style>

.stApp{
background-color:#050816;
color:white;
}

[data-testid="stSidebar"]{
background-color:#111827;
}

h1,h2,h3{
color:white;
}

.metric-box{
background:#111827;
padding:20px;
border-radius:12px;
text-align:center;
}

.metric-value{
font-size:30px;
font-weight:bold;
}

.metric-title{
font-size:14px;
color:gray;
}

.block-container{
padding-top:2rem;
}

</style>

""", unsafe_allow_html=True)

#################################################

st.title("🧠 NeuralRetail Analytics")

st.sidebar.title("🛒 NeuralRetail")

st.sidebar.markdown(
"AI Powered Retail Analytics Platform"
)

module = st.sidebar.radio(

"Navigate",

[
"Overview",
"Forecasting",
"Segmentation",
"Churn",
"Inventory",
"Monitoring"

]

)

#################################################
# OVERVIEW
#################################################

if module=="Overview":

    st.header("🚀 Overview")

    c1,c2,c3,c4 = st.columns(4)

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
        "Forecast Horizon",
        "30 Days"
    )

    c4.metric(
        "Segments",
        "6"
    )

    st.divider()

    st.subheader("Platform Features")

    st.markdown("""

• 📈 Demand Forecasting

• 👥 Customer Segmentation

• ⚠️ Churn Prediction

• 📦 Inventory Optimization

• 📊 Monitoring Dashboard

• 🤖 ML Powered Analytics

""")

#################################################
# FORECASTING
#################################################

elif module=="Forecasting":

    st.header("📈 Demand Forecasting")

    a,b,c = st.columns(3)

    a.metric("MAPE","10.4%")

    b.metric("Accuracy","89%")

    c.metric("Horizon","30 Days")

    st.divider()

    st.image(
        "reports/forecast.png",
        use_container_width=True
    )

    df = pd.read_csv(
        "reports/future_30_days.csv"
    )

    st.subheader(
        "Forecast Table"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

#################################################
# SEGMENTATION
#################################################

elif module=="Segmentation":

    st.header(
        "👥 Customer Segmentation"
    )

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Customers",
        "300"
    )

    c2.metric(
        "Segments",
        "6"
    )

    c3.metric(
        "Silhouette",
        "0.42"
    )

    st.divider()

    st.image(

        "reports/segments.png",

        use_container_width=True

    )

#################################################
# CHURN
#################################################

elif module=="Churn":

    st.header(
        "⚠️ Churn Dashboard"
    )

    a,b,c = st.columns(3)

    a.metric(

        "Customers",

        "20"

    )

    b.metric(

        "Avg Risk",

        "85.7%"

    )

    c.metric(

        "AUC",

        "0.94"

    )

    st.divider()

    st.image(

        "reports/shap_summary.png",

        use_container_width=True

    )

    st.success(

        "Average churn risk among top customers: 92%"

    )

#################################################
# INVENTORY
#################################################

elif module=="Inventory":

    st.header(

        "📦 Inventory Optimizer"

    )

    a,b,c,d = st.columns(4)

    a.metric(

        "SKUs",

        "36"

    )

    b.metric(

        "Lead Time",

        "10 Days"

    )

    c.metric(

        "Reduction",

        "32.7%"

    )

    d.metric(

        "Savings",

        "$18K"

    )

    st.divider()

    st.image(

        "reports/abc_chart.png",

        use_container_width=True

    )

#################################################
# MONITORING
#################################################

elif module=="Monitoring":

    st.header(

        "📊 Monitoring Dashboard"

    )

    c1,c2,c3 = st.columns(3)

    c1.metric(

        "Drift",

        "0.22"

    )

    c2.metric(

        "Stockouts",

        "13"

    )

    c3.metric(

        "Churn Spike",

        "19%"

    )

    st.divider()

    data = {

        "Metric":[

        "Drift Score",

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

    }

    df = pd.DataFrame(data)

    st.dataframe(

        df,

        use_container_width=True

    )

    st.warning(

        "Churn spike detected"

    )