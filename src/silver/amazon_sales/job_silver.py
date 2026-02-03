from pyspark.sql import SparkSession
from src.silver.amazon_sales.pipeline_silver import pipeline_silver

def run(spark: SparkSession, input_path: str, output_path: str):
    df_bronze = (spark.read
              .option("header","True")
              .option("inferSchema",True)
              .parquet(input_path)
              )
    
    df_silver = pipeline_silver(df_bronze)

    df_silver.write.mode("overwrite").parquet(output_path)

def main():
    spark = (
        SparkSession.builder
        .appName("silver-amazon-sales")
        .getOrCreate()
    )

    # boundary com o mundo externo
    input_path = "data/bronze/bronze_amazon_sales.parquet"
    output_path = "data/silver/silver_amazon_sales.parquet"

    run(spark, input_path, output_path)

    spark.stop()

if __name__ == "__main__":
    main()