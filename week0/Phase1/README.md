# Phase 1 — SQL to PySpark

## 🔹 Objective

- The main goal of this phase was to understand basic SQL operations and how they can be implemented using PySpark DataFrame API.

## 🔹 Problem Summary

We were given a simple customer dataset. The task was to:
- Display data
- Apply filtering conditions
- Select specific columns
- Perform basic aggregation

## 🔹 Approach

- Created DataFrame using createDataFrame()
- Viewed data using show()
- Applied filtering using filter() and col()
- Selected specific columns using select()
- Performed aggregation using groupBy() and count()

## 🔹 Key Transformations

- DataFrame Creation → createDataFrame()
- Viewing Data → show()
- Filtering → filter(), col()
- Column Selection → select()
- Aggregation → groupBy(), count()

## 🔹 Output

- Output 1: All Customers
  - Displays the complete dataset
 
  - ![PYSPARK_Query1](https://github.com/user-attachments/assets/1b1fc84b-8b9d-43bf-80fb-1c68a83f507d)


- Output 2: Customers from Chennai
  - Filters customers based on city
 
  - ![PYSPARK_Query2](https://github.com/user-attachments/assets/470837f2-28fc-46cb-a4da-832fe5f3454d)


- Output 3: Customers with Age > 25
  - Applies condition on age column
 
  - ![PYSPARK_Query3](https://github.com/user-attachments/assets/019e8186-a890-4478-8a4c-843d2851901b)


- Output 4: Selected Columns
  - Displays only customer_name and city
 
  - ![PYSPARK_Query4](https://github.com/user-attachments/assets/9aa4b2fc-83c4-47b7-bc75-634a5d2c0fa6)


- Output 5: Customer Count by City
  - Shows number of customers in each city
 
  - ![PYSPARK_Query5](https://github.com/user-attachments/assets/02655adc-296f-4510-bf9b-60dfb0d91015)


## 🔹 Learnings

- Understood how SQL queries map to PySpark operations
- Learned basic DataFrame operations like select and filter
- Gained understanding of grouping and aggregation
- Improved familiarity with PySpark syntax

## 🔹 Challenges

- Understanding PySpark syntax compared to SQL
- Using col() correctly for filtering conditions
- Learning DataFrame operations step-by-step

## 🔹 Files in this Folder

- solution.py → PySpark implementation
- phase1_problem_statement.pdf → Problem description
- outputs/ → Output screenshots
