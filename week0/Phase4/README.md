# Phase 4 — Mini Project: Business Pipeline & Analytics using PySpark

## 🔹 Objective

- The main goal of this phase was to build a complete business analytics pipeline using PySpark. This includes data cleaning, transformation, aggregation, and generating business-level insights from raw datasets.

## 🔹 Problem Summary

We were given customer and sales datasets. The task was to:
- Clean and prepare raw data
- Join datasets to create a unified view
- Perform multiple analytical tasks
- Generate business insights such as revenue, top customers, and segmentation
- Build a final reporting dataset

## 🔹 Approach

- Initialized Spark session
- Loaded datasets using spark.read.csv()
- Cleaned data using a reusable function:
  - Removed null values
  - Removed duplicates
  - Converted data types
  - Filtered invalid values
- Joined cleaned datasets using customer_id
- Converted date column to proper format
- Built multiple analytical outputs:
  - Daily sales
  - City-wise revenue
  - Top customers
  - Repeat customers
  - Customer segmentation
- Created final reporting table
- Saved output as CSV file

## 🔹 Key Transformations

- Data Extraction → spark.read.csv()
- Data Cleaning → dropna(), dropDuplicates(), filter()
- Type Casting → cast()
- Column Operations → col(), concat(), lit(), when()
- Date Handling → to_date()
- Joining → join()
- Aggregation → groupBy(), sum(), count()
- Sorting → orderBy(), desc()
- Limiting → limit()
- Output Writing → write.csv()

## 🔹 Output

- Output 1: Daily Sales
  - Shows total sales per day
  - Helps track daily performance
 
  - ![p4_Task1_Query](https://github.com/user-attachments/assets/c336ca74-1b05-4e60-a3b8-a7e63e8df23f)


- Output 2: City-wise Revenue
  - Displays revenue generated per city
  - Useful for regional analysis
 
  - ![p4_Task2_Query](https://github.com/user-attachments/assets/b9484cee-c384-49c0-b8c8-1d5ec20206e3)


- Output 3: Top 5 Customers
  - Identifies highest spending customers
  - Helps in customer targeting
 
  - ![p4_Task3_Query](https://github.com/user-attachments/assets/011cb243-4545-4a9f-9950-de7406f3ee6b)


- Output 4: Repeat Customers
  - Shows customers with more than one order
  - Useful for retention analysis
 
  - ![p4_Task4_Query](https://github.com/user-attachments/assets/f2376a01-d2a7-42a5-936e-2217bf401010)


- Output 5: Customer Segmentation
  - Categorizes customers into Gold, Silver, Bronze
  - Based on total spending
 
  - ![p4_Task5_Query](https://github.com/user-attachments/assets/748df077-8ea9-4606-982e-9a506b4ec87c)


- Output 6: Final Reporting Table
  - Combines customer details, spending, orders, and segment
  - Ready for business reporting
 
  - ![p4_Task6_Query](https://github.com/user-attachments/assets/022cafcd-fa08-4802-99bb-f6cb5145b867)


## 🔹 Learnings

- Understood how to build an end-to-end data pipeline
- Learned how to modularize cleaning logic using functions
- Gained experience in real-world business metrics
- Learned customer segmentation techniques
- Improved skills in joining and aggregating large datasets

## 🔹 Challenges

- Handling data quality issues across multiple datasets
- Managing multiple transformations efficiently
- Understanding segmentation logic
- Ensuring joins do not create duplicate or incorrect records

## 🔹 Files in this Folder

- solution.py → PySpark pipeline implementation :contentReference[oaicite:0]{index=0}
- phase4_problem_statement.pdf → Problem description
- outputs/ → Output screenshots
