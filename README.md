🛍️ E-Commerce Data Analytics + AI Pipeline

This project automates the full workflow of an online store dataset using Python, SQL, ML, and data visualization.

It automatically:

✔ Generates realistic synthetic data (customers, products, orders, items)
✔ Loads it into a structured SQLite database
✔ Runs SQL-based analytics queries and exports reports
✔ Builds machine learning models (Recommendations + CLV scoring)
✔ Produces visual business dashboards (charts)

This project demonstrates skills in:
Data Engineering → ETL → SQL Analytics → Machine Learning → Data Visualization


⭐Key Features

✔ Synthetic data generator (customers, products, orders, order_items)
✔ Automated SQLite ingestion with indexing
✔ SQL analytics (joins, aggregations, trends)
✔ Customer Lifetime Value (CLV) scoring
✔ ML Recommendation Engine using Cosine Similarity
✔ Dashboard with revenue, sales & customer insights (Matplotlib)


 
 
 How to Run (Step-by-Step)


1. Install dependencies
   ```
   pip install faker pandas scikit-learn matplotlib
   ```
   Expected: `Successfully installed ...`

2. Generate synthetic data
   ```
   python generate_data.py
   ```
   Expected: CSV files appear under `data/` (customers/products/orders/order_items).

3. Ingest data into SQLite
   ```
   python ingest_sqlite.py
   ```
   Expected: `data/ecommerce.db` recreated and message showing tables loaded.

4. Run SQL analytics
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


