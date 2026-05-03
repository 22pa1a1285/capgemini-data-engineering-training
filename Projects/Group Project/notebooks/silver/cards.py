# Databricks notebook source
# DBTITLE 1,Read Accounts and Generate Cards
# Read accounts table and generate cards

from pyspark.sql.functions import col, concat, lit, when, rand

# Define paths
silver_accounts_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/accounts"
silver_cards_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta/silver/cards"

# Read accounts table
df_accounts = spark.read.format("delta").load(silver_accounts_path)

print(f"Total accounts: {df_accounts.count()}")
print("\nAccounts Schema:")
df_accounts.printSchema()
print("\nSample accounts:")
df_accounts.show(5, truncate=False)

# COMMAND ----------

# DBTITLE 1,Generate Card ID and Card Type
# Generate card_id and card_type columns

# Create card_id as "C_" + account_id
df_cards = df_accounts.withColumn(
    "card_id",
    concat(lit("C_"), col("account_id"))
)

# Randomly assign card_type (Debit or Credit)
df_cards = df_cards.withColumn(
    "card_type",
    when(rand() < 0.5, lit("Debit")).otherwise(lit("Credit"))
)

# Select only required columns
df_cards = df_cards.select("card_id", "account_id", "card_type")

print(f"Total cards generated: {df_cards.count()}")
print("\nCards with account relationship:")
df_cards.show(10, truncate=False)

# COMMAND ----------

# DBTITLE 1,Remove Duplicates and Show Schema
# Remove duplicates based on card_id

print(f"Before deduplication: {df_cards.count()}")
df_cards = df_cards.dropDuplicates(["card_id"])
print(f"After deduplication: {df_cards.count()}")

print("\nFinal Cards Schema:")
df_cards.printSchema()

print("\nCard Type Distribution:")
df_cards.groupBy("card_type").count().orderBy("card_type").show()

# COMMAND ----------

# DBTITLE 1,Save to Delta Table
# Save as Delta table

df_cards.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(silver_cards_path)

print(f"✓ Cards table saved successfully to: {silver_cards_path}")

# COMMAND ----------

# DBTITLE 1,Verify Saved Delta Table
# Verify the saved Delta table

df_verify = spark.read.format("delta").load(silver_cards_path)

print(f"Total cards in Delta table: {df_verify.count()}")
print("\nDelta Table Schema:")
df_verify.printSchema()

print("\nSample cards with foreign key relationship:")
df_verify.orderBy("card_id").show(10, truncate=False)

print("\nCard Type Distribution:")
df_verify.groupBy("card_type").count().orderBy("card_type").show()