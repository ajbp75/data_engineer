from pyspark.sql import SparkSession
from src.bronze.amazon_sales.pipeline_bronze import pipeline_bronze

def run(spark: SparkSession, input_path: str, output_path: str):
    df_raw = (spark.read
              .option("header","True")
              .option("inferSchema",True)
              .csv(input_path)
              )
    
    df_bronze = pipeline_bronze(df_raw)

    df_bronze.write.mode("overwrite").parquet(output_path)

def main():
    spark = (
        SparkSession.builder
        .appName("bronze-amazon-sales")
        .getOrCreate()
    )

    # boundary com o mundo externo
    input_path = "raw/Amazon Sale Report.csv"
    output_path = "data/bronze/bronze_amazon_sales.parquet"

    run(spark, input_path, output_path)

    spark.stop()

if __name__ == "__main__":
    main()