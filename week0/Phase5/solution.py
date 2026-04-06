# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# ------------------------------------------------------------
# TASK 1: Top 3 Customers per City
# ------------------------------------------------------------

# Join payments with orders to get customer_id
payments_orders = payments.join(orders, "order_id")

# Total spend per customer
customer_spend = payments_orders.groupBy("customer_id") \
    .agg(sum("payment_value").alias("total_spend"))

# Join with customers to get city
customer_city_spend = customer_spend.join(customers, "customer_id") \
    .select("customer_city", "customer_id", "total_spend")

# Window function for ranking
window_city = Window.partitionBy("customer_city") \
    .orderBy(col("total_spend").desc())

# Top 3 customers per city
top_customers_per_city = customer_city_spend \
    .withColumn("rank", rank().over(window_city)) \
    .filter(col("rank") <= 3)

display(top_customers_per_city)


# ------------------------------------------------------------
# TASK 2: Running Total of Sales
# ------------------------------------------------------------

# Join orders with payments
orders_payments = orders.join(payments, "order_id")

# Extract date
orders_payments = orders_payments.withColumn(
    "order_date",
    to_date("order_purchase_timestamp")
)

# Daily sales
daily_sales = orders_payments.groupBy("order_date") \
    .agg(sum("payment_value").alias("daily_sales"))

# Window for running total
window_date = Window.orderBy("order_date") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Running total
daily_sales_running = daily_sales.withColumn(
    "running_total",
    sum("daily_sales").over(window_date)
)

display(daily_sales_running)


# ------------------------------------------------------------
# TASK 3: Top Products per Category
# ------------------------------------------------------------

# Total sales per product
product_sales = order_items.groupBy("product_id") \
    .agg(sum("price").alias("total_sales"))

# Join with products
product_with_category = product_sales.join(products, "product_id")

# Join with category translation
product_category = product_with_category.join(
    category_translation,
    "product_category_name"
).select(
    col("product_category_name_english").alias("category"),
    "product_id",
    "total_sales"
)

# Window function
window_category = Window.partitionBy("category") \
    .orderBy(col("total_sales").desc())

# Ranking
top_products_per_category = product_category \
    .withColumn("rank", dense_rank().over(window_category)) \
    .filter(col("rank") <= 3)

display(top_products_per_category)


# ------------------------------------------------------------
# TASK 4: Customer Lifetime Value (CLV)
# ------------------------------------------------------------

# Total spend per customer
customer_lifetime = orders_payments.groupBy("customer_id") \
    .agg(sum("payment_value").alias("customer_lifetime_value"))

display(customer_lifetime)


# ------------------------------------------------------------
# TASK 5: Customer Segmentation
# ------------------------------------------------------------

customer_segmented = customer_lifetime.withColumn(
    "segment",
    when(col("customer_lifetime_value") > 10000, "Gold")
    .when(col("customer_lifetime_value").between(5000, 10000), "Silver")
    .otherwise("Bronze")
)

display(customer_segmented)


# ------------------------------------------------------------
# FINAL REPORT
# ------------------------------------------------------------

# Total orders per customer
customer_orders = orders.groupBy("customer_id") \
    .agg(count("order_id").alias("total_orders"))

# Final dataset
final_report = customer_segmented \
    .join(customers, "customer_id") \
    .join(customer_orders, "customer_id") \
    .select(
        "customer_id",
        col("customer_city").alias("city"),
        col("customer_lifetime_value").alias("total_spend"),
        "segment",
        "total_orders"
    )

display(final_report)
