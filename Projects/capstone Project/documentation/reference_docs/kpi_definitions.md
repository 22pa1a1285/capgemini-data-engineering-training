# KPI Definitions

This document explains the main KPIs produced by the FMCG capstone Gold layer.

## Sales Summary

- `total_quantity`: Total units sold.
- `total_revenue`: Sum of sales value.
- `total_orders`: Number of unique invoices or orders.

## SKU Performance

- `total_quantity`: Quantity sold per SKU.
- `total_revenue`: Revenue generated per SKU.
- `revenue_share_percent`: SKU contribution to total revenue.
- `rank`: SKU ranking based on revenue.

## Distributor Performance

- `total_sales`: Distributor-level sales value.
- `order_count`: Number of unique orders handled by the distributor.
- `total_quantity`: Total quantity handled by the distributor.
- `approx_fill_rate`: Estimated fulfillment measure based on quantity and order count.

## Inventory Snapshot

- `estimated_stock`: Simulated stock measure based on available sales data.
- `stockout_flag`: Indicates zero estimated stock.
- `overstock_flag`: Indicates estimated stock above the configured threshold.

## Stock Aging

- `qty_at_risk`: Quantity associated with older stock.
- `avg_stock_age`: Average stock age in days.
- `stock_age_bucket`: Age band such as `<30`, `30-60`, `60-90`, or `90+`.
