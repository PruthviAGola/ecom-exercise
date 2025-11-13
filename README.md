# 🛍️ E-Commerce Data Analytics + AI

## 🔎 Overview
Compact toolkit that simulates an online store, loads everything into SQLite, and layers on analytics plus AI. Perfect for beginners who want to practice data generation, SQL analysis, machine learning recommendations, and dashboard visualization in one place.

## ✨ Key Features
- Synthetic data generator for customers, products, orders, and order_items.
- Automated SQLite ingestion with indexes for fast queries.
- Ready-to-run SQL analytics scripts for business insights.
- Customer Lifetime Value (CLV) scoring with pandas.
- Product recommendation engine using cosine similarity.
- Matplotlib dashboard with revenue and sales charts.

## 🧰 Tech Stack
| Layer | Tools |
| --- | --- |
| Language | Python 3.10 |
| Data Generation | Faker, pandas |
| Database | SQLite |
| Machine Learning | pandas, scikit-learn cosine similarity |
| Visualization | Matplotlib |
| Version Control | Git & GitHub |

## 🗂 Project Folder Structure
```
cursor-ecom-exercise/
├── data/                # CSV exports + ecommerce.db
├── charts/              # Generated PNG charts
├── generate_data.py
├── ingest_sqlite.py
├── run_query.py
├── recommendation_engine.py
├── clv_analysis.py
├── dashboard.py
└── README.md
```

## 🛠️ How to Run (Step-by-Step)
> Run these commands from the project root. Messages listed are the expected confirmations.

1. **Install dependencies**
   ```
   pip install faker pandas scikit-learn matplotlib
   ```
   Expected: `Successfully installed ...`

2. **Generate synthetic data**
   ```
   python generate_data.py
   ```
   Expected: CSV files appear under `data/` (customers/products/orders/order_items).

3. **Ingest data into SQLite**
   ```
   python ingest_sqlite.py
   ```
   Expected: `data/ecommerce.db` recreated and message showing tables loaded.

4. **Run SQL analytics**
   ```
   python run_query.py
   ```
   Expected: Console prints each query section with row counts.

5. **Run ML recommendation engine**
   ```
   python recommendation_engine.py
   ```
   Expected: `Top recommendations saved to data/recommendations.csv` plus example recommendations for 3 products.

6. **Run CLV analysis**
   ```
   python clv_analysis.py
   ```
   Expected: `Top 10 Customers by Customer Lifetime Value (CLV)` displayed and `data/clv_report.csv` saved.

7. **Generate dashboard charts**
   ```
   python dashboard.py
   ```
   Expected: `Charts saved to /charts` and four PNGs written to the `charts/` folder.

## 📁 Output Files
- `data/customers.csv`, `data/products.csv`, `data/orders.csv`, `data/order_items.csv`
- `data/ecommerce.db`
- `data/recommendations.csv`
- `data/clv_report.csv`
- `charts/monthly_revenue.png`
- `charts/category_revenue.png`
- `charts/top_customers.png`
- `charts/best_selling_products.png`

## 🚀 Future Improvements
- Fraud detection module
- FastAPI web API
- Streamlit UI for self-serve dashboards

## 👤 Author
Pruthvi A Gola

## 📄 License
Released under the MIT License.
