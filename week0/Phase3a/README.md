Phase 3A – Data Quality & Cleaning Challenge
Objective:
Work with intentionally messy data and apply cleaning techniques before building a pipeline
-In this phase, we worked with a messy dataset and performed data cleaning and aggregation using PySpark. 
The goal was to identify issues in the data, clean it properly, validate the results, and generate useful insights.

#######Data Cleaning Steps

We performed the following cleaning operations:

Removed null customer_id
Since it is a key field, rows with NULL values were removed
Handled missing values
Replaced NULL values in:
name → "Unknown"
city → "Unknown"
Removed duplicate records
Ensured only unique rows are retained
Filtered invalid data
Removed rows where age is less than 0

######### Data Validation:
To ensure cleaning was successful:
Before cleaning
After cleaning

######### Methods Used:
createDataFrame()
count()
dropna()
fillna()
dropDuplicates()
filter()
col()
groupBy()
agg()
alias()
show()

######### Challenges Faced
Handling NULL values in key columns
Deciding how to fill missing values appropriately
Identifying and removing duplicate records
Filtering invalid data (negative age)
Understanding difference between DataFrame methods and functions
Correct use of aggregation functions with groupBy()


######### Key Learnings:
Importance of handling missing and invalid data
How to remove duplicates in PySpark
Using groupBy() and agg() for analysis
Validating data before and after cleaning
