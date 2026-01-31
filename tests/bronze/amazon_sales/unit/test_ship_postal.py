def test_ship_postal_code_remove_decimal_zero(spark):
    df = spark.createDataFrame(
    [
    ("123", "Delivered", "400081.0"),
    ("124", "Canceled", "300087.0"),
    ],
    ["Order ID", "Status", "ship-postal-code"]
    )


    from src.bronze.amazon_sales.ship_postal import normalize_postal_code


    result = normalize_postal_code(df)
    rows = result.collect()


    assert rows[0]["ship-postal-code"] == "400081"
    assert rows[1]["ship-postal-code"] == "300087"