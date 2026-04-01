#Business Pipeline Exercises
########### 1. Read sales data -> clean nulls -> calculate daily sales

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Read data
sales = spark.read.option("header","true").csv("/samples/sales.csv")

# Cast correct column
sales = sales.withColumn("total_amount", col("total_amount").cast("double"))

# Clean data
sales = sales.dropna()

# Calculate daily sales
daily_sales = sales.groupBy("sale_date") \
    .agg(sum("total_amount").alias("daily_sales"))

daily_sales.show()

########### 2. Read customer data -> clean invalid rows -> city-wise revenue
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Read customers
customers = spark.read.option("header","true").csv("/samples/customers.csv")

# Clean customers (no age column)
customers = customers.dropna()

# Read sales
sales = spark.read.option("header","true").csv("/samples/sales.csv")

# Clean sales
sales = sales.withColumn("total_amount", col("total_amount").cast("double"))
sales = sales.dropna()

# Join
joined_df = customers.join(sales, "customer_id")

# City-wise revenue
city_revenue = joined_df.groupBy("city") \
    .agg(sum("total_amount").alias("total_revenue"))

city_revenue.show()

############# 3. Find repeat customers (>2 orders)
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Read data
sales = spark.read.option("header","true").csv("/samples/sales.csv")

# Clean data
sales = sales.dropna()

# Count orders per customer
customer_orders = sales.groupBy("customer_id") \
    .agg(count("*").alias("order_count"))

# Filter repeat customers
repeat_customers = customer_orders.filter(col("order_count") > 1)

repeat_customers.show()

############### 4. Find highest spending customer in each city
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Read data
customers = spark.read.option("header","true").csv("/samples/customers.csv")
sales = spark.read.option("header","true").csv("/samples/sales.csv")

# Clean data
customers = customers.dropna()

sales = sales.withColumn("total_amount", col("total_amount").cast("double"))
sales = sales.dropna()

# Join
joined_df = customers.join(sales, "customer_id")

# Total spend per customer per city
customer_spend = joined_df.groupBy("city", "customer_id") \
    .agg(sum("total_amount").alias("total_spent"))

# Window function
window_spec = Window.partitionBy("city").orderBy(col("total_spent").desc())

ranked_df = customer_spend.withColumn("rank", rank().over(window_spec))

# Top customers
top_customers = ranked_df.filter(col("rank") == 1)

top_customers.show()

############ 5. Build final reporting table with customer, city, total spend, order count
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

# Read data
customers = spark.read.option("header","true").csv("/samples/customers.csv")
sales = spark.read.option("header","true").csv("/samples/sales.csv")

# Clean data
customers = customers.dropna()

sales = sales.withColumn("total_amount", col("total_amount").cast("double"))
sales = sales.dropna()

# Join
joined_df = customers.join(sales, "customer_id")

# Final reporting table
final_report = joined_df.groupBy("customer_id", "city") \
    .agg(
        sum("total_amount").alias("total_spend"),
        count("*").alias("order_count")
    )

# Output
final_report.show()
