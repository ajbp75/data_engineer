from bronze.amazon_sales.pipeline_bronze import pipeline_bronze
def test_pipeline_bronze(spark):
    df = spark.createDataFrame(
        [
            ("123", "Delivered", "04-30-22", "400081.0"),
            # duplicação técnica (mesmo Order, Status, Date)
            ("123", "Delivered", "04-30-22", "400081.0"),
            # evento real: mesmo pedido, status diferente
            ("123", "Canceled", "05-01-22", "400081.0"),
            # evento real: mesmo pedido, mesma status, date diferente
            ("123", "Delivered", "05-02-22", "400081.0"),
            # evento inválido (date inválida)
            ("124", "Delivered", "2022-04-30", "400082.0"),
            # evento inválido (date nula)
            ("125", "Canceled", None, "400083.0"),

        ], ["Order ID", "Status", "Date", "ship-postal-code"]
    )

    result = pipeline_bronze(df)
    rows = result.collect()

    assert len(rows) == 3
    
    keys = {(r["Order ID"], r["Status"], r["Date"]) for r in rows}
    assert ("123", "Delivered", "04-30-22") in keys
    assert ("123", "Canceled", "05-01-22") in keys
    assert ("123", "Delivered", "05-02-22") in keys
    
    assert any(r["ship-postal-code"] == "400081" for r in rows)