from pyspark.sql.functions import col

def filter_valid_financial_rows(df):
       
    """
    Aplica regras de consistência entre courier_status e campos financeiros.

    Regras válidas:
    1) courier_status == 'Cancelled' AND currency IS NULL AND amount IS NULL
    2) courier_status IS NULL AND currency IS NOT NULL AND amount IS NOT NULL

    Qualquer outro cenário é considerado inválido e removido.
    """ 

    rule_cancelled = (
        (col("Courier Status") == "Cancelled") &
        col("currency").isNull() &
        col("Amount").isNull()
    )

    rule_not_cancelled = (
        col("Courier Status").isNull() &
        col("currency").isNotNull() &
        col("Amount").isNotNull()
    )

    return df.filter(rule_cancelled | rule_not_cancelled)