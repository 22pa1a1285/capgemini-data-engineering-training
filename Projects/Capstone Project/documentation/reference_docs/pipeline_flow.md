# Pipeline Flow

## Overview

The FMCG capstone follows a medallion architecture with Bronze, Silver, and Gold layers.

```text
CSV files in Databricks Volumes
   |
   v
Bronze DLT tables
   |
   v
Silver cleaned and enriched sales table
   |
   v
Gold KPI and dashboard tables
```

## Bronze Flow

1. Read CSV files from `/Volumes/fmcg/bronze`.
2. Apply strict schemas for customers, orders, order items, payments, products, and sellers.
3. Add metadata fields such as ingest timestamp, source file, source system, and batch ID.
4. Publish raw Bronze tables.

## Silver Flow

1. Join orders, items, payments, customer, product, seller, and region data.
2. Standardize column names.
3. Add derived fields such as quantity, net amount, and sales value.
4. Filter invalid records.
5. Create quarantine tables for bad records.
6. Publish the cleaned `silver_sales` table.

## Gold Flow

1. Aggregate Silver data by date, region, channel, SKU, and distributor.
2. Calculate sales, order, stock, and performance metrics.
3. Publish final tables for dashboards and analysis.
