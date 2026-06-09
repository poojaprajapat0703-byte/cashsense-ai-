import os
from groq import Groq
from mcp.mongodb_connector import fetch_predictions, fetch_transactions

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
client = Groq(api_key=GROQ_API_KEY)

def run_action_agent() -> dict:
    predictions = fetch_predictions()
    transactions = fetch_transactions()

    crisis_months = [p for p in predictions if p["predicted_cash"] < 25000]

    if not crisis_months:
        return {"status": "no_crisis", "actions": ""}

    spending = {}
    for t in transactions:
        cat = t["category"]
        spending[cat] = spending.get(cat, 0) + t["amount"]

    prompt = f"""
You are a financial advisor for a small business.

Cash flow predictions show a crisis coming:
{crisis_months}

Current spending by category:
{spending}

Give exactly 3 specific actions:
1. A payment reminder email draft to a late client
2. One expense to cut immediately
3. One way to bridge the cash gap

Be specific and concise.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "status": "crisis_detected",
        "crisis_months": crisis_months,
        "actions": response.choices[0].message.content
    }

if __name__ == "__main__":
    result = run_action_agent()
    print(result["status"])
    print("\n--- AI Recommendations ---")
    print(result["actions"])