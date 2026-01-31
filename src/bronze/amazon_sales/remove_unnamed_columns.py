
def remove_cols_unnamed(df):
    cols = [c for c in df.columns if not c.startswith("Unnamed")]
    return df.select(cols)
