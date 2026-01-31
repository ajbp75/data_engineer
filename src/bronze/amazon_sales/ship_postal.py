from pyspark.sql import functions as F

def normalize_postal_code(df):
    return (
        df.withColumn(
            "ship-postal-code",
            F.regexp_replace(F.col("ship-postal-code"), r"\.0$", "")
        )
    )
