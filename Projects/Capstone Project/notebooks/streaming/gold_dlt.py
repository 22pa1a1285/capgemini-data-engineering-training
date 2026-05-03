import dlt
from pyspark.sql.functions import (
    col, sum, countDistinct, avg,
    to_date, current_timestamp
)

# =========================
# SALES SUMMARY
# =========================
@dlt.table(name="sales_summary", table_properties={"quality": "gold"})
def sales_summary():

    df = spark.read.table("fmcg.silver.silver_sales_stream")

    return df.groupBy(
        to_date("invoice_date").alias("sales_date")
    ).agg(
        sum("sales_value").alias("total_sales"),
        countDistinct("invoice_id").alias("total_orders"),
        avg("sales_value").alias("avg_order_value")
    ).withColumn("_processed_ts", current_timestamp())


# =========================
# SKU PERFORMANCE
# =========================
@dlt.table(name="sku_performance", table_properties={"quality": "gold"})
def sku_performance():

    df = spark.read.table("fmcg.silver.silver_sales_stream")

    return df.groupBy("sku_id").agg(
        sum("sales_value").alias("total_sales"),
        countDistinct("invoice_id").alias("total_orders")
    ).withColumn("_processed_ts", current_timestamp())


# =========================
# DISTRIBUTOR PERFORMANCE
# =========================
@dlt.table(name="distributor_performance", table_properties={"quality": "gold"})
def distributor_performance():

    df = spark.read.table("fmcg.silver.silver_sales_stream")

    return df.groupBy("retailer_id").agg(
        sum("sales_value").alias("total_sales"),
        countDistinct("invoice_id").alias("total_orders")
    ).withColumn("_processed_ts", current_timestamp())


# =========================
# PAYMENT SUMMARY
# =========================
@dlt.table(name="payment_summary", table_properties={"quality": "gold"})
def payment_summary():

    df = spark.read.table("fmcg.silver.silver_sales_stream")

    return df.groupBy("payment_value").agg(
        countDistinct("invoice_id").alias("transactions")
    ).withColumn("_processed_ts", current_timestamp())


# =========================
# INVENTORY SNAPSHOT
# =========================
@dlt.table(name="inventory_snapshot", table_properties={"quality": "gold"})
def inventory_snapshot():

    df = spark.read.table("fmcg.silver.silver_sales_stream")

    return df.groupBy("sku_id").agg(
        sum("sales_value").alias("stock_value")
    ).withColumn("_processed_ts", current_timestamp())