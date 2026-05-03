# Exported Banking Databricks Notebooks

These notebooks were exported from:

```text
/Shared/Banking-Transactions-Lakehouse-Project-Selected-Dataset-Edition
```

## Notebook Folders

| Folder | Contents |
| --- | --- |
| `bronze` | Raw banking transaction load |
| `silver` | Transaction cleaning plus accounts, customers, cards, and branches |
| `gold` | KPI, final report, ranking, running total, and aggregation outputs |

`mast.py` is the master orchestration notebook that runs Bronze, Silver, and Gold notebooks in sequence.
