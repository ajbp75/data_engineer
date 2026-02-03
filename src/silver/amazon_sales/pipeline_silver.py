from src.silver.amazon_sales.nulls_ship import remove_nulls_ship
from src.silver.amazon_sales.courier_financial_rules import filter_valid_financial_rows
from src.silver.amazon_sales.cast_type import cast_order_date
from src.silver.amazon_sales.rename_columns import rename_columns

def pipeline_silver(df):

    df = remove_nulls_ship(df)
    df = filter_valid_financial_rows(df)
    df = cast_order_date(df)
    df = rename_columns(df)


    return df
