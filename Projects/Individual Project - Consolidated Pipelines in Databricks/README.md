# Individual Project - Consolidated Pipelines in Databricks

This individual project focuses on building consolidated data pipelines in Databricks. The project should demonstrate how raw data is ingested, cleaned, transformed, and prepared for analytics using Spark, PySpark, SQL, and Delta Lake.

## Folder Structure

| Folder | Purpose |
| --- | --- |
| `notebooks` | Databricks notebooks used for ingestion, transformation, validation, and final outputs |
| `documentation` | Project explanation, architecture, workflow, and implementation details |
| `screenshots` | Screenshots of notebooks, pipeline runs, tables, outputs, and dashboards |

## Expected Notebook Organization

Recommended notebooks:

- `01_ingestion.ipynb`
- `02_cleaning_and_validation.ipynb`
- `03_transformation.ipynb`
- `04_consolidated_pipeline.ipynb`
- `05_reporting_outputs.ipynb`

## Project Workflow

1. Load raw source data into Databricks.
2. Create Bronze tables for raw or lightly processed data.
3. Clean and validate records in the Silver layer.
4. Apply business transformations and aggregations.
5. Store final curated outputs in Gold tables.
6. Capture important outputs and pipeline execution screenshots.

## Documentation

Detailed project documentation is available in [documentation/PROJECT_DOCUMENTATION.md](documentation/PROJECT_DOCUMENTATION.md).
