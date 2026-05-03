# Capstone Project - FMCG Data Engineering Pipeline

This capstone project contains the FMCG Databricks pipeline package provided in `FMCG_PROJECT.zip`. The project uses Delta Live Tables style Python code to build Bronze, Silver, and Gold layers for FMCG sales, product, distributor, retailer, payment, inventory, and dashboard-ready analytics.

## Folder Structure

| Folder | Purpose |
| --- | --- |
| `notebooks/dlt_pipeline` | Bronze, Silver, and Gold DLT pipeline Python files from the FMCG project |
| `notebooks/streaming` | Streaming Silver and Gold pipeline files from the FMCG project |
| `documentation` | Project explanation, architecture, workflow, and final deliverable notes |
| `documentation/reference_docs` | Reference documentation files included in the zip |
| `screenshots/dashboards` | Dashboard screenshot placeholders from the zip |
| `screenshots/diagrams` | Architecture and pipeline diagram placeholders from the zip |
| `outputs` | Output CSV placeholders from the zip |

## Expected Notebook Organization

Included pipeline files:

- `notebooks/dlt_pipeline/bronze/bronze_dlt.py`
- `notebooks/dlt_pipeline/bronze/common_utils.py`
- `notebooks/dlt_pipeline/silver/silver_dlt.py`
- `notebooks/dlt_pipeline/gold/gold_dlt.py`
- `notebooks/streaming/silver_sales_stream.py`
- `notebooks/streaming/gold_dlt.py`

## Project Workflow

1. Load FMCG source CSV files into the configured Databricks volume path.
2. Run Bronze DLT logic to enforce source schemas and add metadata.
3. Run Silver logic to join sales entities, standardize fields, validate records, and quarantine bad data.
4. Run Gold logic to create business-ready sales, SKU, distributor, inventory, and stock-aging outputs.
5. Use dashboard screenshots and output files to document final results.
6. Keep screenshots and diagrams inside the matching folders.

## Documentation

Detailed project documentation is available in [documentation/PROJECT_DOCUMENTATION.md](documentation/PROJECT_DOCUMENTATION.md).
