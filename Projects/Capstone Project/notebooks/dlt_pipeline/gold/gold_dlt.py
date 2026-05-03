import dlt
from pyspark.sql.functions import (
    col, sum, countDistinct, avg, current_timestamp,
    when, rank, lit, datediff, current_date
)
from pyspark.sql.window import Window


# =========================
# SALES SUMMARY (FINAL)
# =========================
@dlt.table(name="sales_summary", table_properties={"quality": "gold"})
def sales_summary():

    df = dlt.read("silver_sales")

    result = df.groupBy(
        "invoice_date", "region", "channel"
    ).agg(
        sum("quantity").alias("total_quantity"),
        sum("sales_value").alias("total_revenue"),
        countDistinct("invoice_id").alias("total_orders")
    )

    return result.withColumn("_processed_ts", current_timestamp())


# =========================
# SKU PERFORMANCE (FINAL)
# =========================
@dlt.table(name="sku_performance", table_properties={"quality": "gold"})
def sku_performance():

    df = dlt.read("silver_sales")

    total_sales = df.agg(sum("sales_value").alias("overall_revenue"))

    sku_df = df.groupBy(
        "sku_id", "product_category_name"
    ).agg(
        sum("quantity").alias("total_quantity"),
        sum("sales_value").alias("total_revenue")
    )

    result = sku_df.crossJoin(total_sales).withColumn(
        "revenue_share_percent",
        (col("total_revenue") / col("overall_revenue")) * 100
    )

    window_spec = Window.orderBy(col("total_revenue").desc())

    result = result.withColumn(
        "rank",
        rank().over(window_spec)
    )

    return result.withColumn("_processed_ts", current_timestamp())


# =========================
# DISTRIBUTOR PERFORMANCE (FINAL)
# =========================
@dlt.table(name="distributor_performance", table_properties={"quality": "gold"})
def distributor_performance():

    df = dlt.read("silver_sales")

    result = df.groupBy(
        "distributor_id", "region", "channel"
    ).agg(
        sum("sales_value").alias("total_sales"),
        countDistinct("invoice_id").alias("order_count"),
        sum("quantity").alias("total_quantity")
    )

    # ⚠️ Approximation due to missing ordered vs delivered dataset
    result = result.withColumn(
        "approx_fill_rate",
        col("total_quantity") / col("order_count")
    )

    window_spec = Window.orderBy(col("total_sales").desc())

    result = result.withColumn(
        "rank",
        rank().over(window_spec)
    )

    return result.withColumn("_processed_ts", current_timestamp())


# =========================
# INVENTORY SNAPSHOT (FINAL)
# =========================
@dlt.table(name="inventory_snapshot", table_properties={"quality": "gold"})
def inventory_snapshot():

    df = dlt.read("silver_sales")

    result = df.groupBy(
        "sku_id", "distributor_id"
    ).agg(
        sum("quantity").alias("estimated_stock")  # ⚠️ simulated
    )

    result = result.withColumn(
        "stockout_flag",
        when(col("estimated_stock") == 0, 1).otherwise(0)
    ).withColumn(
        "overstock_flag",
        when(col("estimated_stock") > 100, 1).otherwise(0)
    )

    return result.withColumn("_processed_ts", current_timestamp())


# =========================
# STOCK AGING (FINAL)
# =========================
@dlt.table(name="stock_aging", table_properties={"quality": "gold"})
def stock_aging():

    df = dlt.read("silver_sales")

    df = df.withColumn(
        "stock_age_days",
        datediff(current_date(), col("invoice_date"))
    )

    result = df.groupBy(
        "sku_id", "distributor_id"
    ).agg(
        sum("quantity").alias("qty_at_risk"),
        avg("stock_age_days").alias("avg_stock_age")
    )

    result = result.withColumn(
        "stock_age_bucket",
        when(col("avg_stock_age") < 30, "<30")
        .when((col("avg_stock_age") >= 30) & (col("avg_stock_age") < 60), "30-60")
        .when((col("avg_stock_age") >= 60) & (col("avg_stock_age") < 90), "60-90")
        .otherwise("90+")
    )

    return result.withColumn("_processed_ts", current_timestamp())