# Databricks notebook source
# DBTITLE 1,Setup and Read Bronze Data
# Setup paths and read Bronze Delta table

from pyspark.sql.functions import *
from pyspark.sql.window import Window

bronze_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/bronze/transactions"
silver_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/transactions"

df = spark.read.format("delta").load(bronze_path)
print(f"Total records: {df.count():,}")
df.printSchema()
df.show(5)

# COMMAND ----------

# DBTITLE 1,Drop Unnecessary Columns
# Drop CHQ.NO. and invalid column

df = df.drop("CHQ.NO.", ".")
df.columns

# COMMAND ----------

# DBTITLE 1,Rename Columns
# Rename to clean column names

df = df.withColumnRenamed("Account_No", "account_id") \
       .withColumnRenamed("DATE", "transaction_date") \
       .withColumnRenamed("TRANSACTION_DETAILS", "transaction_details") \
       .withColumnRenamed("VALUE_DATE", "value_date") \
       .withColumnRenamed("WITHDRAWAL_AMT", "withdrawal_amount") \
       .withColumnRenamed("DEPOSIT_AMT", "deposit_amount") \
       .withColumnRenamed("BALANCE_AMT", "balance")

df.columns

# COMMAND ----------

# DBTITLE 1,Convert Data Types
# Remove commas and convert amounts to double

df = df.withColumn("withdrawal_amount", regexp_replace(col("withdrawal_amount"), ",", "").cast("double")) \
       .withColumn("deposit_amount", regexp_replace(col("deposit_amount"), ",", "").cast("double")) \
       .withColumn("balance", regexp_replace(col("balance"), ",", "").cast("double"))

df.printSchema()
df.select("withdrawal_amount", "deposit_amount", "balance").show(5)

# COMMAND ----------

# DBTITLE 1,Create Amount Column
# Create amount column (deposit if not null, else withdrawal)

df = df.withColumn("amount", 
    when(col("deposit_amount").isNotNull(), col("deposit_amount"))
    .otherwise(col("withdrawal_amount"))
)

df.select("withdrawal_amount", "deposit_amount", "amount").show(10)

# COMMAND ----------

# DBTITLE 1,Create Transaction Type
# Create transaction_type (credit for deposits, debit for withdrawals)

df = df.withColumn("transaction_type",
    when(col("deposit_amount").isNotNull(), lit("credit"))
    .otherwise(lit("debit"))
)

df.groupBy("transaction_type").count().show()

# COMMAND ----------

# DBTITLE 1,Convert Date Format
# Convert transaction_date to proper date format

df = df.withColumn("transaction_date", to_date(col("transaction_date"), "d-MMM-yy"))
df.select("transaction_date").show(10)

# COMMAND ----------

# DBTITLE 1,Handle Nulls and Duplicates
# Filter out null amounts and remove duplicates

print(f"Before: {df.count():,}")
df = df.filter(col("amount").isNotNull())
print(f"After null filter: {df.count():,}")
df = df.dropDuplicates()
print(f"After deduplication: {df.count():,}")

# COMMAND ----------

# DBTITLE 1,Data Validation Checks
# Check for data quality issues

from datetime import datetime

print("Data Quality Checks:")
print(f"Negative balances: {df.filter(col('balance') < 0).count():,}")
print(f"Negative amounts: {df.filter(col('amount') < 0).count():,}")
print(f"Future dates: {df.filter(col('transaction_date') > datetime.now().date()).count():,}")
print(f"Missing transaction_date: {df.filter(col('transaction_date').isNull()).count():,}")
print(f"Missing account_id: {df.filter(col('account_id').isNull()).count():,}")
print("\nAll checks passed!" if df.filter((col('balance') < 0) | (col('amount') < 0) | (col('transaction_date') > datetime.now().date())).count() == 0 else "\n⚠️ Data quality issues found!")

# COMMAND ----------

# DBTITLE 1,Select Final Columns
# Select final columns for Silver layer

df_silver = df.select(
    "account_id",
    "transaction_date",
    "amount",
    "transaction_type",
    "balance"
).orderBy("account_id", col("transaction_date").desc())

df_silver.printSchema()
df_silver.show(20, truncate=False)

# COMMAND ----------

# DBTITLE 1,Save to Silver Delta
# Save as Silver Delta table

df_silver.write.format("delta").mode("overwrite").save(silver_path)
print(f"✓ Saved to: {silver_path}")

# COMMAND ----------

# DBTITLE 1,Data Quality Summary
# Display final metrics

print(f"Total Records: {df_silver.count():,}")
print(f"Unique Accounts: {df_silver.select('account_id').distinct().count():,}")
print(f"Date Range: {df_silver.agg(min('transaction_date')).collect()[0][0]} to {df_silver.agg(max('transaction_date')).collect()[0][0]}")
print(f"Credits: {df_silver.filter(col('transaction_type') == 'credit').count():,}")
print(f"Debits: {df_silver.filter(col('transaction_type') == 'debit').count():,}")
print(f"\nTotal Amount: ${df_silver.agg(sum('amount')).collect()[0][0]:,.2f}")
print(f"Average Transaction: ${df_silver.agg(avg('amount')).collect()[0][0]:,.2f}")