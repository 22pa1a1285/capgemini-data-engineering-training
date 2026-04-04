
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

- Output 2: Customer Count by Segment
  - Shows distribution of customers across segments

- Output 3: Quantile-Based Segmentation
  - Segmentation based on data distribution using quantiles

- Output 4: Bucketizer Output
  - Numerical bucketing of customers into ranges

- Output 5: Window-Based Ranking
  - Customers ranked based on spending percentile

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
