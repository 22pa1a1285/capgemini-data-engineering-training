# Databricks notebook source
# DBTITLE 1,Setup and Read Transactions
# Setup paths and read Silver transactions

from pyspark.sql.functions import *
from pyspark.sql.window import Window

silver_transactions_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/transactions"
silver_accounts_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/accounts"

df_transactions = spark.read.format("delta").load(silver_transactions_path)
print(f"Total transactions: {df_transactions.count():,}")
df_transactions.printSchema()
df_transactions.select("account_id", "transaction_date", "balance").show(10)

# COMMAND ----------

# DBTITLE 1,Window Function - Latest Balance
# Use Window function to get latest balance per account

window_spec = Window.partitionBy("account_id").orderBy(col("transaction_date").desc())

df_latest = df_transactions.withColumn("row_num", row_number().over(window_spec))

df_latest.select("account_id", "transaction_date", "balance", "row_num").show(20)

# COMMAND ----------

# DBTITLE 1,Filter Latest Record per Account
# Keep only the latest record for each account

df_accounts = df_latest.filter(col("row_num") == 1)

print(f"Total accounts: {df_accounts.count():,}")
df_accounts.select("account_id", "transaction_date", "balance").show(10)

# COMMAND ----------

# DBTITLE 1,Add Account Type
# Rename balance and add account_type and branch_id columns

from pyspark.sql.functions import hash, abs

df_accounts = df_accounts.select(
    col("account_id"),
    col("balance").alias("latest_balance")
).withColumn("account_type", lit("Savings"))

# Use hash of account_id to randomly assign branch
branch_num = abs(hash(col("account_id"))) % 4

df_accounts = df_accounts.withColumn(
    "branch_id",
    when(branch_num == 0, lit("B1"))
    .when(branch_num == 1, lit("B2"))
    .when(branch_num == 2, lit("B3"))
    .otherwise(lit("B4"))
)

df_accounts.show(10, truncate=False)

# COMMAND ----------

# DBTITLE 1,Remove Duplicates
# Ensure no duplicates and select final columns

print(f"Before deduplication: {df_accounts.count():,}")
df_accounts = df_accounts.dropDuplicates(["account_id"])
print(f"After deduplication: {df_accounts.count():,}")

df_accounts = df_accounts.select("account_id", "latest_balance", "account_type", "branch_id")
df_accounts.printSchema()

# COMMAND ----------

# DBTITLE 1,Save to Delta
# Save as Delta table with schema overwrite

df_accounts.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_accounts_path)
print(f"✓ Saved to: {silver_accounts_path}")

# COMMAND ----------

# DBTITLE 1,Sample Output
# Show sample data ordered by account_id

df_accounts.orderBy("account_id").show(10, truncate=False)

# COMMAND ----------

# DBTITLE 1,Balance Statistics
# Display balance statistics

print("Balance Statistics:")
df_accounts.select(
    min("latest_balance").alias("min_balance"),
    max("latest_balance").alias("max_balance"),
    avg("latest_balance").alias("avg_balance")
).show()

print("\nAccount Type Distribution:")
df_accounts.groupBy("account_type").count().show()

# COMMAND ----------

# DBTITLE 1,Branch Distribution
# Verify branch assignment distribution

print("Accounts per Branch:")
df_accounts.groupBy("branch_id").count().orderBy("branch_id").show()