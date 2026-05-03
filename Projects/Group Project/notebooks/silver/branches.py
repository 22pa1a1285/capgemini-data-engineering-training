# Databricks notebook source
# DBTITLE 1,Setup Delta Path
# Define the Delta table path

silver_branches_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/branches"

print(f"Delta table will be saved to: {silver_branches_path}")

# COMMAND ----------

# DBTITLE 1,Create Branches Table
# Create Branches DataFrame with proper schema

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col

# Define the schema explicitly for type safety
schema = StructType([
    StructField("branch_id", StringType(), False),
    StructField("branch_name", StringType(), False),
    StructField("city", StringType(), False)
])

# Create sample branch data
data = [
    ("B1", "Main Branch", "Hyderabad"),
    ("B2", "Central Branch", "Mumbai"),
    ("B3", "North Branch", "Delhi"),
    ("B4", "South Branch", "Chennai")
]

# Create DataFrame with explicit schema
df_branches = spark.createDataFrame(data, schema=schema)

print(f"Total branches created: {df_branches.count()}")
print("\nBranches Schema:")
df_branches.printSchema()

print("\nBranches Data:")
df_branches.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Remove Duplicates
# Remove duplicates (if any) based on branch_id

print(f"Before deduplication: {df_branches.count()}")
df_branches = df_branches.dropDuplicates(["branch_id"])
print(f"After deduplication: {df_branches.count()}")

print("\nFinal branches:")
df_branches.orderBy("branch_id").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Save to Delta Table
# Save as Delta table

df_branches.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_branches_path)

print(f"✓ Branches table saved successfully to: {silver_branches_path}")

# COMMAND ----------

# DBTITLE 1,Verify Saved Delta Table
# Verify the saved Delta table

df_verify = spark.read.format("delta").load(silver_branches_path)

print(f"Total branches in Delta table: {df_verify.count()}")
print("\nDelta Table Schema:")
df_verify.printSchema()

print("\nDelta Table Contents:")
df_verify.orderBy("branch_id").show(truncate=False)