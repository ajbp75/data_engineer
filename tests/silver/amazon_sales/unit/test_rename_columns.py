from silver.amazon_sales.rename_columns import rename_columns

def test_rename_columns(spark):
    df = spark.createDataFrame(
        [(1, "123", "04-30-22")],
        ["index", "Order ID", "Date"]
    )

    result = rename_columns(df)

    assert "row_index" in result.columns
    assert "order_id" in result.columns
    assert "order_date" in result.columns
