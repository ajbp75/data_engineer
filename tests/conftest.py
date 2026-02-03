import sys
from pathlib import Path
import pytest
from pyspark.sql import SparkSession

# 👉 adiciona src/ ao PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

@pytest.fixture(scope="session")
def spark():
    spark = (
        SparkSession.builder
        .master("local[1]")
        .appName("pytest-spark")
        .getOrCreate()
    )
    yield spark
    spark.stop()
