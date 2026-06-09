from fastapi import FastAPI
from pydantic import BaseModel
from agents.data_agent import run_data_agent
from agents.analysis_agent import run_analysis_agent
from agents.prediction_agent import run_prediction_agent
from agents.alert_agent import run_alert_agent
from agents.action_agent import run_action_agent

app = FastAPI(title="CashSense AI", version="1.0.0")


class RunRequest(BaseModel):
    csv_path: str = "data/sample_transactions.csv"


@app.get("/")
def root():
    return {"status": "CashSense AI running", "agents": 5}


@app.post("/run")
def run_pipeline(req: RunRequest):
    """Run all 5 agents in sequence. Accepts csv_path in request body."""
    data = run_data_agent(req.csv_path)
    analysis = run_analysis_agent()
    predictions = run_prediction_agent()
    alerts = run_alert_agent()
    actions = run_action_agent()
    return {
        "data": data,
        "analysis": analysis,
        "predictions": predictions,
        "alerts": alerts,
        "actions": actions,
    }


@app.get("/analysis")
def get_analysis():
    return run_analysis_agent()


@app.get("/predictions")
def get_predictions():
    return run_prediction_agent()


@app.get("/alerts")
def get_alerts():
    return run_alert_agent()


@app.get("/actions")
def get_actions():
    return run_action_agent()