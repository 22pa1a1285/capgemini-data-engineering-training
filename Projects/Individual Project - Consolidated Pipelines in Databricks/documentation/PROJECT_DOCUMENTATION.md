# Individual Project Documentation - Consolidated Pipelines in Databricks

## Project Objective

The objective of this project is to create a consolidated data engineering pipeline in Databricks that can ingest source data, clean and validate it, transform it into useful business outputs, and store the final results for reporting or analytics.

## Tools and Technologies

- Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- GitHub

## Proposed Architecture

```text
Source Data
   |
   v
Bronze Layer - Raw/Ingested Data
   |
   v
Silver Layer - Cleaned and Validated Data
   |
   v
Gold Layer - Aggregated and Business-Ready Data
```

## Implementation Steps

1. Ingest the raw dataset into Databricks.
2. Store raw data in Delta format.
3. Apply data cleaning rules such as null handling, duplicate removal, and data type correction.
4. Create transformation logic using PySpark and SQL.
5. Build consolidated output tables.
6. Validate row counts, schema, and business rules.
7. Save final outputs and screenshots.

## Notebooks

Place all Databricks notebooks for this project in the `notebooks/` folder.

Recommended notebook sequence:

- Ingestion notebook
- Cleaning and validation notebook
- Transformation notebook
- Final pipeline notebook
- Reporting/output notebook

## Screenshots

Place project screenshots in the `screenshots/` folder. Recommended screenshots include:

- Databricks notebook run
- Bronze, Silver, and Gold tables
- Pipeline execution result
- Query outputs
- Dashboard or final report outputs, if available

## Final Deliverables

- Databricks notebooks
- Project README
- Project documentation
- Output screenshots
- Final curated tables or query outputs
