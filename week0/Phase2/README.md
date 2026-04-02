
# Phase 2 — SQL to PySpark Transformation

## 🔹 Objective

- The main goal of this phase was to understand how SQL queries can be translated into PySpark DataFrame operations. This includes data cleaning, joins, aggregations, and generating insights.

## 🔹 Problem Summary

We were given datasets such as customers and sales. The task was to:
- Clean and prepare the data
- Join datasets using common keys
- Perform SQL-like operations in PySpark
- Generate insights such as total spend, top customers, and revenue

## 🔹 Approach

- Loaded datasets using spark.read.csv()
- Cleaned data by removing null customer_id values
- Checked schema using printSchema()
- Converted data types using cast()
- Joined datasets using inner join on customer_id
- Applied transformations equivalent to SQL queries:
  - groupBy and aggregations
  - filtering conditions
  - sorting and limiting results

## 🔹 Key Transformations

- Data Extraction → spark.read.csv()
- Data Cleaning → dropna()
- Schema Inspection → printSchema()
- Type Casting → cast()
- Joining → join()
- Aggregation → groupBy(), sum(), avg(), count()
- Filtering → filter()
- Sorting → orderBy(), desc()
- Limiting → limit()
- Column Reference → col()
- Formatting → round()

## 🔹 Output

- Output 1: Total Order Amount per Customer
  - Shows total spending of each customer
  - Equivalent to SQL GROUP BY with SUM
 
  - ![p2_pyspark_query1](https://github.com/user-attachments/assets/3048cdc7-0b3a-4b7b-b0ac-ff2a48625136)


- Output 2: Top 3 Customers by Spend
  - Displays top customers based on total spending
  - Uses sorting and limiting
 
  - ![p2_pyspark_query2](https://github.com/user-attachments/assets/7e77b2ad-0507-43d1-929a-2bd91df412dd)


- Output 3: Customers with No Orders
  - Identifies customers without matching sales records
  - Uses left_anti join
 
  - ![p2_pyspark_query3](https://github.com/user-attachments/assets/69f3ad4d-0684-4e85-af3e-551eeda33bea)


- Output 4: City-wise Total Revenue
  - Shows total revenue generated per city
  - Uses aggregation and rounding
 
  - ![p2_pyspark_query4](https://github.com/user-attachments/assets/6dcf6a35-bd3c-4f35-b73d-d0208d4c2867)


- Output 5: Average Order Amount per Customer
  - Calculates average spending per customer
 
  - ![p2_pyspark_query5](https://github.com/user-attachments/assets/84498b9c-c92c-4082-bb4f-fccae2bbb47f)


- Output 6: Customers with More Than One Order
  - Filters customers based on order count
 
  - ![p2_pyspark_query6](https://github.com/user-attachments/assets/49e38f25-72df-489c-a7ba-3a91d73bb6b3)


- Output 7: Customers Sorted by Total Spend
  - Displays customers ranked by spending in descending order
 
  - ![p2_pyspark_query7](https://github.com/user-attachments/assets/f679a0f9-0de7-4015-af3c-bef7f3431aed)


## 🔹 Learnings

- Understood how SQL operations map to PySpark transformations
- Learned how to perform joins and aggregations in PySpark
- Gained clarity on filtering and sorting data
- Improved understanding of handling data types

## 🔹 Challenges

- Converting SQL logic into PySpark syntax
- Handling data type casting correctly
- Writing correct join conditions
- Debugging aggregation and sorting results

## 🔹 Files in this Folder

- solution.py → PySpark implementation
- queries.sql → SQL equivalent queries
- phase2_problem_statement.pdf → Problem description
- outputs/ → Output screenshots
