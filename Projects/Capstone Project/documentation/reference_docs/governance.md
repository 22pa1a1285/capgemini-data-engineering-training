# Governance Notes

## Purpose

This document records the governance expectations for the FMCG capstone pipeline.

## Data Governance Practices

- Keep raw source files in the Bronze layer without business transformations.
- Add ingestion metadata to support lineage and auditability.
- Apply validation and quarantine rules before publishing Silver and Gold outputs.
- Keep business-ready tables in the Gold layer.
- Do not store credentials, tokens, or secrets in notebooks or GitHub files.

## Data Quality Rules

- Reject records with invalid or non-positive price values.
- Reject records with missing or future invoice/order dates.
- Remove duplicate order and product combinations.
- Standardize payment type values.
- Enrich output records with region and channel fields where possible.

## Security

- Use Databricks secrets or environment variables for credentials.
- Restrict write access to production tables.
- Keep screenshots free from tokens, account IDs, and sensitive customer details.
