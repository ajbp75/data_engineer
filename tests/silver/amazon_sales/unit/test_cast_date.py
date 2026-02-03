from silver.amazon_sales.cast_type import cast_order_date
from pyspark.sql.types import DateType

def test_cast_order_date(spark):
    df = spark.createDataFrame([
        ("04-30-22",),
        ("05-02-22",)
    ],["Date"])

    result = cast_order_date(df)
    assert isinstance(result.schema["Date"].dataType, DateType)