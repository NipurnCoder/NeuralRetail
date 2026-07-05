import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="NeuralRetail",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[2]
REPORTS = BASE_DIR / "reports"


def show_image(filename):

    path = REPORTS / filename

    if path.exists():

        try:

            image = Image.open(path)

            st.image(

                image,

                use_container_width=True

            )

        except Exception as e:

            st.error(

                f"Cannot load {filename}"

            )

            st.write(e)

    else:

        st.warning(

            f"{filename} not found"

        )


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

#################################################

elif module=="Forecasting":

    st.header(

        "📈 Demand Forecasting"

    )

    a,b,c = st.columns(3)

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

    csv_file = REPORTS / "future_30_days.csv"

    if csv_file.exists():

        df = pd.read_csv(

            csv_file

        )

        st.dataframe(

            df,

            use_container_width=True

        )

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

    show_image(

        "segments.png"

    )

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

    show_image(

        "shap_summary.png"

    )

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

    show_image(

        "abc_chart.png"

    )

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

    df = pd.DataFrame(

        data

    )

    st.dataframe(

        df,

        use_container_width=True

    )

    st.warning(

        "Churn spike detected"

    )