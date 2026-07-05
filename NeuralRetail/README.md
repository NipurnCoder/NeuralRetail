# 🧠 NeuralRetail

AI-Powered Retail Analytics Platform built using Machine Learning, FastAPI, Streamlit, and PostgreSQL.

---

# 🚀 Features

### 📈 Demand Forecasting
- 30-day sales forecasting
- Prophet based predictions
- Forecast visualization
- Future sales CSV export

### 👥 Customer Segmentation
- K-Means clustering
- Segment visualization
- Customer grouping analysis

### ⚠️ Churn Prediction
- Churn risk scoring
- SHAP Explainability
- High-risk customer identification

### 📦 Inventory Optimization
- ABC Analysis
- EOQ Calculation
- Safety Stock Estimation
- Reorder Point Prediction

### 📊 Monitoring Dashboard
- Drift Monitoring
- Stockout Alerts
- Churn Spike Detection
- KPI Tracking

---

# 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| Dashboard | Streamlit |
| Database | PostgreSQL |
| ML Models | Scikit-Learn |
| Forecasting | Prophet |
| Visualization | Matplotlib |
| Data Processing | Pandas |
| Deployment | Streamlit Cloud |

---

# 📂 Project Structure

```bash
NeuralRetail/

├── docs/
├── models/
│   ├── churn.pkl
│   ├── kmeans.pkl
│   ├── prophet.pkl
│   └── scaler.pkl
│
├── reports/
│   ├── abc_chart.png
│   ├── forecast.png
│   ├── future_30_days.csv
│   ├── segments.png
│   └── shap_summary.png
│
├── src/
│   ├── api/
│   │    └── main.py
│   │
│   ├── dashboard/
│   │    └── app.py
│   │
│   ├── forecasting/
│   ├── inventory/
│   ├── churn/
│   ├── segmentation/
│   └── database/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone repository

```bash
git clone https://github.com/yourusername/NeuralRetail.git

cd NeuralRetail
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

Start PostgreSQL

Create database

```sql
CREATE DATABASE neuralretail;
```

Run schema

```sql
\i schema.sql
```

---

# 🚀 Run FastAPI

```bash
uvicorn src.api.main:app --reload
```

API

```bash
http://127.0.0.1:8000
```

---

# 📊 Run Dashboard

```bash
streamlit run src/dashboard/app.py
```

Dashboard URL

```bash
http://localhost:8501
```

---

# 🤖 Machine Learning Models

| Model | Purpose |
|-------|---------|
| KMeans | Segmentation |
| Prophet | Forecasting |
| Random Forest | Churn Prediction |
| EOQ | Inventory Planning |
| ABC Analysis | Product Categorization |

---

# 📷 Dashboard Preview

Overview Dashboard

Forecasting Dashboard

Customer Segmentation

Churn Dashboard

Inventory Optimization

Monitoring Dashboard

---

# 🎯 Key Metrics

✔ Forecast Accuracy

✔ Churn AUC

✔ Stockout Reduction

✔ Inventory Savings

✔ Customer Segmentation

✔ Demand Prediction

---

# Future Improvements

- Docker Deployment
- CI/CD Pipeline
- Authentication
- Kafka Streaming
- Redis Cache
- Grafana Monitoring
- Kubernetes Deployment

---

# Author

**NIPURN**

B-Tech CSE | AI Engineer | Data Science Enthusiast

GitHub:
https://github.com/NipurnCoder

---

⭐ If you found this project useful, consider giving it a star.
