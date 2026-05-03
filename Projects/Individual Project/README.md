# Individual Project - Consolidated Pipelines in Databricks

This project contains the exported Databricks notebooks from the **Consolidated Pipelines** workspace folder:

```text
/Shared/consolidated_pipeline
```

The project builds an FMCG-style consolidated pipeline using Databricks, PySpark, Delta Lake, Bronze/Silver/Gold schemas, dimension processing, fact processing, full loads, incremental loads, and merges into parent Gold tables.

## Project Structure

| Folder | Purpose |
| --- | --- |
| `notebooks/setup_folder` | Catalog/schema setup, common utilities, and date dimension creation |
| `notebooks/2_dimension_data_processing` | Dimension pipelines for customers, products, and pricing |
| `notebooks/3_fact_data_processing` | Full and incremental fact order processing |
| `documentation` | Detailed project documentation and implementation notes |
| `screenshots` | Screenshots from Databricks notebook runs and output tables |

## Exported Databricks Notebooks

| Notebook | Description |
| --- | --- |
| `setup_folder/utilities.py` | Defines common schema names: Bronze, Silver, and Gold |
| `setup_folder/setup_catalog.py` | Creates the `fmcg` catalog and `bronze`, `silver`, `gold` schemas |
| `setup_folder/dim_date_table_creation.py` | Creates the date dimension table |
| `2_dimension_data_processing/customer_data_processing.py` | Loads, cleans, standardizes, and merges customer dimension data |
| `2_dimension_data_processing/2_products_data_processing.py` | Loads, cleans, standardizes, and merges product dimension data |
| `2_dimension_data_processing/3_pricing_data_processing.py` | Processes pricing dimension data |
| `3_fact_data_processing/1_full_load_fact.py` | Performs full load order fact processing and parent table merge |
| `3_fact_data_processing/2_incremental_load_fact.py` | Performs incremental order fact processing using landing and processed paths |

## Pipeline Summary

1. Create the `fmcg` catalog and required schemas.
2. Load source CSV files from cloud storage.
3. Write raw records into Bronze Delta tables with file metadata.
4. Clean and standardize data in Silver tables.
5. Build child Gold dimension and fact tables.
6. Merge child project outputs into parent company Gold tables.
7. Support incremental order processing by reading new landing files and moving processed files.

## Main Technologies

- Databricks
- PySpark
- Spark SQL
- Delta Lake
- Delta merge/upsert
- Change Data Feed enabled Delta tables
- Bronze, Silver, and Gold architecture

## Documentation

Detailed documentation is available in [documentation/PROJECT_DOCUMENTATION.md](documentation/PROJECT_DOCUMENTATION.md).

## Screenshots

Add Databricks screenshots to the `screenshots/` folder, such as:

- Catalog and schema creation
- Bronze, Silver, and Gold tables
- Dimension notebook outputs
- Full load fact outputs
- Incremental load fact outputs
- Parent Gold table merge results
