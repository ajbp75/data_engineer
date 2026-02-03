from bronze.amazon_sales.job_bronze import run
def test_bronze_pipeline_e2e(spark, tmp_path):
    input_path = tmp_path / "input"
    output_path = tmp_path / "output"

    # dado de entrada realista
    spark.createDataFrame(
        [
            # evento válido
            ("123", "Delivered", "04-30-22", "400081.0"),
            # duplicação técnica
            ("123", "Delivered", "04-30-22", "400081.0"),

            # evento real (status diferente)
            ("123", "Canceled", "05-01-22", "400081.0"),

            # evento real (mesmo status, date diferente)
            ("123", "Delivered", "05-02-22", "400081.0"),

            # evento inválido (date inválida)
            ("124", "Delivered", "2022-04-30", "400082.0"),

            # evento inválido (date nula)
            ("125", "Canceled", None, "400083.0"),
        ],
        ["Order ID", "Status", "Date", "ship-postal-code"]
    ).write.csv(str(input_path), header=True)

    # executa o SISTEMA (não função interna)
    run(spark, str(input_path), str(output_path))

    result = spark.read.parquet(str(output_path))
    rows = result.collect()

    # apenas eventos válidos e únicos
    assert len(rows) == 3

    keys = {(r["Order ID"], r["Status"], r["Date"]) for r in rows}

    assert (123, "Delivered", "04-30-22") in keys
    assert (123, "Canceled", "05-01-22") in keys
    assert (123, "Delivered", "05-02-22") in keys

    # payload preservado
    assert all(r["ship-postal-code"].isdigit() for r in rows)
