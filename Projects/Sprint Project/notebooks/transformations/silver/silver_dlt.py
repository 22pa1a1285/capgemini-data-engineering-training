import dlt
from pyspark.sql.functions import (
    col, current_timestamp, lower, lit, when,
    trim, upper, current_date, struct, coalesce
)


# =========================
# REGION LOOKUP
# =========================
@dlt.table(name="region_lookup", table_properties={"quality": "silver"})
def region_lookup():
    data = [
        ("SP", "SOUTHEAST"), ("RJ", "SOUTHEAST"), ("MG", "SOUTHEAST"), ("ES", "SOUTHEAST"),
        ("RS", "SOUTH"), ("SC", "SOUTH"), ("PR", "SOUTH"),
        ("BA", "NORTHEAST"), ("PE", "NORTHEAST"), ("CE", "NORTHEAST"),
        ("AM", "NORTH"), ("PA", "NORTH"),
        ("GO", "CENTRAL-WEST"), ("DF", "CENTRAL-WEST")
    ]
    return spark.createDataFrame(data, ["state", "region"])


# =========================
# QUARANTINE TABLE
# =========================
@dlt.table(name="quarantine_sales", table_properties={"quality": "silver"})
def quarantine_sales():

    o = dlt.read("orders_raw").alias("o")
    i = dlt.read("order_items_raw").alias("i")
    p = dlt.read("payments_raw").alias("p")

    df = o.join(i, "order_id") \
          .join(p, "order_id", "left")

    df = df.select(
        col("o.order_id"),
        col("o.customer_id"),
        col("o.order_purchase_timestamp"),
        col("i.product_id"),
        col("i.seller_id"),
        col("i.price"),
        col("i.freight_value"),
        col("p.payment_type"),
        col("p.payment_value"),
        col("o._ingest_ts"),
        col("o._source_file"),
        col("o._source_system"),
        col("o._batch_id")
    )

    df = df.toDF(*[c.strip().lower().replace(" ", "_") for c in df.columns])

    invalid_df = df.filter(
        (col("price") <= 0) |
        col("order_purchase_timestamp").isNull() |
        (col("order_purchase_timestamp") > current_date())
    )

    return invalid_df.select(
        struct(*invalid_df.columns).alias("record"),
        when(col("price") <= 0, "invalid_price")
        .when(col("order_purchase_timestamp").isNull(), "missing_date")
        .otherwise("future_date").alias("failure_reason"),
        current_timestamp().alias("ingest_ts")
    )


# =========================
# MONITORING TABLE
# =========================
@dlt.table(name="quarantine_monitoring", table_properties={"quality": "silver"})
def quarantine_monitoring():
    return dlt.read("quarantine_sales") \
        .withColumn("_batch_id", lit("batch_001")) \
        .groupBy("_batch_id") \
        .count()


# =========================
# SILVER FACT TABLE
# =========================
@dlt.table(
    name="silver_sales",
    table_properties={
        "quality": "silver",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true"
    }
)
def silver_sales():

    # =========================
    # SOURCE TABLES
    # =========================
    o = dlt.read("orders_raw")
    i = dlt.read("order_items_raw")
    p = dlt.read("payments_raw")

    customers = dlt.read("customer_master")
    products = dlt.read("product_master")
    sellers = dlt.read("seller_master")
    regions = dlt.read("region_lookup")

    # =========================
    # CORE JOIN (FIRST)
    # =========================
    df = o.join(i, "order_id") \
          .join(p, "order_id", "left")

    # =========================
    # DIMENSION ENRICHMENT (EARLY FIX)
    # =========================
    df = df.join(
    customers,
    col("customer_id") == col("retailer_id"),
    "left"
).join(
    products,
    col("product_id") == col("sku_id"),
    "left"
).join(
    sellers,
    col("seller_id") == col("distributor_id"),
    "left"
)

    # =========================
    # SELECT CLEAN SCHEMA
    # =========================
    df = df.select(
        "order_id",
        "customer_id",
        "seller_id",
        "product_id",
        "order_purchase_timestamp",
        "price",
        "freight_value",
        "payment_type",
        "payment_value",
        "retailer_city",
        "retailer_state",
        "distributor_city",
        "distributor_state",
        "product_category_name"
    )

    df = df.toDF(*[c.strip().lower().replace(" ", "_") for c in df.columns])

    # =========================
    # STANDARDIZATION
    # =========================
    df = df.withColumn("payment_type", lower(trim(col("payment_type"))))

    # =========================
    # DERIVED FIELDS
    # =========================
    # NOTE: dataset does not contain quantity → assumed = 1
    df = df.withColumn("quantity", lit(1)) \
           .withColumn("net_amount", col("price")) \
           .withColumn("sales_value", col("quantity") * col("net_amount"))

    # =========================
    # VALIDATION
    # =========================
    df = df.filter(
        (col("price") > 0) &
        col("order_purchase_timestamp").isNotNull() &
        (col("order_purchase_timestamp") <= current_date())
    )

    # =========================
    # DEDUPLICATION
    # =========================
    df = df.dropDuplicates(["order_id", "product_id"])

    # =========================
    # REGION ENRICHMENT
    # =========================
    df = df.join(regions, col("distributor_state") == col("state"), "left")

    df = df.withColumn(
        "region",
        upper(coalesce(col("region"), lit("UNKNOWN")))
    )

    # =========================
    # CHANNEL LOGIC
    # =========================
    # NOTE: simplified logic due to lack of channel column
    df = df.withColumn(
        "channel",
        when(col("distributor_state").isin("SP", "RJ"), "MT")
        .otherwise("GT")
    )

    # =========================
    # FINAL SELECT
    # =========================
    final_df = df.select(
        col("order_id").alias("invoice_id"),
        col("seller_id").alias("distributor_id"),
        col("customer_id").alias("retailer_id"),
        col("product_id").alias("sku_id"),
        col("order_purchase_timestamp").alias("invoice_date"),
        "quantity",
        "net_amount",
        "sales_value",
        "freight_value",
        "payment_type",
        "payment_value",
        "channel",
        "region",
        "product_category_name",
        "retailer_city",
        "retailer_state",
        "distributor_city",
        "distributor_state"
    )

    return final_df.withColumn("processing_date", current_timestamp())