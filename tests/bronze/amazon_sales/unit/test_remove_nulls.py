import pytest

def test_fail_when_nulls_in_required_columns(spark):
    df = spark.createDataFrame(
    [
    (None, "Delivered"),
    ("123", None),
    ("124", "Canceled")
    ],
    ["Order ID", "Status"]
    )


    from src.bronze.amazon_sales.remove_nulls import drop_rows_with_nulls
    result = drop_rows_with_nulls(df)

    rows = result.collect()
    assert len(rows) == 1
    assert rows[0]["Order ID"] == "124"
