from pyspark.sql.functions import col, to_date
def cast_order_date(df):
    return df.withColumn(
        "Date",
        to_date(col("Date"),"MM-dd-yy")
    )