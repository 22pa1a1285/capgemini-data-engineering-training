# Capstone Project Documentation - FMCG Data Engineering Pipeline

## Project Objective

The objective of this capstone project is to build an end-to-end FMCG data engineering pipeline in Databricks. The project demonstrates source ingestion, schema enforcement, metadata capture, data cleansing, validation, quarantine handling, Silver enrichment, and Gold-level business outputs.

## Tools and Technologies

- Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- GitHub
- Delta Live Tables

## Source Data

The Bronze pipeline expects FMCG source files in Databricks volume paths under:

```text
/Volumes/fmcg/bronze
```

Expected source domains include:

- Customers
- Orders
- Order items
- Payments
- Products
- Sellers

## Architecture

```text
FMCG CSV Source Files
   |
   v
Bronze Layer - Raw tables with strict schemas and ingest metadata
   |
   v
Silver Layer - Cleaned, validated, enriched sales data and quarantine tables
   |
   v
Gold Layer - Sales, SKU, distributor, inventory, and stock-aging metrics
   |
   v
Dashboards, CSV outputs, and analytics
```

## Bronze Layer

Main files:

- `notebooks/dlt_pipeline/bronze/bronze_dlt.py`
- `notebooks/dlt_pipeline/bronze/common_utils.py`

Bronze responsibilities:

- Define strict schemas for source datasets
- Load CSV files from Databricks volumes
- Create raw DLT tables
- Add ingest timestamp, source file, source system, and batch ID metadata

## Silver Layer

Main files:

- `notebooks/dlt_pipeline/silver/silver_dlt.py`
- `notebooks/streaming/silver_sales_stream.py`

Silver responsibilities:

- Join orders, order items, payments, customers, products, sellers, and region lookup data
- Standardize column names and payment values
- Derive quantity, net amount, and sales value
- Filter invalid prices and invalid dates
- Remove duplicate order/product combinations
- Create quarantine tables for invalid records
- Enrich records with channel and region

## Gold Layer

Main files:

- `notebooks/dlt_pipeline/gold/gold_dlt.py`
- `notebooks/streaming/gold_dlt.py`

Gold outputs:

- `sales_summary`
- `sku_performance`
- `distributor_performance`
- `inventory_snapshot`
- `stock_aging`
- `payment_summary` in the streaming Gold file

Gold responsibilities:

- Create dashboard-ready sales summaries
- Rank SKU and distributor performance
- Estimate inventory and stock-aging views
- Produce business metrics for reporting

## Screenshots

Place final project screenshots in the `screenshots/` folder. Recommended screenshots include:

- Databricks folder/project view
- Notebook execution results
- Bronze, Silver, and Gold tables
- Data quality check outputs
- Final reporting outputs or dashboards

The zip included dashboard and diagram placeholder files. Replace placeholder images with real screenshots after running the pipeline in Databricks.

## Databricks Deployment Steps

1. Upload or clone this repository into Databricks Repos.
2. Open the Capstone Project folder.
3. Create or use a cluster that supports Delta Live Tables.
4. Upload source CSV files to `/Volumes/fmcg/bronze`.
5. Configure a DLT pipeline with the Bronze, Silver, and Gold Python files.
6. Run the pipeline and validate created tables.
7. Capture screenshots and place them in `screenshots/dashboards` or `screenshots/diagrams`.
8. Export final output files into `outputs/` if required.

## Final Deliverables

- Databricks notebooks
- Project README
- Project documentation
- Output screenshots
- Final curated tables or analytics outputs
