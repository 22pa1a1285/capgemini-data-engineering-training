# Healthcare Capstone Notebooks

These files came from `healthcare-ops-capstone.zip` and are organized by pipeline layer.

## Folders

| Folder | Contents |
| --- | --- |
| `bronze` | Raw healthcare CSV ingestion into Bronze Delta tables |
| `silver` | Silver transformations and appointment full/incremental load logic |
| `gold` | Healthcare KPI table creation |
| `validation` | Source count and data quality validation checks |

## Run Order

1. `bronze/01_bronze_ingestion.py`
2. `silver/02_silver_transformations.py`
3. `silver/05_appointments_full_incremental_load.py`
4. `gold/03_gold_kpis.py`
5. `validation/04_validation_checks.py`
