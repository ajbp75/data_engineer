from pyspark.sql import functions as F

def validade_date_format(df):
    return (
        df
        .withColumn(
            "_parsed_date",
            F.expr("try_to_date(Date, 'MM-dd-yy')")
        )
        .filter(F.col("_parsed_date").isNotNull())
        .drop("_parsed_date")
    )