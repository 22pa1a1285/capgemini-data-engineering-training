# Group Project Documentation - Banking Transactions Lakehouse

## Project Objective

The objective of this group project was to build a Banking Transactions Lakehouse in Databricks. We implemented a Bronze/Silver/Gold data pipeline that loads raw banking transactions, cleans and validates them, creates related banking entity tables, and publishes business-ready Gold analytics outputs.

## Databricks Source

The project was exported from:

```text
/Shared/Banking-Transactions-Lakehouse-Project-Selected-Dataset-Edition
```

The exported notebooks are stored as Python source files under the `notebooks/` folder.

## Tools and Technologies Used

- Databricks
- Apache Spark
- PySpark
- Delta Lake
- Spark SQL functions
- Window functions
- Databricks Volumes
- `dbutils.notebook.run` orchestration
- GitHub

## Architecture

```text
Raw bank.csv file
   |
   v
Bronze Delta - Raw transaction records
   |
   v
Silver Delta - Clean transactions and banking entities
   |
   v
Gold Delta - KPIs, reports, rankings, and aggregations
```

## Source Path

The Bronze notebook reads the source CSV from:

```text
/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/bronze/bank.csv
```

Delta outputs are written under:

```text
/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta
```

## Bronze Layer Work

Notebook:

```text
notebooks/bronze/bronze_load.py
```

Work completed:

- Loaded raw banking transaction CSV data.
- Inferred the source schema.
- Displayed sample rows and schema for validation.
- Cleaned column names by removing spaces and special characters.
- Counted total raw records.
- Saved the raw data as a Bronze Delta table at:

```text
delta/bronze/transactions
```

## Silver Layer Work

### Transaction Cleaning

Notebook:

```text
notebooks/silver/silver_transform.py
```

Work completed:

- Read Bronze transaction data.
- Dropped unnecessary columns such as cheque number and invalid placeholder columns.
- Renamed columns into clean names:
  `account_id`, `transaction_date`, `transaction_details`, `value_date`, `withdrawal_amount`, `deposit_amount`, and `balance`.
- Converted withdrawal, deposit, and balance fields to numeric values.
- Created a unified `amount` column.
- Created `transaction_type` as `credit` or `debit`.
- Parsed transaction dates into proper date format.
- Removed records with null amounts.
- Removed duplicate records.
- Ran data quality checks for:
  - Negative balances
  - Negative amounts
  - Future dates
  - Missing transaction dates
  - Missing account IDs
- Saved cleaned transaction records to:

```text
delta/silver/transactions
```

### Accounts

Notebook:

```text
notebooks/silver/accounts.py
```

Work completed:

- Read Silver transaction data.
- Used a window function to identify the latest transaction per account.
- Created an account table with latest balance.
- Assigned account type as `Savings`.
- Assigned accounts to branches using a hash-based branch mapping.
- Removed duplicate account records.
- Saved account data to:

```text
delta/silver/accounts
```

### Customers

Notebook:

```text
notebooks/silver/customers.py
```

Work completed:

- Created customer records from account records.
- Generated `customer_id` from `account_id`.
- Generated customer names.
- Assigned cities across Hyderabad, Mumbai, Delhi, Chennai, and Bangalore using account hash logic.
- Removed duplicate customers.
- Saved customer data to:

```text
delta/silver/customers
```

### Cards

Notebook:

```text
notebooks/silver/cards.py
```

Work completed:

- Generated card records from account records.
- Created `card_id` using account ID.
- Assigned card type as Debit or Credit.
- Removed duplicate card records.
- Saved card data to:

```text
delta/silver/cards
```

### Branches

Notebook:

```text
notebooks/silver/branches.py
```

Work completed:

- Created a branch master table with explicit schema.
- Added four branches:
  `B1`, `B2`, `B3`, and `B4`.
- Stored branch names and cities.
- Removed duplicate branch records.
- Saved branch data to:

```text
delta/silver/branches
```

## Gold Layer Work

Notebook:

```text
notebooks/gold/gold_transform.py
```

Work completed:

- Copied Silver tables into Gold tables:
  - `transactions`
  - `accounts`
  - `branches`
  - `cards`
  - `customers`
- Built a KPI table with business metrics.
- Created a final report by joining transactions, accounts, customers, branches, and cards.
- Created customer behavior analytics.
- Ranked accounts by latest balance.
- Calculated running transaction totals per account.
- Built group-by aggregations for transaction type, branch activity, and city-level customer metrics.

## Gold Tables Created

| Gold Table | Purpose |
| --- | --- |
| `kpi_business_metrics` | Stores overall banking KPIs |
| `final_report` | Joined reporting table across transactions, accounts, customers, branches, and cards |
| `agg_customer_behavior` | Customer-level transaction behavior and segmentation |
| `ranked_accounts` | Account ranking by latest balance |
| `running_total_transactions` | Running transaction total per account |
| `agg_amount_by_transaction_type` | Credit/debit transaction summary |
| `agg_transactions_by_branch` | Branch-level transaction summary |
| `agg_customers_by_city` | City-level customer and balance summary |

## KPIs Created

- Total transactions
- Total transaction amount
- Average transaction amount
- Total accounts
- Active accounts
- Total customers
- Total branches
- Total cards
- Active cards
- Average accounts per customer
- Average cards per customer

## Orchestration

Notebook:

```text
notebooks/mast.py
```

The master notebook runs the pipeline in sequence:

1. Bronze load
2. Silver transform
3. Gold transform

It uses `dbutils.notebook.run` to trigger the notebooks and prints completion status.

## Data Quality Checks Completed

- Null amount filtering
- Duplicate removal
- Numeric amount conversion
- Date parsing
- Negative amount checks
- Negative balance checks
- Future date checks
- Missing account ID checks
- Missing transaction date checks

## Screenshots to Add

Project screenshots should be stored in `screenshots/`:

- Bronze raw data load
- Cleaned Silver transaction schema
- Data quality check output
- Account/customer/card/branch Silver tables
- Gold KPI table
- Final report table
- Customer behavior aggregation
- Ranked accounts output
- Running total output
- Branch and city aggregations

## Security Notes

- Databricks access tokens are not stored in this repository.
- Source data and credentials should stay in Databricks Volumes, secrets, or secure workspace configuration.
- Screenshots should not expose tokens or private credentials.
