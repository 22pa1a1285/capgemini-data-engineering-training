
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.getOrCreate()

# =========================
# Dirty Customers Dataset
# =========================

customers_data = [
    (1, "John Doe", "john@example.com", "Hyderabad"),
    (2, "Alice ", "alice@example.com", "Chennai"),
    (3, None, "bob@example.com", "Bangalore"),        # NULL name
    (4, "David", None, "Mumbai"),                    # NULL email
    (5, "Eva", "eva@example.com", "Hyderabad"),
    (6, "Frank", "frank@example.com", "Delhi"),
]

customers = spark.createDataFrame(customers_data, ["customer_id", "name", "email", "city"])

# =========================
# Dirty Orders Dataset
# =========================

orders_data = [
    (101, 1, "2024-01-01", 1000),
    (102, 2, "2024-01-02", 2000),
    (103, 3, "2024-01-03", -500),     # INVALID negative value
    (104, 99, "2024-01-04", 1500),    # INVALID FK (customer_id 99)
    (105, 1, "2024-01-05", None),     # NULL amount
    (106, 5, "2024-01-06", 3000),
    (107, 5, "2024-01-07", 3000),     # duplicate-like record
]

orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "order_date", "amount"])

# =========================
# Convert date column
# =========================

orders = orders.withColumn("order_date", to_date(col("order_date")))


# Practice Set A: Join Drills
##  Inner join between orders and customers → Output valid records

inner_join_df = orders.join(customers, "customer_id", "inner")
display(inner_join_df)



## - Left join → identify null values
left_join_df = orders.join(customers, "customer_id", "left")
display(left_join_df)

## - Left_anti join → find invalid foreign keys

invalid_fk = orders.join(customers, "customer_id", "left_anti")
display(invalid_fk)

## - Compare row counts across joins

print("Orders count:", orders.count())
print("Inner join count:", inner_join_df.count())
print("Left join count:", left_join_df.count())
print("Invalid FK count:", invalid_fk.count())


# Practice Set B: Window Functions- Top 3 customers per city using ranking
## - Running total of sales

customer_spend = orders.groupBy("customer_id") \
    .agg(sum("amount").alias("total_spend"))

## - Rank customers by total spend

from pyspark.sql.window import Window

window_spec = Window.orderBy(col("total_spend").desc())

ranked_df = customer_spend.withColumn(
    "rank", rank().over(window_spec)
)

display(ranked_df)

## - Use LAG to find previous order

window_lag = Window.partitionBy("customer_id").orderBy("order_date")

lag_df = orders.withColumn(
    "prev_amount",
    lag("amount").over(window_lag)
)

display(lag_df)

# Practice Set C: Date Analysis
## - Extract month from date- Monthly sales aggregation
orders_month = orders.withColumn(
    "month", month("order_date")
)
## - Calculate difference between dates- Trend analysis by month

window_date = Window.orderBy("order_date")

date_diff_df = orders.withColumn(
    "prev_date", lag("order_date").over(window_date)
).withColumn(
    "date_diff",
    datediff(col("order_date"), col("prev_date"))
)

display(date_diff_df)

# Practice Set D: Timed Pipeline 
## Remove Invalid Orders
orders_clean = orders \
    .filter(col("amount") > 0) \
    .filter(col("amount").isNotNull())

## Validate FK
orders_valid = orders_clean.join(customers_clean, "customer_id", "inner")

## Remove Duplicates
orders_valid = orders_valid.dropDuplicates(["customer_id", "order_date", "amount"])

## Aggregation
final_agg = orders_valid.groupBy("customer_id", "city") \
    .agg(sum("amount").alias("total_sales"))

## Ranking
window_final = Window.partitionBy("city").orderBy(col("total_sales").desc())

final_output = final_agg.withColumn(
    "rank", rank().over(window_final)
)

## Save Output
final_output.write.mode("overwrite").saveAsTable("customer_sales_report")
