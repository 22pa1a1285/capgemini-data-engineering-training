# Capstone Notebooks and Pipeline Code

This folder contains the Databricks pipeline code from the FMCG capstone project.

## Folders

| Folder | Purpose |
| --- | --- |
| `dlt_pipeline/bronze` | Bronze Delta Live Tables source ingestion and metadata code |
| `dlt_pipeline/silver` | Silver cleaning, validation, enrichment, and quarantine logic |
| `dlt_pipeline/gold` | Gold business aggregation tables |
| `streaming` | Streaming Silver and Gold pipeline files |

## How to Use in Databricks

1. Import or clone this repository into Databricks Repos.
2. Open the Python files in this folder.
3. Configure a DLT pipeline that includes the Bronze, Silver, and Gold files.
4. Set the source data path to `/Volumes/fmcg/bronze` or update the base path in `bronze_dlt.py`.
5. Run the DLT pipeline and validate output tables.
