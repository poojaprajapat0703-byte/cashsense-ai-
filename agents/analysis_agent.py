from mcp.mongodb_connector import fetch_transactions
from collections import defaultdict

def run_analysis_agent() -> dict:
    transactions = fetch_transactions()
    
    late_payers = []
    spending_by_category = defaultdict(float)
    monthly_cash = defaultdict(float)

    for t in transactions:
        amount = t["amount"]
        category = t["category"]
        month = t["date"][:7]
        spending_by_category[category] += amount
        monthly_cash[month] += amount

        if category == "income" and amount > 0:
            late_payers.append(t["description"])

    result = {
        "spending_by_category": dict(spending_by_category),
        "monthly_cash_flow": dict(sorted(monthly_cash.items())),
        "income_sources": list(set(late_payers)),
    }

    return result

if __name__ == "__main__":
    result = run_analysis_agent()
    for k, v in result.items():
        print(f"\n{k}:")
        print(v)