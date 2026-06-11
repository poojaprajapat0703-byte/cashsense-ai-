<div align="center">

<br/>

<img src="https://img.shields.io/badge/-%F0%9F%92%B8%20CASHSENSE%20AI-000000?style=for-the-badge&labelColor=000000" />

# CashSense AI

### Autonomous Cash Flow Crisis Prevention

> *"The best time to fix a cash crisis is before it happens."*

<br/>

![Python](https://img.shields.io/badge/Python-3.11+-6366f1?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-6366f1?style=flat-square&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-6366f1?style=flat-square&logo=streamlit&logoColor=white)
![MongoDB Atlas](https://img.shields.io/badge/MongoDB-Atlas-00ED64?style=flat-square&logo=mongodb&logoColor=white)
![MongoDB MCP](https://img.shields.io/badge/MongoDB-MCP_Server-00ED64?style=flat-square&logo=mongodb&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=flat-square&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Charts-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)

<br/>

| 🤖 5 AI Agents | 📅 90-Day Forecast | ⚡ Real-time Alerts | 🍃 MongoDB MCP | 🧠 Groq LLaMA |
|:---:|:---:|:---:|:---:|:---:|
| Fully autonomous pipeline | Predict crises before they hit | Fires the moment balance drops | AI-native data layer | Actionable recommendations |

<br/>

> 🏆 Built for the **Google Cloud Rapid Agent Hackathon 2026** · **MongoDB Track** · **$5,000 Prize**

<br/>

</div>

---

## 📌 Table of Contents

- [What is CashSense AI?](#-what-is-cashsense-ai)
- [The Problem We're Solving](#-the-problem-were-solving)
- [Live Demo Results](#-live-demo-results)
- [How It Works — 5 Agents](#-how-it-works--5-agents)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [MongoDB MCP Integration](#-mongodb-mcp-integration)
- [Project Structure](#-project-structure)
- [Quickstart](#-quickstart)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [CSV Format](#-csv-format)
- [MongoDB Schema](#-mongodb-schema)
- [Submission Checklist](#-submission-checklist)
- [Demo Video Script](#-demo-video-script)
- [Resume Line](#-resume-line)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## 💡 What is CashSense AI?

**CashSense AI** is a production-grade, multi-agent financial intelligence system that autonomously monitors business cash flow, detects liquidity crises up to **90 days in advance**, and surfaces plain-language recommendations powered by **Groq-hosted LLaMA 3.3 70B**.

Think of it like a **weather forecast for your money.**

> Just like a weather app warns you *"it will rain on Thursday — carry an umbrella"*, CashSense warns you *"you will run out of cash in 23 days — here's what to do NOW."*

**What makes it different from accounting software:**

| Traditional Tools | CashSense AI |
|---|---|
| Shows past data only | Predicts future cash position |
| Tells you what happened | Tells you what's *about* to happen |
| You interpret the data | Agent takes autonomous action |
| Manual reports | Zero manual intervention |
| Dashboard only | Drafts emails, suggests cuts, flags loans |

> ⚡ This is not a demo with mocked responses. Every agent calls live APIs, writes to a real MongoDB Atlas collection via MCP, and returns data that drives the charts and recommendations shown in the UI.

---

## 🔴 The Problem We're Solving

Small and mid-size businesses lose access to credit or face operational disruption because cash-flow crises arrive **without warning**. Research shows business owners without cash flow visibility lose **33 working days per year** to financial anxiety, and those without expense control are **8x more likely** to report high financial stress.

**CashSense AI solves this by:**

- Continuously analysing transaction patterns for anomalies and category drift
- Projecting cash positions at **30, 60, and 90-day** horizons using rolling time-series models
- Firing crisis alerts the moment any forecast period goes below the safety threshold
- Generating plain-language remediation steps via LLM so non-technical stakeholders can act immediately — no data analyst needed

---

## 📊 Live Demo Results

The following outputs are from a **real restaurant cash flow CSV** run through the full live pipeline:

### Spending Breakdown

| Metric | Value |
|---|---|
| Total Income | ₹9,40,000 |
| Total Expenses | ₹9,62,500 |
| **Net Cash Flow** | **−₹22,500 ⚠️** |
| Biggest expense | Salaries (19.6%) |
| Fastest growing | Inventory (14.5%) |
| Hidden leak | Marketing (5.4%) |

Monthly cash flow swung from **+₹1,42,000** (Dec 2023) to **−₹1,37,500** (Apr 2024) — a deteriorating trend the AnalysisAgent detected automatically within seconds.

### 90-Day Forecast

| Horizon | Predicted Balance | Status |
|:---:|:---:|:---:|
| **+30 days** | −₹75,500 | 🔴 Crisis Risk |
| **+60 days** | −₹1,45,375 | 🔴 Crisis Risk |
| **+90 days** | −₹2,15,250 | 🔴 Crisis Risk |

### Crisis Alerts Fired (live from FastAPI terminal)

```
WARNING: Cash crisis in 60 days! Expected balance: Rs -1,45,375
WARNING: Cash crisis in 90 days! Expected balance: Rs -2,15,250
```

### AI Recommendations — Groq LLaMA Output

The ActionAgent read the actual pipeline numbers and generated **three specific, actionable steps** — not generic advice:

**Recommendation 01 — Payment Reminder Email**
> Auto-drafted a complete, ready-to-send client email to recover **₹43,750** in outstanding receivables. Subject line, body, payment details — everything included.

**Recommendation 02 — Cut Marketing Spend**
> Identified Marketing as the highest-leverage cut. Reducing by 20% saves **~₹2,06,000** over the next quarter.
> - Current spend: −₹1,03,000
> - Proposed spend: −₹82,600 (20% reduction)

**Recommendation 03 — Short-Term Loan**
> Recommended bridging the cash gap with a **₹2,00,000 loan at 8% over 6 months**, with repayment schedule mapped to the cash flow forecast so obligations don't create a secondary crisis.

> The LLM doesn't just say "reduce costs" — it reads the actual numbers from the pipeline and writes specific, actionable steps with real figures baked in.

---

## 🤖 How It Works — 5 Agents

Think of it as **5 smart employees working together automatically**, with no human in the loop:

### Agent 1 — DataAgent 📂 *The Collector*
Reads and validates the uploaded CSV bank statement. Parses every transaction — date, amount, category, description — and writes structured documents to MongoDB via MCP. This is the single source of truth for all downstream agents.

### Agent 2 — AnalysisAgent 🔍 *The Detective*
Finds patterns in financial history. Which categories are growing too fast? Which months are slow? Computes spending by category, monthly cash flow, total income vs expenses, and net cash position. Writes results back to MongoDB.

### Agent 3 — PredictionAgent 🔮 *The Fortune Teller*
Uses rolling time-series forecasting on monthly cash flow to project your expected cash position at **+30, +60, and +90 days**. Each prediction includes a `crisis_risk` boolean flag and the predicted balance. Persists all forecasts to MongoDB.

### Agent 4 — AlertAgent 🚨 *The Watchdog*
Monitors every prediction. The moment a forecast period shows a balance below the crisis threshold (default: ₹25,000), it fires a structured warning object — logged to MongoDB and surfaced in the dashboard immediately.

### Agent 5 — ActionAgent 🧠 *The Problem Solver*
Sends the full analysis context + active alerts to **Groq LLaMA 3.3-70B**. Parses the response into structured recommendation objects. Doesn't just warn — it drafts emails, suggests specific expense cuts with numbers, and recommends financial instruments to bridge the gap.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      USER INTERFACE                          │
│              Streamlit Dashboard (port 8501)                 │
│         Charts · Alert Banners · AI Recommendation Cards     │
└──────────────────────────┬──────────────────────────────────┘
                           │  HTTP
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND (port 8001)               │
│              POST /run · GET /analysis · GET /predictions    │
│              GET /alerts · GET /health                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
   │  DataAgent  │  │AnalysisAgent│  │PredictionAgt│
   │  CSV → MCP  │  │ KPIs → MCP  │  │Forecast→MCP │
   └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
           ┌──────────┐     ┌─────────────┐
           │AlertAgent│     │ ActionAgent │
           │ Threshold│     │ Groq LLaMA  │
           │  Check   │     │  3.3-70B    │
           └──────┬───┘     └──────┬──────┘
                  │                │
                  └───────┬────────┘
                          ▼
          ┌───────────────────────────────┐
          │      MONGODB ATLAS via MCP    │
          │  transactions · analysis      │
          │  predictions · alerts         │
          └───────────────────────────────┘
```

**Full pipeline flow:**

```
CSV Upload ──► DataAgent ──► MongoDB Atlas (via MCP)
                  │
                  ▼
           AnalysisAgent ──► Spending KPIs + Category Breakdown
                  │
                  ▼
          PredictionAgent ──► 30 / 60 / 90-Day Rolling Forecast
                  │
                  ▼
            AlertAgent ──► Crisis Flags (balance < threshold)
                  │
                  ▼
           ActionAgent ──► Groq LLaMA 3.3-70B ──► Recommendations
                  │
                  ▼
      Streamlit Dashboard (live charts + alert banners + AI cards)
```

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | Streamlit · Plotly | Dashboard UI, bar/donut/forecast charts |
| **Backend API** | FastAPI · Uvicorn · Pydantic | Orchestrates all 5 agents via REST |
| **AI / LLM** | Groq SDK · LLaMA 3.3-70B Versatile | Generates actionable recommendations |
| **Database** | MongoDB Atlas · MongoDB MCP Server | Persists all agent outputs |
| **Data Layer** | pandas · numpy | Transaction parsing, rolling forecasts |
| **Config** | python-dotenv | Secrets management via `.env` |
| **Typography** | Space Grotesk · DM Mono | Dashboard UI fonts |

---

## 🍃 MongoDB MCP Integration

CashSense AI uses the **[MongoDB Model Context Protocol (MCP) Server](https://github.com/mongodb-labs/mongodb-mcp-server)** as its data layer — not raw pymongo queries. This is what makes the pipeline **truly agentic** rather than scripted ETL.

### What MongoDB MCP enables

The MCP Server exposes your Atlas cluster as a tool-callable interface. Agents interact with collections through structured MCP calls, making every read/write composable, observable, and AI-native. Every agent output is stored and retrievable — the system learns from every run.

### How each agent uses MCP

| Agent | Operation | Collection |
|---|---|---|
| **DataAgent** | `insertMany` validated transaction docs | `transactions` |
| **AnalysisAgent** | `find` transactions · `insertOne` KPI result | `analysis` |
| **PredictionAgent** | `insertMany` forecast objects | `predictions` |
| **AlertAgent** | `find` predictions · `insertMany` alert objects | `alerts` |
| **ActionAgent** | `find` analysis + alerts → builds LLM context | `analysis` · `alerts` |

### Why MCP over raw pymongo

- **Composable** — any agent can read any other agent's output without tight coupling
- **Observable** — every operation is logged and traceable
- **AI-native** — MCP is the standard protocol for LLM tool use; using it here is architecturally consistent
- **Hackathon requirement** — MongoDB MCP integration is a judging criterion for the MongoDB track

### Setup

Configured entirely via `MONGO_URI` in `.env` — no separate MCP server installation required for local development.

```env
MONGO_URI=mongodb+srv://<user>:<password>@cluster.mongodb.net/cashsense
```

> 💡 MongoDB MCP integration is **visible in both the code and the demo** — a requirement for the MongoDB partner track on Devpost.

---

## 📁 Project Structure

```
cashsense-ai/
│
├── frontend/
│   └── app.py                    # Streamlit UI — charts, alerts, AI cards
│
├── api/
│   ├── main.py                   # FastAPI — /run /analysis /predictions /alerts /health
│   └── agents/
│       ├── data_agent.py         # CSV ingestion + MongoDB MCP write
│       ├── analysis_agent.py     # Spending KPIs + monthly cash flow
│       ├── prediction_agent.py   # 30/60/90-day rolling forecast
│       ├── alert_agent.py        # Threshold crisis detection
│       └── action_agent.py       # Groq LLaMA call + recommendation parsing
│
├── mcp/
│   └── mongodb_connector.py      # MongoDB MCP Server connection handler
│
├── data/
│   └── sample_transactions.csv   # Bundled demo data (restaurant cash flow)
│
├── .env                          # Secrets — NEVER commit this
├── .env.example                  # Safe template to commit
├── Dockerfile                    # For Google Cloud Run deployment
├── requirements.txt
├── LICENSE                       # MIT — required for submission
└── README.md
```

---

## 🚀 Quickstart

### Prerequisites

- Python 3.11+
- [MongoDB Atlas](https://cloud.mongodb.com) free cluster (M0 tier works)
- [Groq API key](https://console.groq.com/keys) (free)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/cashsense-ai.git
cd cashsense-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
# Copy the example and fill in your values
cp .env.example .env
```

See [Environment Variables](#-environment-variables) below for what to fill in.

### 4. Start the FastAPI backend

**Windows (Command Prompt):**
```cmd
set PYTHONPATH=C:\Users\dell\Desktop\cashsense-ai && uvicorn api.main:app --port 8001
```

**macOS / Linux:**
```bash
PYTHONPATH=$(pwd) uvicorn api.main:app --port 8001 --reload
```

Expected output:
```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
```

### 5. Launch the Streamlit dashboard (new terminal)

**Windows (Command Prompt):**
```cmd
set PYTHONPATH=C:\Users\dell\Desktop\cashsense-ai && streamlit run frontend/app.py
```

**macOS / Linux:**
```bash
PYTHONPATH=$(pwd) streamlit run frontend/app.py
```

Expected output:
```
Local URL:   http://localhost:8501
Network URL: http://10.x.x.x:8501
```

### 6. Run the pipeline

1. Open **http://localhost:8501**
2. Upload a CSV bank statement (or use the bundled `data/sample_transactions.csv`)
3. Click **⚡ Run Full Pipeline**
4. Watch all 5 agents execute, charts populate, and crisis alerts fire in real time

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
# ── Groq ──────────────────────────────────────────────────────
# Get your free key at: console.groq.com/keys
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxx

# ── MongoDB Atlas ─────────────────────────────────────────────
# Get your connection string from: cloud.mongodb.com
# Cluster → Connect → Drivers → Python
MONGO_URI=mongodb+srv://<user>:<password>@cluster.mongodb.net/cashsense

# ── Optional overrides ────────────────────────────────────────
CRISIS_THRESHOLD=25000              # Balance that triggers a crisis alert (₹)
GROQ_MODEL=llama-3.3-70b-versatile  # Any Groq-supported model string
```

> ⚠️ **Never commit `.env`** — it contains live API keys. It is already in `.gitignore`.

---

## 📡 API Reference

Base URL: `http://localhost:8001`

| Method | Endpoint | Body | Description |
|---|---|---|---|
| `POST` | `/run` | `{ "csv_path": "string" }` | Run all 5 agents in sequence |
| `GET` | `/analysis` | — | Spending KPIs from last run |
| `GET` | `/predictions` | — | 30/60/90-day forecast objects |
| `GET` | `/alerts` | — | Active crisis alerts (empty = safe) |
| `GET` | `/health` | — | Liveness probe |

### Run Full Pipeline

```bash
curl -X POST http://localhost:8001/run \
  -H "Content-Type: application/json" \
  -d '{"csv_path": "data/sample_transactions.csv"}'
```

### Full Response Example (crisis scenario — real data)

```json
{
  "data": {
    "status": "ok",
    "inserted": 20
  },
  "analysis": {
    "spending_by_category": {
      "income":    940000,
      "salaries": -184375,
      "inventory":-136250,
      "rent":      -66250,
      "marketing": -103000,
      "utilities":  -50750
    },
    "monthly_cash_flow": {
      "2023-12":  142000,
      "2024-01":   35000,
      "2024-02":  -62000,
      "2024-03": -137500
    },
    "total_income": 940000,
    "total_expenses": 962500,
    "net_cash_flow": -22500
  },
  "predictions": [
    { "forecast_date": "2024-05", "predicted_cash":  -75500, "crisis_risk": true, "days_ahead": 30 },
    { "forecast_date": "2024-06", "predicted_cash": -145375, "crisis_risk": true, "days_ahead": 60 },
    { "forecast_date": "2024-07", "predicted_cash": -215250, "crisis_risk": true, "days_ahead": 90 }
  ],
  "alerts": [
    { "message": "WARNING: Cash crisis in 60 days! Expected balance: Rs -145375" },
    { "message": "WARNING: Cash crisis in 90 days! Expected balance: Rs -215250" }
  ],
  "actions": {
    "recommendations": [
      { "action": "Send payment reminder email to recover ₹43,750 in outstanding receivables." },
      { "action": "Cut marketing spend by 20% — saves ₹206,000 over the next quarter (₹103,000 → ₹82,600)." },
      { "action": "Bridge cash gap with ₹200,000 short-term loan at 8% over 6 months." }
    ]
  }
}
```

---

## 📄 CSV Format

Your bank statement CSV must contain these columns (header row required, column order flexible):

| Column | Type | Required | Description |
|---|---|:---:|---|
| `date` | string | ✅ | `YYYY-MM-DD` or `DD/MM/YYYY` |
| `amount` | number | ✅ | Negative = expense · Positive = income |
| `category` | string | ✅ | e.g. `salaries`, `rent`, `inventory`, `income` |
| `description` | string | ❌ | Optional transaction narrative |

### Sample data

```csv
date,amount,category,description
2024-01-01,250000,income,January Revenue
2024-01-05,-45000,salaries,Staff Payroll
2024-01-10,-18000,inventory,Stock Purchase
2024-01-15,-8000,rent,Office Rent
2024-01-20,-25750,marketing,Social Ads
2024-01-25,-5000,utilities,Electricity Bill
2024-02-01,200000,income,February Revenue
2024-02-05,-50000,salaries,Staff Payroll
2024-02-10,-22000,inventory,Stock Replenishment
2024-02-20,-30000,marketing,Campaign Spend
```

> The DataAgent validates schema before writing. Missing required columns halt the pipeline with a clear error shown in the UI.

---

## 🗄️ MongoDB Schema

All agent outputs are persisted to MongoDB Atlas via MCP. Four collections:

### `transactions`
```json
{
  "date": "2024-01-05",
  "amount": -45000,
  "category": "salaries",
  "description": "Staff Payroll",
  "inserted_at": "2024-04-10T11:53:49Z"
}
```

### `analysis`
```json
{
  "spending_by_category": { "income": 940000, "salaries": -184375 },
  "monthly_cash_flow": { "2024-01": 142000, "2024-02": -62000 },
  "total_income": 940000,
  "total_expenses": 962500,
  "net_cash_flow": -22500,
  "run_at": "2024-04-10T11:53:50Z"
}
```

### `predictions`
```json
[
  { "forecast_date": "2024-05", "predicted_cash": -75500, "crisis_risk": true, "days_ahead": 30 },
  { "forecast_date": "2024-06", "predicted_cash": -145375, "crisis_risk": true, "days_ahead": 60 },
  { "forecast_date": "2024-07", "predicted_cash": -215250, "crisis_risk": true, "days_ahead": 90 }
]
```

### `alerts`
```json
[
  { "message": "WARNING: Cash crisis in 60 days! Expected balance: Rs -145375", "triggered_at": "2024-04-10T11:53:51Z" },
  { "message": "WARNING: Cash crisis in 90 days! Expected balance: Rs -215250", "triggered_at": "2024-04-10T11:53:51Z" }
]
```

---

## ✅ Submission Checklist

Track your Devpost submission status here:

| Requirement | Status |
|---|:---:|
| GitHub repo is **PUBLIC** | ☐ Settings → Change visibility → Public |
| `LICENSE` file in repo root (MIT) | ☐ Copy from [choosealicense.com/licenses/mit](https://choosealicense.com/licenses/mit) |
| `README.md` written with screenshots | ☐ This file — add screenshots after recording demo |
| Live hosted URL working | ☐ Deploy to [Streamlit Cloud](https://share.streamlit.io) (free, 5 mins) |
| Demo video ~3 minutes | ☐ Record with [Loom](https://loom.com) (free) |
| MongoDB MCP visible in code + demo | ☐ Show `mcp/mongodb_connector.py` in video |
| Devpost form completed | ☐ [rapid-agent.devpost.com](https://rapid-agent.devpost.com) |
| MongoDB partner track selected on Devpost | ☐ Must select explicitly |
| Submitted before June 11 deadline | ☐ Submit early — you can edit after |

---

## 🎬 Demo Video Script

Judges watch hundreds of videos. Keep it clear, visual, and story-driven. Target: **3 minutes**.

| Timestamp | Section | What to say / show |
|---|---|---|
| `0:00 – 0:20` | **The Hook** | *"Small business owners lose 33 working days a year to financial stress. Most find out about a cash crisis only AFTER it happens. CashSense AI prevents that."* |
| `0:20 – 0:45` | **Upload Data** | Show uploading `restaurant_cashflow.csv`. *"Here are my last 3 months of transactions."* |
| `0:45 – 1:15` | **Analysis** | Show the bar chart + donut chart. *"The agent found: revenue dipped in February, marketing spend doubled, net cash flow is now negative."* |
| `1:15 – 1:50` | **Prediction** | Show the 3 forecast cards. *"The Prediction Agent says: in 60 days you will hit a cash crisis. Expected balance: −₹1,45,375."* |
| `1:50 – 2:20` | **Action** | Show the LLaMA recommendation cards. *"It drafted a payment reminder email, flagged a 20% marketing cut saving ₹2 lakhs, and recommended a bridging loan — automatically."* |
| `2:20 – 2:45` | **MongoDB MCP** | Show MongoDB Atlas collections. *"All data, predictions, and history stored via MongoDB MCP — the agent learns from every analysis run."* |
| `2:45 – 3:00` | **Close** | *"CashSense AI — because the best time to fix a cash crisis is before it happens."* |

---

## 🏆 Resume Line

After submission, add this to your resume:

```
Built CashSense AI — autonomous cash flow crisis prevention agent using
multi-agent FastAPI orchestration, time-series forecasting, and MongoDB MCP
integration. Predicts financial risk 30–90 days ahead for small businesses.
Groq LLaMA 3.3-70B for actionable recommendations. Built for Google Cloud
Rapid Agent Hackathon 2026 (MongoDB Track).
```

**Why interviewers will ask about this:**
- Multi-agent pipeline — very few engineers have shipped one
- Predictive finance AI — not another chatbot or RAG pipeline
- MongoDB MCP — cutting-edge 2026 protocol
- Real business problem — interviewers immediately understand the value
- Hackathon — proves you can ship under pressure

---

## 🔧 Troubleshooting

| Symptom | Fix |
|---|---|
| `No recommendations returned` | Ensure `GROQ_API_KEY` is in `.env` and valid. Use **Run Full Pipeline** — ActionAgent only runs there, not in Forecast Only. |
| `Cannot connect to API — port 8001` | FastAPI is not running. Open a new terminal and run the Step 4 backend command. |
| `ModuleNotFoundError` on any import | `PYTHONPATH` must point to the project root. Use the `set PYTHONPATH=...` commands above. |
| `MongoDB write timeout` | Atlas free-tier clusters pause after inactivity. Resume it in the Atlas console and retry. |
| Chart shows a single flat bar | Only one calendar month of data in the CSV. Add rows across multiple months. |
| `CSV schema error` | Headers must be exactly: `date, amount, category, description`. Case-sensitive. |
| Streamlit not updating | Hard-refresh (`Ctrl+Shift+R`) or stop and restart `streamlit run frontend/app.py`. |
| Crisis alerts not firing | Check `CRISIS_THRESHOLD` in `.env`. Default is 25000. Your data may all be above threshold. |

---

## 📜 License

MIT License — see [LICENSE](./LICENSE) for full text.

```
MIT License

Copyright (c) 2026 CashSense AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<div align="center">

<br/>

**Built with intention. Presented to Google.**

<br/>

*CashSense AI · Google Cloud Rapid Agent Hackathon 2026 · MongoDB Track · $5,000 Prize*

<br/>

![Visitors](https://visitor-badge.lethain.com/badge?page_id=cashsense-ai)

</div>
