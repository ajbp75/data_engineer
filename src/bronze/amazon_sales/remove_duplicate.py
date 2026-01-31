def drop_rows_with_duplicate(df):
    return df.dropDuplicates(["Order ID", "Status","Date"])

