# Capstone Project Documentation - Healthcare Operations Lakehouse

## Project Objective

The objective of this capstone project was to build an end-to-end healthcare operations lakehouse in Databricks. We implemented Bronze ingestion, Silver transformations, full and incremental appointment loading, Gold KPI generation, and validation checks for healthcare operational analytics.

## Tools and Technologies Used

- Databricks
- PySpark
- Spark SQL
- Delta Lake
- Auto Loader with batch fallback
- Databricks widgets
- Databricks Volumes / cloud storage paths
- Bronze, Silver, and Gold architecture
- Source-to-target validation

## Architecture

```text
Raw Healthcare CSV Files
   |
   v
Bronze Delta Tables
   |
   v
Silver Cleaned and Enriched Tables
   |
   v
Gold KPI Tables
   |
   v
Validation and Dashboard Outputs
```

## Catalog and Schemas

The notebooks use these default widget values:

| Setting | Default |
| --- | --- |
| Catalog | `health_cat` |
| Bronze schema | `bronze` |
| Silver schema | `silver` |
| Gold schema | `gold` |

The notebooks create the required schemas when they run.

## Bronze Layer Work

Notebook:

```text
notebooks/bronze/01_bronze_ingestion.py
```

Work completed:

- Created Bronze, Silver, and Gold schemas.
- Loaded healthcare raw CSV data from:

```text
s3://healthcare-ops-capstone-siddh-20260421235653/raw
```

- Used Auto Loader when available.
- Used batch CSV ingestion as a fallback when Auto Loader was unavailable.
- Added ingestion metadata:
  - `load_time`
  - `batch_id`
  - `source_system`
  - `load_date`
  - `source_file`
- Partitioned Bronze outputs by `load_date`.
- Optimized Bronze tables when supported.

Bronze datasets loaded:

- `departments`
- `doctors`
- `patients`
- `appointments`
- `billing`
- `diagnostics`
- `prescriptions`
- `feedback`
- `kaggle_noshow_appointments`

## Silver Layer Work

Notebook:

```text
notebooks/silver/02_silver_transformations.py
```

Work completed:

- Created cleaned dimension and fact tables.
- Standardized text fields using trim, whitespace normalization, and title casing.
- Cast IDs and financial fields to appropriate types.
- Converted date and timestamp fields.
- Created patient age from date of birth.
- Cleaned appointment statuses.
- Created `no_show_int` and `no_show_flag_clean`.
- Calculated wait time in minutes.
- Created data quality flags for:
  - Null patient ID
  - Null doctor ID
  - Invalid appointment timestamp
  - Unmatched doctor
  - Unmatched patient
- Joined appointments with doctors, departments, billing, and patients.
- Created `appointments_enriched`.
- Created invalid appointment and DQ summary tables.
- Cleaned Kaggle no-show appointment data and calculated lead days.

Silver outputs built:

- `doctors_clean`
- `departments_clean`
- `patients_clean`
- `appointments_clean`
- `appointments_enriched`
- `dq_invalid_appointments`
- `dq_appointments_summary`
- `kaggle_noshow_clean`

## Full and Incremental Appointment Load

Notebook:

```text
notebooks/silver/05_appointments_full_incremental_load.py
```

Work completed:

- Built full load and incremental load logic for the appointments table.
- Used widgets for load type, primary key, watermark column, full source path, incremental source path, processed path, and batch ID.
- Supported full overwrite behavior.
- Supported incremental filtering using `updated_at` watermark.
- Implemented primary-key upsert behavior by removing old matching records and unioning new incremental records.
- Wrote appointments to a partitioned Delta table.
- Optimized the appointment table with ZORDER when supported.
- Created an audit table:

```text
health_cat.bronze.appointments_load_audit
```

Audit fields include batch ID, load type, action, source path, target table, source count, final target count, and audit timestamp.

## Gold Layer Work

Notebook:

```text
notebooks/gold/03_gold_kpis.py
```

Work completed:

- Read `appointments_enriched`, `kaggle_noshow_clean`, diagnostics, and feedback data.
- Built Gold KPI tables for healthcare operations.
- Cached hot tables when enabled.
- Optimized Gold tables when supported.

Gold outputs built:

| Gold Table | Purpose |
| --- | --- |
| `gold_no_show_rate` | Department-level appointment no-show rate |
| `gold_doctor_utilization` | Doctor appointment volume, completed appointments, and no-shows |
| `gold_department_revenue` | Department-level billing revenue |
| `gold_wait_time_trends` | Monthly department wait time trends |
| `gold_patient_revisit_rate` | Patient revisit indicator and visit counts |
| `gold_diagnostics_volume` | Diagnostic test volume by category and test |
| `gold_feedback_summary` | Average rating and feedback count |
| `gold_kaggle_no_show_by_age` | External no-show analysis by age group and gender |

## Validation Work

Notebook:

```text
notebooks/validation/04_validation_checks.py
```

Work completed:

- Validated expected Bronze counts for healthcare source tables.
- Checked that appointment IDs are unique.
- Checked mandatory patient and doctor IDs.
- Checked valid bill amounts.
- Checked valid appointment timestamps.
- Displayed the appointment load audit table.

Expected source tables checked:

- `departments`
- `doctors`
- `patients`
- `appointments`
- `billing`
- `diagnostics`
- `prescriptions`
- `feedback`

## Recommended Run Order

1. `notebooks/bronze/01_bronze_ingestion.py`
2. `notebooks/silver/02_silver_transformations.py`
3. `notebooks/silver/05_appointments_full_incremental_load.py`
4. `notebooks/gold/03_gold_kpis.py`
5. `notebooks/validation/04_validation_checks.py`

## Screenshots to Capture

Screenshots should be stored in `screenshots/`:

- Bronze ingestion row counts
- Bronze table list
- Silver `appointments_enriched`
- DQ appointment summary
- Appointment load audit table
- Gold no-show rate
- Gold doctor utilization
- Gold department revenue
- Gold wait time trends
- Gold feedback summary
- Validation check outputs

## Security Notes

- Do not store Databricks tokens in GitHub.
- Keep cloud storage credentials in Databricks secrets or secure workspace configuration.
- Ensure screenshots do not expose secrets, tokens, or private credentials.
