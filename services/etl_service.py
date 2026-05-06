import pandas as pd

def process_transactions(data: list):
    df = pd.DataFrame(data)

    # Drop duplicates
    df = df.drop_duplicates(subset="transaction_id")

    # Drop nulls
    df = df.dropna()

    # Filter failed
    df = df[df["status"] != "failed"]

    # Normalize timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df.to_dict(orient="records")