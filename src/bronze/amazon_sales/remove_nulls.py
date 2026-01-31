def drop_rows_with_nulls(df, required_cols=None):
    required_cols = required_cols or ["Order ID", "Status"]
    return df.dropna(subset=required_cols)
