from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# ------------------------------------------------------------
# INIT SPARK
# ------------------------------------------------------------
spark = SparkSession.builder.appName('Business_Pipeline').getOrCreate()


# ------------------------------------------------------------
# STEP 1: EXTRACT
# ------------------------------------------------------------
def extract():
    customers = spark.read.option("header","true").csv("/samples/customers.csv")
    sales = spark.read.option("header","true").csv("/samples/sales.csv")
    return customers, sales


# ------------------------------------------------------------
# STEP 2: CLEAN
# ------------------------------------------------------------
def clean(customers, sales):
    # Clean customers
    customers = customers.dropna()

    # Clean sales
    sales = sales.withColumn("total_amount", col("total_amount").cast("double"))
    sales = sales.dropna()

    return customers, sales


# ------------------------------------------------------------
# STEP 3: TRANSFORM (JOIN)
# ------------------------------------------------------------
def transform(customers, sales):
    return customers.join(sales, "customer_id")


# ------------------------------------------------------------
# STEP 4: BUILD METRICS
# ------------------------------------------------------------
def build_metrics(df, sales):

    # 1. Daily Sales
    daily_sales = sales.groupBy("sale_date") \
        .agg(sum("total_amount").alias("daily_sales"))

    # 2. City-wise Revenue
    city_revenue = df.groupBy("city") \
        .agg(sum("total_amount").alias("total_revenue"))

    # 3. Repeat Customers (>2 orders)
    repeat_customers = sales.groupBy("customer_id") \
        .agg(count("*").alias("order_count")) \
        .filter(col("order_count") > 2)

    # 4. Highest spending customer per city
    spend = df.groupBy("city", "customer_id") \
        .agg(sum("total_amount").alias("total_spent"))

    window_spec = Window.partitionBy("city").orderBy(col("total_spent").desc())

    top_customers = spend.withColumn("rank", rank().over(window_spec)) \
        .filter(col("rank") == 1)

    # 5. Final Reporting Table
    final_report = df.groupBy("customer_id", "city") \
        .agg(
            sum("total_amount").alias("total_spent"),
            count("*").alias("order_count")
        )

    return daily_sales, city_revenue, repeat_customers, top_customers, final_report


# ------------------------------------------------------------
# STEP 5: LOAD (DISPLAY)
# ------------------------------------------------------------
def load(daily, city, repeat, top, final):

    print("\n=== Daily Sales ===")
    daily.show()

    print("\n=== City Revenue ===")
    city.show()

    print("\n=== Repeat Customers ===")
    repeat.show()

    print("\n=== Top Customers per City ===")
    top.show()

    print("\n=== Final Report ===")
    final.show()


# ------------------------------------------------------------
# MAIN PIPELINE
# ------------------------------------------------------------
def run_pipeline():
    customers, sales = extract()
    customers, sales = clean(customers, sales)
    df = transform(customers, sales)

    daily, city, repeat, top, final = build_metrics(df, sales)

    load(daily, city, repeat, top, final)


# ------------------------------------------------------------
# EXECUTE
# ------------------------------------------------------------
run_pipeline()
