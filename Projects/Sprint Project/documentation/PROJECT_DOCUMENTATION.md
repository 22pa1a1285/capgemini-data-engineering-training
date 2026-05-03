# FMCG Sprint Project Documentation

## Overview

The FMCG Sprint Project implements a Databricks Lakehouse pipeline for sales analytics. The solution follows the Medallion architecture and separates work into Bronze ingestion, Silver transformation and validation, and Gold reporting layers.

## Source Data

The Bronze layer expects raw CSV datasets in Databricks Volumes under:

```text
/Volumes/fmcg/bronze
```

The pipeline includes strict schemas for:

- Customers
- Orders
- Order items
- Payments
- Products
- Sellers

## Bronze Layer

The Bronze DLT code reads raw CSV files with explicit schemas and writes them as DLT tables. Each table adds standard metadata through `common_utils.py`, including ingestion timestamp, source file, source system, and batch ID.

Bronze tables:

- `customers_raw`
- `orders_raw`
- `order_items_raw`
- `payments_raw`
- `products_raw`
- `sellers_raw`

## Silver Layer

The Silver layer creates cleaned and enriched sales records. It joins orders, order items, and payments, then enriches the result with customer, product, seller, and region information.

Silver processing includes:

- Column name standardization
- Payment type normalization
- Invalid record quarantine
- Quarantine monitoring
- Sales value derivation
- Duplicate removal
- Region enrichment
- Channel assignment

Silver tables:

- `region_lookup`
- `quarantine_sales`
- `quarantine_monitoring`
- `silver_sales`

## Gold Layer

The Gold layer creates analytics-ready DLT tables for dashboards and reporting.

Gold tables:

- `sales_summary`: daily sales by region and channel
- `sku_performance`: SKU revenue, quantity, revenue share, and rank
- `distributor_performance`: distributor sales, orders, quantity, approximate fill rate, and rank
- `inventory_snapshot`: estimated stock and stock flags by SKU and distributor
- `stock_aging`: estimated stock aging buckets by SKU and distributor

## Dashboards And Outputs

Dashboard screenshots are stored under:

```text
screenshots/dashboards
```

Included dashboard views:

- Pipeline health
- Sales trend
- SKU performance
- Distributor performance
- Stock aging

Sample output CSV files are stored under:

```text
outputs
```

## Diagrams

Architecture, ER, and pipeline flow diagrams are stored under:

```text
screenshots/diagrams
```

## Secret Handling

Do not commit Databricks access tokens. Use the repo root `.env.example` as a template and keep the real token in a local `.env` file or in Databricks secrets.

## Run Notes

1. Configure `DATABRICKS_HOST` and `DATABRICKS_TOKEN` locally.
2. Upload or verify raw CSV files under `/Volumes/fmcg/bronze`.
3. Import the DLT transformation files into Databricks.
4. Run Bronze, Silver, and Gold transformations in pipeline order.
5. Validate dashboards and compare exported outputs with the files in `outputs`.

