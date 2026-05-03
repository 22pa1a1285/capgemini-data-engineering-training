# capstone Project - Healthcare Operations Lakehouse

This capstone project contains the Healthcare Operations Databricks pipeline from `healthcare-ops-capstone.zip`.

In this project, we built a healthcare operations lakehouse using Databricks, PySpark, Delta Lake, Auto Loader fallback ingestion, and a Bronze/Silver/Gold architecture. The pipeline ingests raw healthcare datasets, cleans and enriches appointments, supports full and incremental appointment loading, builds Gold KPI tables, and runs validation checks.

## Project Structure

| Folder | Purpose |
| --- | --- |
| `notebooks/bronze` | Bronze ingestion notebook for raw healthcare CSV files |
| `notebooks/silver` | Silver cleaning, enrichment, and appointment full/incremental load notebooks |
| `notebooks/gold` | Gold KPI notebook for dashboard-ready healthcare metrics |
| `notebooks/validation` | Validation notebook for source counts and quality checks |
| `documentation` | Detailed project documentation |
| `screenshots` | Place for Databricks run screenshots and output screenshots |

## Project Files

| File | Work Completed |
| --- | --- |
| `notebooks/bronze/01_bronze_ingestion.py` | Created Bronze Delta tables from healthcare raw CSV files using Auto Loader with batch fallback |
| `notebooks/silver/02_silver_transformations.py` | Cleaned doctors, departments, patients, billing, appointments, and Kaggle no-show data into Silver tables |
| `notebooks/silver/05_appointments_full_incremental_load.py` | Built full and incremental appointment load logic using watermark and primary-key upsert behavior |
| `notebooks/gold/03_gold_kpis.py` | Built Gold KPI tables for no-show rate, doctor utilization, revenue, wait time, revisits, diagnostics, feedback, and Kaggle no-show analysis |
| `notebooks/validation/04_validation_checks.py` | Added source-to-Bronze count checks, Silver data quality checks, and load audit review |

## Pipeline Summary

1. Created `health_cat` catalog schemas for Bronze, Silver, and Gold layers.
2. Loaded raw healthcare datasets from cloud storage into Bronze Delta tables.
3. Added load metadata such as load time, batch ID, source system, load date, and source file.
4. Cleaned and standardized healthcare dimensions and facts in Silver.
5. Enriched appointments with doctors, departments, billing, and patient data.
6. Created invalid appointment and data quality summary tables.
7. Processed Kaggle no-show appointments data for external no-show analysis.
8. Built full and incremental load handling for appointments.
9. Created Gold KPI tables for dashboard and analytics use.
10. Ran validation checks for counts, mandatory fields, valid dates, and bill amounts.

## Gold Outputs Built

- `gold_no_show_rate`
- `gold_doctor_utilization`
- `gold_department_revenue`
- `gold_wait_time_trends`
- `gold_patient_revisit_rate`
- `gold_diagnostics_volume`
- `gold_feedback_summary`
- `gold_kaggle_no_show_by_age`

## Documentation

Detailed documentation is available in [documentation/PROJECT_DOCUMENTATION.md](documentation/PROJECT_DOCUMENTATION.md).

## Screenshots

Healthcare capstone screenshots can be stored in `screenshots/`, including Bronze ingestion results, Silver enriched appointments, Gold KPI tables, validation check outputs, and appointment load audit results.
