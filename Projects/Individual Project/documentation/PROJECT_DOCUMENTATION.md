# Individual Project Documentation - Consolidated Pipelines in Databricks

## Project Objective

The objective of this individual project is to build a consolidated Databricks data pipeline for FMCG-style data. The pipeline processes customer, product, pricing, and order data through Bronze, Silver, and Gold layers, then merges the cleaned child project output into parent company Gold tables.

## Databricks Source

The notebooks were exported from the Databricks workspace folder:

```text
/Shared/consolidated_pipeline
```

GitHub stores the exported notebooks as Python source files under the `notebooks/` folder.

## Tools and Technologies

- Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- DeltaTable merge
- Change Data Feed
- Cloud object storage source paths
- GitHub

## Architecture

```text
Source CSV Files
   |
   v
Bronze Delta Tables
   |
   v
Silver Cleaned Tables
   |
   v
Child Gold Dimension and Fact Tables
   |
   v
Parent Company Gold Tables
```

## Catalog and Schema Setup

The setup notebook creates the Databricks catalog and schemas:

```sql
CREATE CATALOG IF NOT EXISTS fmcg;
CREATE SCHEMA IF NOT EXISTS fmcg.gold;
CREATE SCHEMA IF NOT EXISTS fmcg.silver;
CREATE SCHEMA IF NOT EXISTS fmcg.bronze;
```

The utility notebook defines shared schema names:

```python
bronze_schema = "bronze"
silver_schema = "silver"
gold_schema = "gold"
```

## Dimension Processing

### Customer Dimension

Notebook:

```text
notebooks/2_dimension_data_processing/customer_data_processing.py
```

Main steps:

- Read customer CSV files from the source path.
- Add read timestamp, source file name, and file size metadata.
- Write raw customer data to the Bronze table.
- Remove duplicate customer records.
- Trim customer names.
- Standardize city values and fix known city spelling issues.
- Apply business-confirmed city corrections.
- Convert `customer_id` to string.
- Build a final `customer` field using customer name and city.
- Add static attributes such as market, platform, and channel.
- Write cleaned records to Silver.
- Create child Gold table `sb_dim_customers`.
- Merge child customer data into the parent `dim_customers` table.

### Product Dimension

Notebook:

```text
notebooks/2_dimension_data_processing/2_products_data_processing.py
```

Main steps:

- Read product CSV files from the source path.
- Write raw product data to Bronze.
- Drop duplicate product records.
- Standardize product category casing.
- Fix spelling issues such as `Protien` to `Protein`.
- Derive `division` from product category.
- Extract product variant from product name.
- Generate deterministic `product_code` using SHA-256.
- Clean invalid product IDs using fallback value `999999`.
- Write product data to Silver.
- Create child Gold table `sb_dim_products`.
- Merge product data into parent `dim_products`.

### Pricing Dimension

Notebook:

```text
notebooks/2_dimension_data_processing/3_pricing_data_processing.py
```

Main purpose:

- Process pricing data through Bronze, Silver, and Gold layers.
- Standardize pricing information for downstream fact processing.
- Support parent table consolidation.

## Fact Processing

### Full Load Orders

Notebook:

```text
notebooks/3_fact_data_processing/1_full_load_fact.py
```

Main steps:

- Read order CSV files from the landing path.
- Append raw order data into the Bronze orders table.
- Move processed files from landing to processed storage.
- Filter records where `order_qty` is present.
- Clean invalid `customer_id` values using fallback value `999999`.
- Parse `order_placement_date` from multiple date formats.
- Drop duplicate order records.
- Cast `product_id` to string.
- Join orders with the Silver product table to get `product_code`.
- Write or merge cleaned order records into Silver.
- Build child Gold fact table `sb_fact_orders`.
- Aggregate daily child data to monthly grain.
- Merge monthly results into parent `fact_orders`.

### Incremental Load Orders

Notebook:

```text
notebooks/3_fact_data_processing/2_incremental_load_fact.py
```

Main steps:

- Check whether new CSV files exist in the landing directory.
- Exit safely if no new files are present.
- Read only newly arrived files.
- Append raw records to the Bronze table.
- Write staging Bronze data for the current batch.
- Move processed files to the processed directory.
- Clean and deduplicate current batch records.
- Merge batch records into the Silver orders table.
- Write staging Silver data for incremental Gold processing.
- Deduplicate before Delta merge to avoid multiple source row matches.
- Merge current batch into child Gold table `sb_fact_orders`.
- Recalculate only affected monthly partitions.
- Merge recalculated monthly data into parent `fact_orders`.
- Drop staging tables after processing.

## Data Quality and Standardization Rules

- Drop duplicate customers and products.
- Trim customer names.
- Standardize customer city spellings.
- Apply business-confirmed customer city fixes.
- Standardize product category casing.
- Correct spelling mistakes in product names and categories.
- Replace invalid customer IDs with fallback value `999999`.
- Replace invalid product IDs with fallback value `999999`.
- Parse order dates from multiple possible formats.
- Drop duplicate fact records before Delta merge.

## Tables Created or Updated

| Layer | Example Tables |
| --- | --- |
| Bronze | `fmcg.bronze.customers`, `fmcg.bronze.products`, `fmcg.bronze.orders` |
| Silver | `fmcg.silver.customers`, `fmcg.silver.products`, `fmcg.silver.orders` |
| Child Gold | `fmcg.gold.sb_dim_customers`, `fmcg.gold.sb_dim_products`, `fmcg.gold.sb_fact_orders` |
| Parent Gold | `fmcg.gold.dim_customers`, `fmcg.gold.dim_products`, `fmcg.gold.fact_orders` |

## Recommended Run Order

1. `setup_folder/setup_catalog.py`
2. `setup_folder/utilities.py`
3. `setup_folder/dim_date_table_creation.py`
4. `2_dimension_data_processing/customer_data_processing.py`
5. `2_dimension_data_processing/2_products_data_processing.py`
6. `2_dimension_data_processing/3_pricing_data_processing.py`
7. `3_fact_data_processing/1_full_load_fact.py`
8. `3_fact_data_processing/2_incremental_load_fact.py`

## Screenshots to Add

Add project screenshots into the `screenshots/` folder:

- Databricks folder view for `/Shared/consolidated_pipeline`
- Successful catalog/schema creation
- Bronze customer/product/order tables
- Silver cleaned tables
- Child Gold dimension and fact tables
- Parent Gold merge results
- Incremental load run result

## Security Notes

- Do not commit Databricks access tokens.
- Do not store secrets in notebooks.
- Keep source storage credentials in Databricks secrets or secure workspace configuration.
- Revoke exposed tokens and generate new ones when needed.
