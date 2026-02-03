from silver.amazon_sales.job_silver import run
def test_silver_pipeline_e2e(spark, tmp_path):
    input_path = tmp_path / "input"
    output_path = tmp_path / "output"

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
    ).write.parquet(str(input_path))

    # executa o SISTEMA (não função interna)
    run(spark, str(input_path), str(output_path))

    result = spark.read.parquet(str(output_path))
    rows = result.collect()

    # apenas eventos válidos e únicos
    assert len(rows) == 2
