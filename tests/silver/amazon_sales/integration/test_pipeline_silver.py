from silver.amazon_sales.pipeline_silver import pipeline_silver
def test_pipeline_silver(spark):

    df = spark.createDataFrame(
        [
            ("Cancelled",None, None,"HYDERABAD","TELANGANA","IN","01-15-23"), #True
            (None,"INR",708.66,"HYDERABAD","TELANGANA","IN","01-15-23"), #True
            ("Cancelled",None, None,None,"TELANGANA","IN","01-15-23"), #False
            (None,"INR",708.66,None,"TELANGANA","IN","01-15-23"), #False
            ("Cancelled",None, None,"HYDERABAD",None,"IN","01-15-23"), #False
            (None,"INR",708.66,"HYDERABAD",None,"IN","01-15-23"), #False  
            ("Cancelled",None, None,"HYDERABAD","TELANGANA",None,"01-15-23"), #False
            (None,"INR",708.66,"HYDERABAD","TELANGANA",None,"01-15-23"), #False          
            (None, None, None,"HYDERABAD","TELANGANA","IN","01-15-23"), #false
            ("Cancelled","INR", None,"HYDERABAD","TELANGANA","IN","01-15-23"), #false
            ("Cancelled",None, 500.23,"HYDERABAD","TELANGANA","IN","01-15-23"), #false
            (None, "USD", None,"HYDERABAD","TELANGANA","IN","01-15-23"), #false
            (None, None, 100.0,"HYDERABAD","TELANGANA","IN","01-15-23"), #false
            ("Delivered", "USD", 100.0,"HYDERABAD","TELANGANA","IN","01-15-23"), #false
            
        ],
        ["Courier Status","currency","Amount","ship-city","ship-state","ship-country","Date"]
    )

    result = pipeline_silver(df)
    rows = result.collect()

    assert len(rows) == 2
