# Databricks notebook source
# DBTITLE 1,Setup and Read All Silver Tables
from pyspark.sql.functions import *

base_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta"
silver_tables = ["transactions", "accounts", "branches", "cards", "customers"]

for table_name in silver_tables:
    silver_path = f"{base_path}/silver/{table_name}"
    gold_path = f"{base_path}/gold/{table_name}"
    df = spark.read.format("delta").load(silver_path)
    df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(gold_path)
    print(f"✓ {table_name}: {df.count():,} records")

print("\n✅ Silver to Gold push complete")

# COMMAND ----------

# MAGIC %md
# MAGIC ### KPI Table - Business Metrics

# COMMAND ----------

# DBTITLE 1,Create KPI Table - Business Metrics
from pyspark.sql.functions import *
from datetime import datetime

base_path = "/Volumes/workspace/default/banking-transactions-lakehouse-project-selected-dataset-edition/delta"

transactions_df = spark.read.format("delta").load(f"{base_path}/gold/transactions")
accounts_df = spark.read.format("delta").load(f"{base_path}/gold/accounts")
branches_df = spark.read.format("delta").load(f"{base_path}/gold/branches")
cards_df = spark.read.format("delta").load(f"{base_path}/gold/cards")
customers_df = spark.read.format("delta").load(f"{base_path}/gold/customers")

transactions_df.display()
accounts_df.display()
branches_df.display()
cards_df.display()
customers_df.display()

# COMMAND ----------

total_transactions = transactions_df.count()
total_transaction_amount = transactions_df.agg(sum("amount")).collect()[0][0]
avg_transaction_amount = transactions_df.agg(avg("amount")).collect()[0][0]
total_accounts = accounts_df.count()
active_accounts = accounts_df.count()
total_customers = customers_df.count()
total_branches = branches_df.count()
total_cards = cards_df.count()
active_cards = cards_df.count()

# COMMAND ----------

kpi_records = [
    ("total_transactions", float(total_transactions), "count", "Total number of transactions"),
    ("total_transaction_amount", float(total_transaction_amount), "amount", "Total transaction amount"),
    ("avg_transaction_amount", float(avg_transaction_amount), "amount", "Average transaction amount"),
    ("total_accounts", float(total_accounts), "count", "Total number of accounts"),
    ("active_accounts", float(active_accounts), "count", "Number of active accounts"),
    ("total_customers", float(total_customers), "count", "Total number of customers"),
    ("total_branches", float(total_branches), "count", "Total number of branches"),
    ("total_cards", float(total_cards), "count", "Total number of cards"),
    ("active_cards", float(active_cards), "count", "Number of active cards"),
    ("avg_accounts_per_customer", float(total_accounts / total_customers), "ratio", "Average accounts per customer"),
    ("avg_cards_per_customer", float(total_cards / total_customers), "ratio", "Average cards per customer")
]

kpi_schema = ["kpi_name", "kpi_value", "kpi_type", "kpi_description"]
kpi_df = spark.createDataFrame(kpi_records, kpi_schema)

# COMMAND ----------

kpi_path = f"{base_path}/gold/kpi_business_metrics"
kpi_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(kpi_path)
spark.read.format("delta").load(kpi_path).display()

# COMMAND ----------

# DBTITLE 1,Task 5: Join Multiple Tables - Final Report
print("Task 5: Final Report Table")

final_report_df = transactions_df \
    .join(accounts_df, transactions_df.account_id == accounts_df.account_id, "inner") \
    .join(customers_df, accounts_df.account_id == customers_df.account_id, "inner") \
    .join(branches_df, accounts_df.branch_id == branches_df.branch_id, "inner") \
    .join(cards_df, accounts_df.account_id == cards_df.account_id, "left") \
    .select(
        accounts_df.account_id,
        customers_df.customer_name,
        customers_df.city.alias("customer_city"),
        branches_df.branch_name,
        cards_df.card_type,
        transactions_df.transaction_date,
        transactions_df.amount,
        transactions_df.transaction_type,
        accounts_df.latest_balance
    )

final_report_path = f"{base_path}/gold/final_report"
final_report_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(final_report_path)

print(f"Saved: {final_report_path}")
print(f"Records: {final_report_df.count():,}")
display(final_report_df.limit(20))

# COMMAND ----------

# MAGIC %md
# MAGIC ### AGGREGATION

# COMMAND ----------

# DBTITLE 1,Business Aggregations - Solving Real Problems
print("Aggregation 1: Customer Transaction Behavior")

customer_behavior_df = transactions_df \
    .join(accounts_df, "account_id", "inner") \
    .join(customers_df, "account_id", "inner") \
    .groupBy(
        customers_df.customer_id,
        customers_df.customer_name,
        customers_df.city
    ) \
    .agg(
        count("*").alias("total_transactions"),
        sum("amount").alias("total_spent"),
        avg("amount").alias("avg_transaction_amount"),
        min("amount").alias("min_transaction"),
        max("amount").alias("max_transaction"),
        max("transaction_date").alias("last_transaction_date")
    ) \
    .withColumn("customer_segment",
        when(col("total_spent") > 50000000, "Premium")
        .when(col("total_spent") > 20000000, "Gold")
        .when(col("total_spent") > 5000000, "Silver")
        .otherwise("Standard")
    ) \
    .orderBy(col("total_spent").desc())

