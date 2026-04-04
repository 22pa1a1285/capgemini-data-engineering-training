
# Phase 4A — Bucketing & Segmentation in PySpark

## 🔹 Objective

- The main goal of this phase was to perform customer segmentation using different techniques in PySpark. This includes rule-based segmentation, quantile-based segmentation, bucketization, and ranking using window functions.

## 🔹 Problem Summary

We were given customer and sales datasets. The task was to:
- Calculate total spend per customer
- Segment customers based on spending
- Apply multiple segmentation techniques
- Analyze customer distribution across segments

## 🔹 Approach

- Initialized Spark session
- Loaded datasets using spark.read.csv()
- Performed data preparation:
  - Converted data types using cast()
  - Joined datasets using customer_id
- Calculated total spend per customer using groupBy()
- Applied different segmentation techniques:
  - Conditional segmentation using when()
  - Quantile-based segmentation using approxQuantile()
  - Bucketization using MLlib Bucketizer
  - Ranking using window functions

## 🔹 Key Transformations

- Data Extraction → spark.read.csv()
- Type Casting → cast()
- Joining → join()
- Aggregation → groupBy(), sum()
- Conditional Logic → when()
- Quantile Calculation → approxQuantile()
- Bucketization → Bucketizer
- Window Functions → Window(), percent_rank()
- Column Reference → col()

## 🔹 Output

- Output 1: Conditional Segmentation
  - Customers categorized as Gold, Silver, Bronze based on spending rules
  - 
  ![WhatsApp Image 2026-04-04 at 4 10 13 PM](https://github.com/user-attachments/assets/ca3877cc-b83b-44a7-a217-fa5d4bb3b53e)


- Output 2: Customer Count by Segment
  - Shows distribution of customers across segments
 
  - ![WhatsApp Image 2026-04-04 at 4 13 53 PM](https://github.com/user-attachments/assets/8fdac2f4-18f4-42a8-93ca-293238f5dea0)


- Output 3: Quantile-Based Segmentation
  - Segmentation based on data distribution using quantiles
 
  - ![WhatsApp Image 2026-04-04 at 4 15 52 PM](https://github.com/user-attachments/assets/688dba35-b67c-4dcb-9e51-1ff1fecda3b7)


- Output 4: Bucketizer Output
  - Numerical bucketing of customers into ranges
 
  - ![WhatsApp Image 2026-04-04 at 4 15 52 PM](https://github.com/user-attachments/assets/23f12b7c-4b80-4264-880a-9f53560507e8)


- Output 5: Window-Based Ranking
  - Customers ranked based on spending percentile
 
  - ![WhatsApp Image 2026-04-04 at 4 16 47 PM](https://github.com/user-attachments/assets/50866d43-6dce-4bee-86ea-096dd7a60919)


## 🔹 Learnings

- Learned multiple ways of customer segmentation
- Understood difference between rule-based and data-driven segmentation
- Gained knowledge of MLlib Bucketizer
- Learned how window functions help in ranking and analytics
- Improved understanding of real-world business segmentation

## 🔹 Challenges

- Choosing correct thresholds for segmentation
- Understanding quantile-based logic
- Working with Bucketizer and defining splits
- Applying window functions correctly

## 🔹 Files in this Folder

- solution.py → PySpark implementation
- phase4a_problem_statement.pdf → Problem description
- outputs/ → Output screenshots
