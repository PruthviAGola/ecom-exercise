
 🛍️ E-Commerce Analytics Sandbox

This project simulates a compact end-to-end ecommerce analytics system. It can:

* Fabricate realistic datasets for customers, products, orders, and order items.
* Build an SQLite analytics warehouse with a structured schema.
* Run repeatable, multi-table SQL analysis for business insights.
* Apply machine learning models for Customer Lifetime Value (CLV) and product recommendations.
* Generate visualization dashboards for revenue and sales trends.

Use it to demo ETL workflows, practice SQL joins, experiment with machine learning logic, or test BI pipelines without accessing real production data.

---

⭐ Key Features

* Synthetic data generation — `generate_data.py` outputs linked CSV files representing realistic ecommerce behavior (customers, products, orders, and order items) using Faker.
* One-step ingestion into SQLite — `ingest_sqlite.py` creates `ecommerce.db`, defines the schema, loads the generated CSVs, and applies indexing for fast analytical queries.
* Analytics queries — `run_query.py` performs multi-table joins to produce business insights such as best-selling products and top customers.
* Machine learning modules — Includes a recommendation engine using cosine similarity and CLV scoring for identifying high-value users.
* Visualization dashboard— `dashboard.py` generates PNG charts including top customers, category revenue, and monthly sales trends using Matplotlib.
* Portable and lightweight — No cloud services or external dependencies; everything runs locally on Python and SQLite.

---

📁 Repository Layout

```
ecom-exercise/
├── data/                      # Generated CSV files & SQLite database
├── charts/                    # Auto-generated dashboard visualizations
│
├── generate_data.py           # Synthetic data generator
├── ingest_sqlite.py           # SQLite schema + loader
├── run_query.py               # SQL reporting
├── recommendation_engine.py   # ML-based product recommendation system
├── clv_analysis.py            # Customer Lifetime Value analytics
├── dashboard.py               # Visualization builder
│
└── README.md
```

---

🧱 Data Model

| Table       | Purpose / Columns                                                              |
| ----------- | ------------------------------------------------------------------------------ |
| customers   | `customer_id, name, email` — customer identity and metadata                    |
| products    | `product_id, name, category, price` — catalog items                            |
| orders      | `order_id, customer_id, order_date, total_amount` — purchase records           |
| order_items | `item_id, order_id, product_id, quantity, price` — SKU-level details per order |

The generator enforces referential integrity: every `order_items.product_id` exists in `products`, and every `orders.customer_id` exists in `customers`.

---

▶️ Workflow

 1) Generate synthetic CSVs

```sh
python generate_data.py
```

2) Build the SQLite database and ingest data

```sh
python ingest_sqlite.py
```

3) Run analytics reporting

```sh
python run_query.py
```

4) Run ML models

```sh
python recommendation_engine.py
python clv_analysis.py
```

5) Generate visual dashboards

```sh
python dashboard.py
```

Each command is idempotent — you can regenerate or reload as often as needed.

---

 🧰 CLI Reference

| Script                     | Key Function     | Description                                          |
| -------------------------- | ---------------- | ---------------------------------------------------- |
| `generate_data.py`         | Data fabrication | Creates CSV datasets representing ecommerce behavior |
| `ingest_sqlite.py`         | ETL              | Creates and loads the SQLite warehouse               |
| `run_query.py`             | Reporting        | Runs analytical joins and outputs insights           |
| `recommendation_engine.py` | ML               | Computes product similarity and suggestions          |
| `clv_analysis.py`          | ML / BI          | Calculates Customer Lifetime Value rankings          |
| `dashboard.py`             | Visualization    | Generates business charts (PNG)                      |






