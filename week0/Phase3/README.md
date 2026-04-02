# Phase 3 — Final ETL & Pipeline using PySpark

## 🔹 Objective

- The main goal of this phase was to build an end-to-end ETL (Extract, Transform, Load) pipeline using PySpark. This includes reading data from sources, cleaning and transforming it, and generating business insights.

## 🔹 Problem Summary

We were given multiple datasets such as customers and sales. The task was to:
- Extract data from source files
- Clean and prepare the data
- Join datasets to create a unified view
- Perform aggregations and build business metrics
- Generate final reports for analysis

## 🔹 Approach

- Initialized Spark session
- Extracted data using spark.read.csv()
- Cleaned data by:
  - Removing null values
  - Casting columns to correct data types
- Joined datasets using customer_id
- Built transformations and metrics:
  - Daily sales calculation
  - City-wise revenue
  - Repeat customers identification
  - Top customers per city using window functions
- Generated final reporting dataset
- Displayed outputs using show()

## 🔹 Key Transformations

- Data Extraction → spark.read.csv()
- Cleaning → dropna(), cast()
- Joining → join()
- Aggregation → groupBy(), sum(), count()
- Filtering → filter()
- Column Operations → col()
- Window Functions → Window(), rank()
- Sorting → orderBy()
- Output → show()

## 🔹 Output

- Output 1: Daily Sales
  - Shows total sales per day
  - Validates aggregation using groupBy()
 
  - ![p3_pyspark_query1](https://github.com/user-attachments/assets/e9254a4a-cf90-426e-8088-4ca1cacf70a7)


- Output 2: City-wise Revenue
  - Displays total revenue generated per city
  - Helps in regional analysis
 
  - ![p3_pyspark_query2](https://github.com/user-attachments/assets/ab489c5d-e981-4f19-be6b-8965241ed321)


- Output 3: Repeat Customers
  - Identifies customers with more than 2 orders
  - Useful for customer behavior analysis
 
  ![p3_pyspark_query3](https://github.com/user-attachments/assets/aea44912-e6ea-4a3b-8972-9af797e87a7a)


- Output 4: Top Customers per City
  - Shows highest spending customer in each city
  - Uses window functions and ranking
 
  - ![p3_pyspark_query4](https://github.com/user-attachments/assets/ca129185-af2a-4934-badc-42a145f7b1a5)


- Output 5: Final Report
  - Combines customer and sales data
  - Provides total spending and order count per customer
 
  - ![p3_pyspark_query5](https://github.com/user-attachments/assets/e0e60147-889a-4762-9fd0-675d229db065)


## 🔹 Learnings

- Understood complete ETL pipeline flow (Extract → Transform → Load)
- Learned how to modularize code using functions
- Gained experience in joins and aggregations
- Learned how to use window functions for ranking
- Understood how to generate business-level insights

## 🔹 Challenges

- Handling data type conversions correctly
- Writing correct join conditions
- Understanding window functions and ranking
- Managing multiple transformations in pipeline flow

## 🔹 Files in this Folder

- solution.py → PySpark ETL pipeline implementation
- phase3_problem_statement.pdf → Problem description
- outputs/ → Output screenshots
