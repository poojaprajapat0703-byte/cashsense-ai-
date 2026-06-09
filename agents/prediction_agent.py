from mcp.mongodb_connector import fetch_transactions, upsert_prediction
from collections import defaultdict
from datetime import datetime, timedelta

def run_prediction_agent() -> list[dict]:
    transactions = fetch_transactions()
    
    monthly_cash = defaultdict(float)
    for t in transactions:
        month = t["date"][:7]
        monthly_cash[month] += t["amount"]

    months = sorted(monthly_cash.keys())
    values = [monthly_cash[m] for m in months]

    avg = sum(values) / len(values)
    trend = (values[-1] - values[0]) / len(values)

    predictions = []
    last_date = datetime.strptime(months[-1], "%Y-%m")

    for i in range(1, 4):
        future_date = last_date + timedelta(days=30 * i)
        forecast_month = future_date.strftime("%Y-%m")
        predicted_cash = avg + (trend * i)
        crisis = predicted_cash < 20000

        pred = {
            "forecast_date": forecast_month,
            "predicted_cash": round(predicted_cash, 2),
            "crisis_risk": crisis,
            "days_ahead": i * 30
        }
        predictions.append(pred)
        upsert_prediction(pred)

    return predictions

if __name__ == "__main__":
    preds = run_prediction_agent()
    for p in preds:
        print(p)