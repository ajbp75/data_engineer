from src.bronze.amazon_sales.remove_duplicate import drop_rows_with_duplicate
from src.bronze.amazon_sales.remove_nulls import drop_rows_with_nulls
from src.bronze.amazon_sales.remove_unnamed_columns import remove_cols_unnamed
from src.bronze.amazon_sales.ship_postal import normalize_postal_code
from src.bronze.amazon_sales.validation_date import validade_date_format

def pipeline_bronze(df):
    df = remove_cols_unnamed(df)
    df = drop_rows_with_duplicate(df)
    df = drop_rows_with_nulls(df)
    df = validade_date_format(df)
    df = normalize_postal_code(df)

    return df
