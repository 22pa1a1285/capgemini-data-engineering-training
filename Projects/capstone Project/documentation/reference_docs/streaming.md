# Streaming Notes

## Purpose

The `notebooks/streaming` folder contains streaming-oriented pipeline files for the FMCG capstone.

## Silver Streaming File

`silver_sales_stream.py` reads streaming/raw tables, joins orders, order items, and payments, validates core fields, converts price values, and publishes a cleaned streaming Silver table.

## Gold Streaming File

`gold_dlt.py` reads the streaming Silver table and creates Gold outputs such as:

- Sales summary
- SKU performance
- Distributor performance
- Payment summary
- Inventory snapshot

## Operational Notes

- Ensure the source streaming tables exist before running the streaming Silver file.
- Validate schema compatibility before starting a production run.
- Monitor failed records and pipeline health from Databricks.
- Capture screenshots of successful pipeline runs for the `screenshots/` folder.
