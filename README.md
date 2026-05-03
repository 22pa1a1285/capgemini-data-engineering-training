# Capgemini Data Engineering Training

This repository contains my Capgemini data engineering training work, organized by week, day, and phase. It includes SQL practice, PySpark DataFrame solutions, Databricks notebooks, Delta Lake exercises, medallion architecture assignments, problem statements, and output screenshots.

## Repository Overview

| Folder | Contents |
| --- | --- |
| `week0/Phase0` | Associate Data Engineering learning pathway certificates |
| `week0/Phase1` | Basic SQL operations implemented with PySpark DataFrames |
| `week0/Phase2` | SQL-to-PySpark transformations and query practice |
| `week0/Phase3` | Intermediate PySpark and SQL query tasks |
| `week0/Phase3a` | Additional PySpark practice tasks |
| `week0/Phase4` | Data cleaning and analytical query tasks |
| `week0/Phase4a` | Additional data analysis practice |
| `week1/Day1` | Phase 5 and Phase 6 PySpark/Databricks assignments |
| `week1/Day2` | SQL joins and group-by practice |
| `week1/Day3` | Case expressions, regex basics, and window functions |
| `week1/Day4` | Advanced SQL assignment and real-data SQL analysis |
| `week1/Day5` | Big sales dataset practice notebook and CSV data |
| `week1/Day6` | Car sales mini pipeline assignment and notebook |
| `week2/Day7` | Insurance pipeline assignment |
| `week2/Day8` | Delta Lake, widgets, null handling, UDFs, and end-to-end pipeline notebooks |
| `week2/Day9` | Data quality checks, star schema, and medallion architecture practice |
| `Projects` | Individual, group, and capstone Databricks project documentation structure |

## Key Topics Covered

- Databricks workspace development
- Apache Spark and PySpark
- Spark SQL
- DataFrame transformations
- Joins, aggregations, case expressions, regex, and window functions
- Data cleaning and validation
- Delta Lake operations
- Full and incremental data loads
- Medallion architecture: Bronze, Silver, and Gold layers
- Data quality checks and dashboard-ready aggregations

## Projects

The `Projects/` folder contains dedicated spaces for major Databricks project work:

- `Individual Project - Consolated Pipelines in Databricks`
- `Group Project - Banking in Databricks`
- `Capstone Project`

Each project has separate folders for notebooks, documentation, and screenshots.

## Typical Folder Structure

Most phase folders follow this pattern:

```text
PhaseX/
  README.md                  # Phase-level explanation
  solution.py                # PySpark implementation
  queries.sql                # SQL solution, where applicable
  *_problem_statement.pdf    # Assignment/problem statement
  Outputs/                   # Result screenshots
```

Some later assignments use Databricks notebooks (`.ipynb`) instead of only Python or SQL scripts.

## How to Use This Repository

1. Clone the repository:

   ```bash
   git clone https://github.com/22pa1a1285/capgemini-data-engineering-training.git
   cd capgemini-data-engineering-training
   ```

2. Open the required phase or day folder.

3. Review the local `README.md` for the assignment objective and approach.

4. Run `.sql`, `.py`, or `.ipynb` files in Databricks, depending on the assignment.

5. Compare your results with the screenshots in the `Outputs/` folder where available.

## Databricks Setup

Use a Databricks workspace with a cluster that supports PySpark and Delta Lake. The notebooks and scripts are intended to be run from Databricks.

Recommended workflow:

1. Import or clone this GitHub repository into Databricks Repos.
2. Attach notebooks to an active cluster.
3. Run cells in order.
4. Store temporary tables, managed tables, or Delta paths according to the assignment instructions.

Detailed setup notes are available in [docs/DATABRICKS_GITHUB_SETUP.md](docs/DATABRICKS_GITHUB_SETUP.md).

## Security Notes

- Do not commit Databricks personal access tokens.
- Do not paste secrets into notebooks, README files, screenshots, or Git history.
- Store workspace credentials in local environment variables or Databricks secrets.
- If a token was exposed, revoke it from Databricks and create a new one.

## Suggested Databricks Environment Variables

For local tools such as the Databricks CLI, use environment variables instead of hardcoding credentials:

```bash
DATABRICKS_HOST=https://your-workspace-url
DATABRICKS_TOKEN=your-token-value
```

On Windows PowerShell:

```powershell
$env:DATABRICKS_HOST = "https://your-workspace-url"
$env:DATABRICKS_TOKEN = "your-token-value"
```

## Status

This repository is a training portfolio and will continue to grow as new assignments, notebooks, and outputs are completed.
