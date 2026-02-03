from bronze.amazon_sales.remove_duplicate import drop_rows_with_duplicate


def test_remove_duplicate_order_id_status_and_date(spark):
    df = spark.createDataFrame(
        [
            # duplicação técnica (mesmo Order, Status, Date)
            ("123", "Delivered", "04-30-22"),
            ("123", "Delivered", "04-30-22"),

            # evento real (mesmo pedido e status, date diferente)
            ("123", "Delivered", "05-02-22"),

            # outro pedido
            ("124", "Canceled", "04-30-22"),
        ],
        ["Order ID", "Status", "Date"]
    )

    result = drop_rows_with_duplicate(df)
    rows = result.collect()

    assert len(rows) == 3

    keys = {(r["Order ID"], r["Status"], r["Date"]) for r in rows}

    assert ("123", "Delivered", "04-30-22") in keys
    assert ("123", "Delivered", "05-02-22") in keys
    assert ("124", "Canceled", "04-30-22") in keys
