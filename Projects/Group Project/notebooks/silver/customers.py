# Databricks notebook source
# DBTITLE 1,Setup and Read Accounts
# Setup paths and read Silver accounts

from pyspark.sql.functions import *
from pyspark.sql.types import *

accounts_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/accounts"
customers_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/customers"

df_accounts = spark.read.format("delta").load(accounts_path)
print(f"Total accounts: {df_accounts.count():,}")
df_accounts.printSchema()
df_accounts.show(10, truncate=False)

# COMMAND ----------

# DBTITLE 1,Create Customer ID
# Create customer_id from account_id

df_customers = df_accounts.withColumn("customer_id", col("account_id"))

df_customers.select("customer_id", "account_id").show(10, truncate=False)

# COMMAND ----------

# DBTITLE 1,Create Customer Name
# Create customer_name column

df_customers = df_customers.withColumn("customer_name", concat(lit("Customer_"), col("account_id")))

df_customers.select("customer_id", "account_id", "customer_name").show(10, truncate=False)

# COMMAND ----------

# DBTITLE 1,Add City Column
# Add city column with random values

cities = ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Bangalore"]

# Use hash function to randomly assign cities (since account_id is string)
df_customers = df_customers.withColumn(
    "city",
    when((hash(col("account_id")) % 5) == 0, lit("Hyderabad"))
    .when((hash(col("account_id")) % 5) == 1, lit("Mumbai"))
    .when((hash(col("account_id")) % 5) == 2, lit("Delhi"))
    .when((hash(col("account_id")) % 5) == 3, lit("Chennai"))
    .otherwise(lit("Bangalore"))
)

print("City distribution:")
df_customers.groupBy("city").count().orderBy("city").show()

# COMMAND ----------

# DBTITLE 1,Remove Duplicates
# Ensure no duplicates

print(f"Before deduplication: {df_customers.count():,}")
df_customers = df_customers.dropDuplicates(["customer_id"])
print(f"After deduplication: {df_customers.count():,}")

# COMMAND ----------

# DBTITLE 1,Select Final Columns
# Select final columns

df_customers = df_customers.select(
    "customer_id",
    "account_id",
    "customer_name",
    "city"
)

df_customers.printSchema()
df_customers.show(10, truncate=False)

# COMMAND ----------



# COMMAND ----------

# DBTITLE 1,Save to Delta
# Save as Delta table

df_customers.write.format("delta").mode("overwrite").save(customers_path)
print(f"✓ Saved to: {customers_path}")

# COMMAND ----------

# DBTITLE 1,Sample Output and Summary
# Display sample data and summary

print("Final Customer Table:")
df_customers.orderBy("customer_id").show(20, truncate=False)

print("\nSummary:")
print(f"Total customers: {df_customers.count():,}")
print(f"\nCustomers per city:")
df_customers.groupBy("city").count().orderBy("city").show()