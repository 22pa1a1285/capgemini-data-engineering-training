# Capstone Project Documentation

## Project Objective

The objective of the capstone project is to demonstrate an end-to-end data engineering solution in Databricks. The project should bring together data ingestion, transformation, quality checks, Delta Lake storage, medallion architecture, and final analytical outputs.

## Tools and Technologies

- Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- GitHub

## Proposed Architecture

```text
Source Systems
   |
   v
Bronze Layer - Raw Data Capture
   |
   v
Silver Layer - Cleansed and Standardized Data
   |
   v
Gold Layer - Business Metrics and Final Outputs
   |
   v
Reports, Dashboards, or Analysis
```

## Implementation Steps

1. Identify source datasets and business requirements.
2. Load source data into Databricks.
3. Store raw data in the Bronze layer.
4. Clean, standardize, and validate data in the Silver layer.
5. Create Gold layer outputs for reporting and analytics.
6. Add data quality checks for nulls, duplicates, invalid values, and schema consistency.
7. Capture screenshots of important outputs.
8. Document assumptions, workflow, and final results.

## Notebooks

Place all Databricks notebooks for this project in the `notebooks/` folder.

Recommended notebook sequence:

- Source ingestion
- Bronze layer creation
- Silver layer cleaning
- Gold layer transformation
- Data quality checks
- Final outputs

## Screenshots

Place project screenshots in the `screenshots/` folder. Recommended screenshots include:

- Databricks folder/project view
- Notebook execution results
- Bronze, Silver, and Gold tables
- Data quality check outputs
- Final reporting outputs or dashboards

## Final Deliverables

- Databricks notebooks
- Project README
- Project documentation
- Output screenshots
- Final curated tables or analytics outputs
