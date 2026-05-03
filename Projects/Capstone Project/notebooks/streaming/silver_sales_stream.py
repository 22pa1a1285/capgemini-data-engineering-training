import dlt
from pyspark.sql.functions import col, current_timestamp, to_timestamp

@dlt.table(name="silver_sales_stream")
def silver_sales_stream():

    orders = spark.readStream.table("fmcg.bronze.orders_raw_stream")
    items = spark.read.table("fmcg.bronze.order_items_raw_stream")
    payments = spark.read.table("fmcg.bronze.payments_raw_stream")

    df = orders.join(items, "order_id") \
               .join(payments, "order_id", "left")

    df = df.withColumn("price_double", col("price").cast("double"))

    df = df.filter(
        col("order_id").isNotNull() &
        col("customer_id").isNotNull() &
        col("product_id").isNotNull() &
        col("price_double").isNotNull() &
        (col("price_double") > 0)
    )

    df = df.withColumn(
        "invoice_date",
        to_timestamp("order_purchase_timestamp")
    )

    return df.select(
        col("order_id").alias("invoice_id"),
        col("customer_id").alias("retailer_id"),
        col("product_id").alias("sku_id"),
        col("price_double").alias("sales_value"),
        col("payment_value").cast("double"),
        "invoice_date"
    ).withColumn("_processed_ts", current_timestamp())