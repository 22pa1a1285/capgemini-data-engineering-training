from pyspark.sql.functions import sum, col, dense_rank, rank, when, count, lit
from pyspark.sql.window import Window

# Load datasets
orders = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/workspace/default/phase5_practice/archive/orders.csv")
customers = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/workspace/default/phase5_practice/archive/customers.csv")
products = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/workspace/default/phase5_practice/archive/products.csv")
categories = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/workspace/default/phase5_practice/archive/categories.csv")

# Task 1: Top 3 Customers per City
customer_spend = orders.groupBy("customer_id").agg(sum("order_amount").alias("total_spend"))
customer_city_spend = customer_spend.join(customers, "customer_id").select("city", "customer_id", "total_spend")
window_city = Window.partitionBy("city").orderBy(col("total_spend").desc())
customer_city_ranked = customer_city_spend.withColumn("rank", rank().over(window_city)).filter(col("rank") <= 3)
display(customer_city_ranked)

# Task 2: Running Total of Sales
daily_sales = orders.groupBy("order_date").agg(sum("order_amount").alias("daily_sales"))
window_date = Window.orderBy("order_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
daily_sales_running = daily_sales.withColumn("running_total", sum("daily_sales").over(window_date))
display(daily_sales_running)

# Task 3: Top Products per Category
product_sales = orders.groupBy("product_id").agg(sum("order_amount").alias("total_sales"))
product_category = product_sales.join(products, "product_id").join(categories, "category_id").select("category", "product_id", "total_sales")
window_category = Window.partitionBy("category").orderBy(col("total_sales").desc())
product_category_ranked = product_category.withColumn("rank", dense_rank().over(window_category))
display(product_category_ranked)

# Task 4: Customer Lifetime Value
customer_lifetime = customer_spend.select("customer_id", "total_spend")
display(customer_lifetime)

# Task 5: Customer Segmentation
customer_segmented = customer_lifetime.withColumn(
    "segment",
    when(col("total_spend") > 10000, "Gold")
    .when((col("total_spend") >= 5000) & (col("total_spend") <= 10000), "Silver")
    .otherwise("Bronze")
)
display(customer_segmented.select("customer_id", "total_spend", "segment"))
segment_count = customer_segmented.groupBy("segment").agg(count("customer_id").alias("customer_count"))
display(segment_count)

# Task 6: Final Reporting Table
customer_orders = orders.groupBy("customer_id").agg(count("order_id").alias("total_order"))
final_report = customer_segmented.join(customers, "customer_id").join(customer_orders, "customer_id").select(
    "customer_id", "city", "total_spend", "segment", "total_order"
)
display(final_report)
