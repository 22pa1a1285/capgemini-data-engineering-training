
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# ------------------------------------------------------------
# INIT SPARK
# ------------------------------------------------------------
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------
customers = spark.read.option("header","true").csv("/samples/customers.csv")
sales = spark.read.option("header","true").csv("/samples/sales.csv")

# ------------------------------------------------------------
# CLEANING FUNCTION
# ------------------------------------------------------------
def clean_data(customers, sales):

    # Remove nulls
    customers = customers.dropna(subset=["customer_id"])
    sales = sales.dropna(subset=["customer_id", "total_amount"])

    # Remove duplicates
    customers = customers.dropDuplicates()
    sales = sales.dropDuplicates()

    # Fix data types
    customers = customers.withColumn("customer_id", F.col("customer_id").cast("int"))

    sales = sales.withColumn("customer_id", F.col("customer_id").cast("int")) \
                 .withColumn("total_amount", F.col("total_amount").cast("double"))

    # Remove invalid values
    sales = sales.filter(
        (F.col("total_amount") >= 0) & 
        (F.col("customer_id").isNotNull())
    )

    return customers, sales


# ------------------------------------------------------------
# APPLY CLEANING
# ------------------------------------------------------------
customers_clean, sales_clean = clean_data(customers, sales)

# ------------------------------------------------------------
# JOIN DATA
# ------------------------------------------------------------
df = sales_clean.join(customers_clean, on="customer_id", how="inner")

# Fix date column
df = df.withColumn("sale_date", F.to_date("sale_date"))

# ------------------------------------------------------------
# TASK 1: Daily Sales → (date, total_sales)
# ------------------------------------------------------------
daily_sales = df.groupBy("sale_date") \
    .agg(F.sum("total_amount").alias("total_sales")) \
    .orderBy("sale_date")

print("=== Daily Sales ===")
daily_sales.show()

# ------------------------------------------------------------
# TASK 2: City-wise Revenue → (city, total_revenue)
# ------------------------------------------------------------
city_revenue = df.groupBy("city") \
    .agg(F.sum("total_amount").alias("total_revenue")) \
    .orderBy(F.desc("total_revenue"))

print("=== City-wise Revenue ===")
city_revenue.show()

# ------------------------------------------------------------
# TASK 3: Top 5 Customers → (customer_name, total_spend)
# ------------------------------------------------------------
top_customers = df.withColumn(
        "customer_name",
        F.concat(F.col("first_name"), F.lit(" "), F.col("last_name"))
    ) \
    .groupBy("customer_name") \
    .agg(F.sum("total_amount").alias("total_spend")) \
    .orderBy(F.desc("total_spend")) \
    .limit(5)

print("=== Top 5 Customers ===")
top_customers.show()

# ------------------------------------------------------------
# TASK 4: Repeat Customers (>1 order)
# ------------------------------------------------------------
repeat_customers = df.groupBy("customer_id") \
    .agg(F.count("*").alias("order_count")) \
    .filter(F.col("order_count") > 1)

print("=== Repeat Customers ===")
repeat_customers.show()

# ------------------------------------------------------------
# TASK 5: Customer Segmentation
# ------------------------------------------------------------
customer_spend = df.groupBy("customer_id") \
    .agg(F.sum("total_amount").alias("total_spend"))

customer_segment = customer_spend.withColumn(
    "segment",
    F.when(F.col("total_spend") > 10000, "Gold")
     .when((F.col("total_spend") >= 5000) & (F.col("total_spend") <= 10000), "Silver")
     .otherwise("Bronze")
)

print("=== Customer Segmentation ===")
customer_segment.show()

# ------------------------------------------------------------
# TASK 6: Final Reporting Table
# ------------------------------------------------------------

final_df = customer_segment \
    .join(repeat_customers, on="customer_id", how="left") \
    .join(customers_clean, on="customer_id", how="left") \
    .withColumn(
        "customer_name",
        F.concat(F.col("first_name"), F.lit(" "), F.col("last_name"))
    ) \
    .select(
        "customer_name",
        "city",
        "total_spend",
        "order_count",
        "segment"
    )

final_df.show()

# ------------------------------------------------------------
# TASK 7: Save Output
# ------------------------------------------------------------
final_df.write.mode("overwrite").option("header","true").csv("/tmp/report")
