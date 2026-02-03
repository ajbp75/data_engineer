from silver.amazon_sales.courier_financial_rules import filter_valid_financial_rows

def test_courier_financial_rules(spark):
    df = spark.createDataFrame(
        [
            ("Cancelled",None, None),
            (None,"INR",708.66),
            (None, None, None),
            ("Cancelled","INR", None),
            ("Cancelled",None, 500.23),
            (None, "USD", None),
            (None, None, 100.0),
            ("Delivered", "USD", 100.0),
            
        ],
        ["Courier Status","currency","Amount"]
    )

    result = filter_valid_financial_rows(df)
    rows = result.collect()

    assert len(rows)==2
