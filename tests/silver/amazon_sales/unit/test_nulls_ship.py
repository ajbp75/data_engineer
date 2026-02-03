import pytest
from silver.amazon_sales.nulls_ship import remove_nulls_ship

def test_nulls_ship(spark):
    df = spark.createDataFrame(
        [
        ("HYDERABAD","TELANGANA","IN"),
        (None,"TELANGANA","IN"),
        ("HYDERABAD",None,"IN"),
        ("HYDERABAD","TELANGANA",None),],
        ["ship-city","ship-state","ship-country"]
        )

    result = remove_nulls_ship(df)
    rows = result.collect()

    assert len(rows) == 1