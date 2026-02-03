def remove_nulls_ship(df):
    cols = ["ship-city","ship-state","ship-country"]
    return df.dropna(subset=cols)