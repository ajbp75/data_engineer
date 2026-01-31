import pytest

def test_fail_when_date_format_is_invalid(spark):
        
    df = spark.createDataFrame(
        [
            ("123", "Delivered", "04-30-22"),   # válido
            ("124", "Canceled", "2022-04-30"), # inválido (YYYY-MM-DD)
            ("125", "Delivered", None),         # inválido (nulo)
            ("126", "Delivered", "13-40-22"),   # inválido (data impossível)
        ],
        ["Order ID", "Status", "Date"]
    )

    from src.bronze.amazon_sales.validation_date import validade_date_format

    result = validade_date_format(df)
    rows = result.collect()

    assert len(rows) == 1
    assert rows[0]["Order ID"] == "123"