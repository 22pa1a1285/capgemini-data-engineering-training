# Group Project Documentation - Banking in Databricks

## Project Objective

The objective of this project is to build a Databricks-based banking data pipeline that prepares clean, reliable, and analysis-ready banking data. The project can include customer, account, transaction, branch, and product-related datasets.

## Tools and Technologies

- Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- GitHub

## Business Focus

The banking project should support analysis such as:

- Customer profile analysis
- Account balance summaries
- Transaction volume and value analysis
- Branch-level performance
- Suspicious or invalid transaction detection
- Data quality reporting

## Proposed Architecture

```text
Banking Source Data
   |
   v
Bronze Layer - Raw Banking Data
   |
   v
Silver Layer - Clean Customer, Account, and Transaction Data
   |
   v
Gold Layer - Banking KPIs and Analytical Tables
```

## Implementation Steps

1. Load customer, account, and transaction datasets.
2. Store source data in Delta format.
3. Standardize column names and data types.
4. Handle null values and duplicate records.
5. Validate transaction amounts, account IDs, and customer IDs.
6. Create business-level tables for analytics.
7. Run data quality checks.
8. Capture screenshots of final outputs.

## Notebooks

Place all Databricks notebooks for this project in the `notebooks/` folder.

Recommended notebook sequence:

- Data ingestion
- Data cleaning
- Transaction processing
- Data quality checks
- Final banking analytics

## Screenshots

Place project screenshots in the `screenshots/` folder. Recommended screenshots include:

- Notebook execution
- Data quality results
- Cleaned Delta tables
- Banking KPI outputs
- Dashboard views, if available

## Final Deliverables

- Databricks notebooks
- Project README
- Project documentation
- Output screenshots
- Banking analytics tables or reports
