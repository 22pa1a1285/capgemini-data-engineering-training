# Day 3 — Window Functions & CASE WHEN in SQL

## 🔹 Objective

- The main goal of this session was to understand and apply SQL window functions and conditional logic using CASE WHEN for advanced data analysis.

---

## 🔹 Problem Summary

We worked with an employees dataset containing:
- Employee details
- Department (city)
- Salary
- Joining date

### Tasks:
- Assign row numbers based on different conditions
- Rank employees using different ranking functions
- Perform partition-based analysis
- Apply CASE WHEN for conditional logic
- Implement nested CASE statements for real-world scenarios

---

## 🔹 Approach

- Created employees table and inserted sample data
- Applied window functions using OVER()
- Used ORDER BY and PARTITION BY for analysis
- Implemented CASE WHEN for conditional calculations
- Used nested CASE for complex business logic

---

## 🔹 Key Concepts Used

- Window Functions → ROW_NUMBER(), RANK(), DENSE_RANK()
- Partitioning → PARTITION BY
- Ordering → ORDER BY
- Conditional Logic → CASE WHEN
- Nested Logic → Nested CASE
- Analytical Queries → OVER()

---

## 🔹 Output

- Output 1: Row Number by Salary
- Output 2: Row Number by Department
- Output 3: Ranking by Salary
- Output 4: Dense Ranking
- Output 5: Joining Date Analysis
- Output 6: Alphabetical Ranking

- Output 7: Bonus Calculation using CASE WHEN
- Output 8: Employee Categorization
- Output 9: Salary-based Segmentation
- Output 10: Promotion & Tax Logic using Nested CASE

---

## 🔹 Learnings

- Learned how window functions work without reducing rows
- Understood difference between:
  - ROW_NUMBER() → unique ranking
  - RANK() → allows gaps
  - DENSE_RANK() → no gaps
- Learned how PARTITION BY helps in group-wise analysis
- Understood how CASE WHEN is used for conditional logic
- Learned how to write nested CASE for complex business rules

---

## 🔹 Challenges

- Understanding differences between ranking functions
- Writing correct PARTITION BY conditions
- Handling ordering correctly
- Writing complex nested CASE statements
- Debugging syntax errors

---

## 🔹 Files in this Folder

- queries.sql → Window functions and CASE statements :contentReference[oaicite:0]{index=0}
- dataset/ → Input data
- outputs/ → Query results screenshots

---

## 🔹 Final Summary

This session covered advanced SQL concepts including window functions and conditional logic. These concepts are widely used in real-world analytics for ranking, segmentation, and business rule implementation.
