import pandas as pd
from mcp.mongodb_connector import insert_transactions, get_collection


def run_data_agent(csv_path: str) -> dict:
    # Clear old data first — fresh start every run
    get_collection("transactions").delete_many({})
    get_collection("predictions").delete_many({})

    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df["amount"] = df["amount"].astype(float)
    transactions = df.to_dict(orient="records")
    inserted = insert_transactions(transactions)
    return {"status": "ok", "inserted": inserted}

if __name__ == "__main__":
    result = run_data_agent("data/sample_transactions.csv")
    print(result)