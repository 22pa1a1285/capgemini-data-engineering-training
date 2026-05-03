 from pyspark.sql.functions import current_timestamp, lit


# =========================
# METADATA FUNCTION (STRICT BRONZE SAFE)
# =========================
def add_metadata(df, source_file, source_system="ERP", batch_id=None):
    """
    Adds ingestion metadata WITHOUT modifying original schema.
    Bronze-safe (no transformation).
    """

    return (
        df
        .withColumn("_ingest_ts", current_timestamp())
        .withColumn("_source_file", lit(source_file))
        .withColumn("_source_system", lit(source_system))
        .withColumn("_batch_id", lit(batch_id if batch_id else "batch_001"))
    )