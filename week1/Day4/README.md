
# Advanced SQL Assignment — Student Submission Analysis

## 🔹 Objective

- The main goal of this assignment is to analyze student submission data using advanced SQL techniques. This includes handling messy data, detecting duplicates, and generating insights using joins and window functions.

---

## 🔹 Problem Summary

We were given three datasets:

- **Student Master Table** → Contains student details (56 records)
- **Task1_Responses** → Submission data (51 records)
- **Task1_File2** → Additional submissions with duplicates and invalid entries (60 records)

### Tasks:
- Normalize and clean data
- Map emails to students
- Identify valid, invalid, and missing submissions
- Detect duplicates using window functions
- Generate analytical insights

---

## 🔹 Approach

### Phase 1: Data Preparation
- Loaded datasets using `read_files()`
- Normalized emails using `LOWER()` and `TRIM()`
- Created unified email mapping using `UNION ALL`
- Built normalized submission view

### Phase 2: Core Analysis
- Used **LEFT ANTI JOIN** to find students who did not submit
- Used **INNER JOIN** to identify valid submissions
- Used **LEFT ANTI JOIN** to detect invalid submissions

### Phase 3: Duplicate Detection
- Used `ROW_NUMBER()` with window function to detect duplicates
- Partitioned by `student_id`
- Ordered by timestamp to keep first valid submission
- Marked remaining records as duplicates

### Phase 4: Advanced Insights
- Counted submissions per student
- Identified students using both emails
- Classified records into:
  - Submitted
  - Not Submitted
  - Duplicate
  - Invalid

---

## 🔹 NULL Handling Practice

This section focuses on handling NULL values in real-world datasets using SQL.

### Topics Covered:
- Identifying NULL and NOT NULL values
- Replacing NULL values using `COALESCE()`
- Handling multiple fallback values
- Using `NULLIF()` to convert specific values into NULL
- Avoiding divide-by-zero errors
- Performing calculations with NULL-safe logic

### Key Functions Used:
- `IS NULL`, `IS NOT NULL`
- `COALESCE()`
- `NULLIF()`

### Real-World Use Cases:
- Replacing missing salary, bonus, or price values
- Calculating total income safely
- Handling missing order amounts and discounts
- Cleaning product and transaction data

---

## 🔹 Key Concepts Used

- Joins → INNER JOIN, LEFT ANTI JOIN  
- Data Cleaning → LOWER(), TRIM()  
- NULL Handling → COALESCE(), NULLIF(), IS NULL  
- Set Operations → UNION ALL  
- Aggregation → COUNT(), GROUP BY  
- Window Functions → ROW_NUMBER() OVER()  
- Conditional Logic → CASE WHEN  
- Data Mapping → COALESCE  

---

## 🔹 Output

- Output 1: Students who did NOT submit
- Output 2: Valid submissions matched with student data
- Output 3: Invalid submissions (emails not found in master)
- Output 4: Duplicate submissions identified using window functions
- Output 5: Final classification of all records
- Output 6: NULL handling transformations and cleaned outputs

---

## 🔹 Learnings

- Learned how to handle real-world messy datasets
- Understood importance of data normalization
- Gained strong knowledge of SQL joins
- Learned how window functions help in duplicate detection
- Understood NULL handling techniques using COALESCE and NULLIF
- Learned how to safely perform calculations with missing data

---

## 🔹 Challenges

- Matching emails across multiple datasets
- Handling duplicates correctly
- Writing efficient join queries
- Managing NULL values in calculations
- Understanding window function behavior

---

## 🔹 Files in this Folder

- queries.sql → SQL queries implementation
- dataset/ → Input CSV files
- outputs/ → Result screenshots

---


## 🔹 Final Summary

This assignment helped in understanding how to clean, join, and analyze data using advanced SQL techniques. It also provided hands-on experience with window functions and NULL handling in real-world scenarios.