customer_behavior_path = f"{base_path}/gold/agg_customer_behavior"
customer_behavior_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(customer_behavior_path)

print(f"Saved: {customer_behavior_path}")
display(customer_behavior_df.limit(20))

# COMMAND ----------

# DBTITLE 1,Task 6: Ranking Function - Top Accounts
print("Task 6: Ranking Top Accounts by Balance")

from pyspark.sql.window import Window

window_spec = Window.orderBy(col("latest_balance").desc())

ranked_accounts_df = accounts_df \
    .join(customers_df, accounts_df.account_id == customers_df.account_id, "inner") \
    .select(
        accounts_df.account_id,
        customers_df.customer_name,
        accounts_df.latest_balance,
        accounts_df.account_type,
        accounts_df.branch_id
    ) \
    .withColumn("balance_rank", dense_rank().over(window_spec)) \
    .withColumn("balance_row_number", row_number().over(window_spec)) \
    .orderBy("balance_rank")

ranked_accounts_path = f"{base_path}/gold/ranked_accounts"
ranked_accounts_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(ranked_accounts_path)

print(f"Saved: {ranked_accounts_path}")
display(ranked_accounts_df.limit(10))

# COMMAND ----------

# DBTITLE 1,Task 7: Running Total per Account
print("Task 7: Running Total per Account")

from pyspark.sql.window import Window

window_spec_running = Window.partitionBy("account_id").orderBy("transaction_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)

running_total_df = transactions_df \
    .join(accounts_df, transactions_df.account_id == accounts_df.account_id, "inner") \
    .join(customers_df, accounts_df.account_id == customers_df.account_id, "inner") \
    .select(
        transactions_df.account_id,
        customers_df.customer_name,
        transactions_df.transaction_date,
        transactions_df.amount,
        transactions_df.transaction_type
    ) \
    .withColumn("running_total", sum("amount").over(window_spec_running)) \
    .withColumn("transaction_count", row_number().over(window_spec_running)) \
    .orderBy("account_id", "transaction_date")

running_total_path = f"{base_path}/gold/running_total_transactions"
running_total_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(running_total_path)

print(f"Saved: {running_total_path}")
display(running_total_df.filter(col("account_id") == running_total_df.select("account_id").first()[0]).limit(20))

# COMMAND ----------

# DBTITLE 1,Task 8: Group By Analytics
print("Task 8: Group By Analytics\n")

# 1. Total amount by transaction_type
print("1. Amount by Transaction Type")
amount_by_type_df = transactions_df \
    .groupBy("transaction_type") \
    .agg(
        count("*").alias("total_transactions"),
        sum("amount").alias("total_amount"),
        avg("amount").alias("avg_amount"),
        min("amount").alias("min_amount"),
        max("amount").alias("max_amount")
    ) \
    .orderBy(col("total_amount").desc())

amount_by_type_path = f"{base_path}/gold/agg_amount_by_transaction_type"
amount_by_type_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(amount_by_type_path)
print(f"Saved: {amount_by_type_path}")
display(amount_by_type_df)

# 2. Transactions per branch
print("\n2. Transactions per Branch")
transactions_by_branch_df = transactions_df \
    .join(accounts_df, "account_id", "inner") \
    .join(branches_df, accounts_df.branch_id == branches_df.branch_id, "inner") \
    .groupBy(
        branches_df.branch_id,
        branches_df.branch_name,
        branches_df.city
    ) \
    .agg(
        count("*").alias("total_transactions"),
        sum("amount").alias("total_amount"),
        countDistinct(transactions_df.account_id).alias("unique_accounts")
    ) \
    .orderBy(col("total_transactions").desc())

transactions_by_branch_path = f"{base_path}/gold/agg_transactions_by_branch"
transactions_by_branch_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(transactions_by_branch_path)
print(f"Saved: {transactions_by_branch_path}")
display(transactions_by_branch_df)

# 3. Customers per city
print("\n3. Customers per City")
customers_by_city_df = customers_df \
    .join(accounts_df, customers_df.account_id == accounts_df.account_id, "inner") \
    .groupBy(customers_df.city) \
    .agg(
        countDistinct(customers_df.customer_id).alias("total_customers"),
        count(accounts_df.account_id).alias("total_accounts"),
        avg(accounts_df.latest_balance).alias("avg_balance")
    ) \
    .withColumn("accounts_per_customer",
        round(col("total_accounts") / col("total_customers"), 2)
    ) \
    .orderBy(col("total_customers").desc())

customers_by_city_path = f"{base_path}/gold/agg_customers_by_city"
customers_by_city_df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(customers_by_city_path)
print(f"Saved: {customers_by_city_path}")
display(customers_by_city_df)

print("\n✅ All analytics completed")