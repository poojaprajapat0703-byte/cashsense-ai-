from mcp.mongodb_connector import fetch_predictions

def run_alert_agent(threshold: float = 25000) -> list[dict]:
    predictions = fetch_predictions()
    alerts = []

    for p in predictions:
        if p["predicted_cash"] < threshold:
            alert = {
                "forecast_date": p["forecast_date"],
                "predicted_cash": p["predicted_cash"],
                "days_ahead": p["days_ahead"],
                "message": f"WARNING: Cash crisis in {p['days_ahead']} days! Expected balance: Rs {p['predicted_cash']:,.0f}"
            }
            alerts.append(alert)

    if not alerts:
        print("No crisis detected. Cash flow looks healthy.")
    else:
        for a in alerts:
            print(a["message"])

    return alerts

if __name__ == "__main__":
    run_alert_agent()