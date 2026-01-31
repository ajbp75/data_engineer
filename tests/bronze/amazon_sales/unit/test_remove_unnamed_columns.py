def test_remove_unnamed_columns(spark):
    df = spark.createDataFrame(
        [(1,"A")],
        ["Order ID", "Unnamed: 22"]
        )

    from src.bronze.amazon_sales.remove_unnamed_columns import remove_cols_unnamed
        
    result = remove_cols_unnamed(df)

    assert "Unnamed: 22" not in result.columns
    assert "Order ID" in result.columns
    