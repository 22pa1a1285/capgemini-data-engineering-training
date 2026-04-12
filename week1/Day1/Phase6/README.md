
# Phase 6 — Spark Playground Exit Sprint (Advanced Practice Lab)

## 🔹 Objective

- The main goal of this phase was to apply all learned PySpark concepts in a real-world scenario. This includes joins, window functions, data cleaning, date analysis, and building a complete pipeline.

---

## 🔹 Problem Summary

We were given dirty datasets for customers and orders. The task was to:
- Clean and validate the data
- Perform different types of joins
- Apply window functions for ranking and analysis
- Perform date-based analysis
- Build a complete pipeline for final reporting

---

## 🔹 Approach

- Created DataFrames for customers and orders
- Identified data issues:
  - NULL values
  - Invalid foreign keys
  - Negative and missing amounts
  - Duplicate records
- Applied transformations in multiple practice sets:
  - Join operations
  - Window functions
  - Date analysis
  - Pipeline building
- Generated final aggregated and ranked output

---

## 🔹 Key Transformations

- DataFrame Creation → createDataFrame()
- Data Cleaning → filter(), dropDuplicates()
- Join Operations → inner, left, left_anti
- Aggregation → groupBy(), sum()
- Window Functions → Window(), rank(), lag()
- Date Functions → to_date(), month(), datediff()
- Column Operations → col()
- Output Writing → saveAsTable()

---

## 🔹 Output

### Practice Set A: Join Analysis
- Inner Join → Valid matched records
- Left Join → All records with NULL identification
- Left Anti Join → Invalid foreign key detection
- Row count comparison across joins

### Practice Set B: Window Functions
- Customer ranking based on total spend
- Previous order value using lag()

### Practice Set C: Date Analysis
- Extracted month from order_date
- Calculated date differences for trend analysis

### Practice Set D: Pipeline Output
- Cleaned and validated orders
- Removed duplicates
- Aggregated total sales per customer and city
- Ranked customers within each city
- Final report saved as table

---

## 🔹 Learnings

- Learned how to handle dirty datasets effectively
- Gained strong understanding of different join types
- Improved skills in window functions like rank() and lag()
- Learned how to perform date-based analysis
- Understood how to build an end-to-end pipeline

---

## 🔹 Challenges

- Handling invalid foreign keys correctly
- Managing NULL and negative values
- Writing correct window specifications
- Ensuring no duplicates in final output
- Combining multiple transformations efficiently

---

## 🔹 Files in this Folder

- solution.py → PySpark implementation
- phase6_problem_statement.pdf → Problem description
- outputs/ → Output screenshots

---

## 🔹 Final Summary

This phase helped in consolidating all PySpark concepts including joins, cleaning, window functions, and pipeline building. It serves as a complete hands-on practice for real-world data engineering tasks.
