import os
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi

load_dotenv(dotenv_path=r"C:\Users\dell\Desktop\cashsense-ai\.env")

_client = None

def get_db():
    global _client
    if _client is None:
        uri = os.getenv("MONGODB_URI")
        _client = MongoClient(uri, tlsCAFile=certifi.where())
    return _client["cashsense"]

def get_collection(name: str):
    return get_db()[name]

def insert_transactions(transactions: list[dict]) -> int:
    col = get_collection("transactions")
    if not transactions:
        return 0
    result = col.insert_many(transactions)
    return len(result.inserted_ids)

def fetch_transactions(limit: int = 500) -> list[dict]:
    col = get_collection("transactions")
    return list(col.find({}, {"_id": 0}).sort("date", -1).limit(limit))

def upsert_prediction(prediction: dict):
    col = get_collection("predictions")
    col.update_one(
        {"forecast_date": prediction["forecast_date"]},
        {"$set": prediction},
        upsert=True
    )

def fetch_predictions() -> list[dict]:
    col = get_collection("predictions")
    return list(col.find({}, {"_id": 0}).sort("forecast_date", 1))