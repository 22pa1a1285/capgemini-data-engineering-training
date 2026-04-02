# Phase 3A — Data Quality & Cleaning using PySpark

## 🔹 Objective

- The main goal of this phase was to understand how to handle messy data using PySpark. This includes identifying data issues, cleaning the dataset, validating the results, and generating useful insights.

## 🔹 Problem Summary

We were given a dataset containing customer information with several data quality issues. The task was to:
- Identify null values, duplicates, and invalid data
- Clean the dataset using appropriate techniques
- Validate the cleaning process
- Perform aggregation to generate meaningful insights

## 🔹 Approach

- Created DataFrame using createDataFrame()
- Inspected data using show() and count()
- Identified issues such as null values, duplicates, and invalid age
- Cleaned data by:
  - Removing null values in customer_id
  - Replacing missing values using fillna()
  - Removing duplicate rows
  - Filtering invalid age values
- Validated data using row counts before and after cleaning
- Applied aggregation using groupBy() and agg()

## 🔹 Key Transformations

- DataFrame Creation → createDataFrame()
- Viewing Data → show()
- Counting Rows → count()
- Handling Nulls → dropna(), fillna()
- Removing Duplicates → dropDuplicates()
- Filtering Data → filter()
- Column Reference → col()
- Aggregation → groupBy(), agg(), count()
- Renaming Columns → alias()

## 🔹 Output

- Output 1: Original Dataset
  - Displays the raw data with null values, duplicates, and invalid entries
  - Helps in identifying data issues before cleaning
  - 
  - ![WhatsApp Image 2026-04-02 at 8 42 57 PM](https://github.com/user-attachments/assets/12bc1ade-9b9b-488f-8746-baf480854f20)


- Output 2: Cleaned Dataset
  - Shows data after removing null keys, handling missing values, removing duplicates, and filtering invalid age
  - Confirms that cleaning steps are applied correctly
  - 
  -<img width="1270" height="897" alt="{CAD9FD45-A9BA-4C9C-879C-13388A6199CA}" src="https://github.com/user-attachments/assets/c8f29571-2947-4f00-92cd-f642b9463462" />


- Output 3: Row Count Validation
  - Displays row count before and after cleaning
  - Verifies that unwanted data has been removed
 
  - <img width="1264" height="885" alt="{8AD05796-1D7D-4902-B63A-2CBF0241D143}" src="https://github.com/user-attachments/assets/93686052-c61e-4eee-a6ce-c485a4591d91" />


- Output 4: Customers per City
  - Shows number of customers in each city after cleaning
  - Confirms correct aggregation using groupBy() and count()
 
  - <img width="1283" height="770" alt="{119F5607-A0F6-4C91-B412-8FD53381D937}" src="https://github.com/user-attachments/assets/60ba7e28-fb8e-4b53-916d-7397d62698c3" />


## 🔹 Learnings

- Understood importance of data cleaning in real-world scenarios
- Learned how to handle null and missing values in PySpark
- Gained knowledge on removing duplicates effectively
- Understood how to validate data using row counts
- Learned how aggregation helps in generating insights

## 🔹 Challenges

- Handling NULL values in key columns
- Deciding appropriate values for missing data
- Identifying duplicate records correctly
- Filtering invalid values like negative age
- Applying transformations in the correct order

## 🔹 Files in this Folder

- solution.py → PySpark implementation
- phase3a_problem_statement.pdf → Problem description
- outputs/ → Output screenshots
