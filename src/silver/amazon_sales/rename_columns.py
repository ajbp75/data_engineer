def rename_columns(df):
    column_mapping = {
        "index": "row_index",
        "Order ID": "order_id",
        "Date": "order_date",
        "Status": "order_status",
        "Courier Status": "courier_status",
        "Fulfilment": "fulfillment_type",
        "fulfilled-by": "fulfilled_by",
        "Sales Channel ": "sales_channel",
        "B2B": "is_b2b",
        "Style": "product_style",
        "SKU": "sku",
        "ASIN": "asin",
        "Category": "product_category",
        "Size": "product_size",
        "ship-service-level": "ship_service_level",
        "ship-city": "ship_city",
        "ship-state": "ship_state",
        "ship-postal-code": "ship_postal_code",
        "ship-country": "ship_country",
        "Qty": "quantity",
        "currency": "currency",
        "Amount": "amount",
        "promotion-ids": "promotion_ids",
    }

    for old, new in column_mapping.items():
        if old in df.columns:
            df = df.withColumnRenamed(old, new)

    return df
