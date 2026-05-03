# Sprint Project - FMCG DLT Lakehouse

This sprint project contains the FMCG Databricks Lakehouse pipeline from `FMCG_PROJECT.zip`.

The project builds an FMCG analytics pipeline using Databricks, Delta Live Tables, PySpark, Delta Lake, and a Bronze/Silver/Gold architecture. It ingests customer, order, order item, payment, product, and seller datasets, validates and enriches sales records, quarantines invalid records, and publishes Gold tables for dashboard-ready business reporting.

## Project Structure

| Folder | Purpose |
| --- | --- |
| `notebooks/transformations/bronze` | Bronze DLT ingestion code and reusable metadata utilities |
| `notebooks/transformations/silver` | Silver cleaning, validation, quarantine, enrichment, and sales fact processing |
| `notebooks/transformations/gold` | Gold KPI and reporting tables for FMCG analytics |
| `documentation` | Project documentation and reference notes |
| `screenshots/dashboards` | Dashboard screenshots for pipeline health and business KPIs |
| `screenshots/diagrams` | Architecture, ER, and pipeline flow diagrams |
| `outputs` | Exported sample output CSV files |
| `presentation` | Final project presentation deck |

## Project Files

| File | Work Completed |
| --- | --- |
| `notebooks/transformations/bronze/common_utils.py` | Adds standard ingestion metadata columns to raw records |
| `notebooks/transformations/bronze/bronze_dlt.py` | Loads raw FMCG CSV files into Bronze DLT tables with strict schemas |
| `notebooks/transformations/silver/silver_dlt.py` | Builds region lookup, quarantine tables, monitoring table, and enriched Silver sales records |
| `notebooks/transformations/gold/gold_dlt.py` | Creates Gold sales summary, SKU performance, distributor performance, inventory snapshot, and stock aging tables |

## Pipeline Summary

1. Load raw FMCG source files from Databricks Volumes into Bronze DLT tables.
2. Add ingestion metadata including source file, source system, batch ID, and ingest timestamp.
3. Join orders, order items, payments, customers, products, sellers, and regions.
4. Standardize payment type and field names.
5. Quarantine records with invalid price, missing date, or future invoice date.
6. Deduplicate valid sales records by order and product.
7. Derive quantity, net amount, sales value, channel, and region.
8. Publish Gold tables for sales, SKU, distributor, inventory, and stock aging analytics.

## Gold Outputs Built

- `sales_summary`
- `sku_performance`
- `distributor_performance`
- `inventory_snapshot`
- `stock_aging`

## Databricks Workspace

Workspace URL:

```text
https://dbc-20852bd9-db66.cloud.databricks.com
```

Store the Databricks access token outside the repository, for example in a local `.env` file based on the repo root `.env.example`.

## Documentation

Detailed documentation is available in [documentation/PROJECT_DOCUMENTATION.md](documentation/PROJECT_DOCUMENTATION.md).

