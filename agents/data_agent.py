import pandas as pd
from mcp.mongodb_connector import insert_transactions

def run_data_agent(csv_path: str) -> dict:
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df["amount"] = df["amount"].astype(float)
    transactions = df.to_dict(orient="records")
    inserted = insert_transactions(transactions)
    return {"status": "ok", "inserted": inserted}

if __name__ == "__main__":
    result = run_data_agent("data/sample_transactions.csv")
    print(result)