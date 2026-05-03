# Group Project - Banking Transactions Lakehouse

This group project contains the exported Databricks notebooks from the Banking Transactions Lakehouse project in Shared:

```text
/Shared/Banking-Transactions-Lakehouse-Project-Selected-Dataset-Edition
```

In this project, we built a Banking Transactions Lakehouse using Databricks, PySpark, Delta Lake, and a Bronze/Silver/Gold architecture. The pipeline loads raw banking transactions, cleans and validates the data, creates supporting banking entities, and publishes Gold analytics tables for reporting.

## Project Structure

| Folder | Purpose |
| --- | --- |
| `notebooks/bronze` | Bronze notebook for loading raw banking transaction CSV data |
| `notebooks/silver` | Silver notebooks for transaction cleaning and banking entity creation |
| `notebooks/gold` | Gold notebook for KPI, report, ranking, and aggregation outputs |
| `bronze` | Exported Bronze Python file from the Databricks project |
| `silver` | Exported Silver Python placeholder/file from the Databricks project |
| `documentation` | Detailed project documentation |
| `screenshots` | Place for Databricks run screenshots and result screenshots |

## Exported Databricks Notebooks

| Notebook | Work Completed |
| --- | --- |
| `notebooks/bronze/bronze_load.py` | Loaded `bank.csv`, cleaned column names, counted records, and saved raw data to Bronze Delta |
| `notebooks/silver/silver_transform.py` | Cleaned transactions, converted amount/date fields, created transaction type, validated quality, and saved Silver transactions |
| `notebooks/silver/accounts.py` | Created account records with latest balance, account type, and branch assignment |
| `notebooks/silver/customers.py` | Created customer records from accounts and assigned customer cities |
| `notebooks/silver/cards.py` | Generated card records and card types for each account |
| `notebooks/silver/branches.py` | Created the branch master table |
| `notebooks/gold/gold_transform.py` | Created Gold tables, KPIs, final report, customer behavior, rankings, running totals, and aggregations |
| `notebooks/mast.py` | Orchestrated Bronze, Silver, and Gold notebooks with `dbutils.notebook.run` |

## Pipeline Summary

1. Loaded raw banking transaction data from Databricks Volumes.
2. Saved raw transaction records into the Bronze Delta layer.
3. Cleaned and standardized transaction fields in the Silver layer.
4. Created `amount`, `transaction_type`, and parsed `transaction_date`.
5. Removed null amount records and duplicate records.
6. Built Silver entity tables for accounts, customers, cards, and branches.
7. Copied Silver tables into the Gold layer.
8. Built Gold KPI and reporting outputs.
9. Created final joins and analytical outputs for banking insights.

## Gold Outputs Built

- `kpi_business_metrics`
- `final_report`
- `agg_customer_behavior`
- `ranked_accounts`
- `running_total_transactions`
- `agg_amount_by_transaction_type`
- `agg_transactions_by_branch`
- `agg_customers_by_city`

## Documentation

Detailed documentation is available in [documentation/PROJECT_DOCUMENTATION.md](documentation/PROJECT_DOCUMENTATION.md).

## Screenshots

Screenshots from the Databricks project can be stored in `screenshots/`, including Bronze load output, Silver quality checks, Gold KPI tables, final report output, and aggregation results.
