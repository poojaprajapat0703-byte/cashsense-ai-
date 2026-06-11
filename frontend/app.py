import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
import time
import re
import os

API = "http://127.0.0.1:8001"

st.set_page_config(
    page_title="CashSense AI",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    font-family: 'Space Grotesk', sans-serif;
    background: #04060f;
    color: #e8eaf2;
}

.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(99,102,241,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,102,241,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 3rem 4rem 3rem !important; max-width: 1400px !important; }

.cs-hero { padding: 4rem 0 2.5rem; position: relative; }

.cs-eyebrow {
    display: inline-flex; align-items: center; gap: 8px;
    font-family: 'DM Mono', monospace; font-size: 0.7rem; font-weight: 500;
    letter-spacing: 3px; text-transform: uppercase; color: #6366f1;
    background: rgba(99,102,241,0.08); border: 1px solid rgba(99,102,241,0.2);
    border-radius: 100px; padding: 6px 14px; margin-bottom: 1.5rem;
}
.cs-eyebrow::before {
    content: ''; width: 6px; height: 6px; background: #6366f1;
    border-radius: 50%; animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.7); }
}

.cs-title {
    font-size: clamp(2.8rem, 5vw, 4.5rem); font-weight: 700;
    line-height: 1.05; letter-spacing: -1.5px; color: #f1f3ff; margin-bottom: 0.75rem;
}
.cs-title .accent {
    background: linear-gradient(120deg, #818cf8 0%, #c084fc 50%, #38bdf8 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.cs-subtitle {
    font-size: 1rem; color: #4b5280; font-weight: 400;
    letter-spacing: 0.3px; max-width: 480px; line-height: 1.7;
}

.stat-strip {
    display: flex; gap: 1px; background: rgba(255,255,255,0.04);
    border-radius: 16px; overflow: hidden; border: 1px solid rgba(255,255,255,0.06); margin: 2rem 0;
}
.stat-item {
    flex: 1; padding: 1.4rem 1.8rem; background: rgba(8,10,22,0.9);
    transition: background 0.2s; position: relative;
}
.stat-item:hover { background: rgba(99,102,241,0.06); }
.stat-item::after {
    content: ''; position: absolute; right: 0; top: 20%;
    height: 60%; width: 1px; background: rgba(255,255,255,0.05);
}
.stat-item:last-child::after { display: none; }
.stat-num { font-size: 1.9rem; font-weight: 700; color: #818cf8; font-variant-numeric: tabular-nums; letter-spacing: -1px; }
.stat-label { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: #3d4168; margin-top: 4px; }

[data-testid="stFileUploader"] {
    background: rgba(99,102,241,0.04) !important; border: 1.5px dashed rgba(99,102,241,0.25) !important;
    border-radius: 14px !important; padding: 1.2rem !important; transition: border-color 0.2s !important;
}
[data-testid="stFileUploader"]:hover { border-color: rgba(99,102,241,0.5) !important; }

div[data-testid="stButton"] button {
    font-family: 'Space Grotesk', sans-serif !important; font-weight: 600 !important;
    font-size: 0.85rem !important; letter-spacing: 0.3px !important; border-radius: 10px !important;
    padding: 0.65rem 1.8rem !important; border: none !important; cursor: pointer !important;
    transition: all 0.2s ease !important; width: 100% !important;
}
div[data-testid="stButton"]:nth-of-type(1) button {
    background: linear-gradient(135deg, #6366f1, #818cf8) !important;
    color: #fff !important; box-shadow: 0 4px 20px rgba(99,102,241,0.35) !important;
}
div[data-testid="stButton"]:nth-of-type(1) button:hover {
    box-shadow: 0 6px 28px rgba(99,102,241,0.55) !important; transform: translateY(-2px) !important;
}
div[data-testid="stButton"]:nth-of-type(2) button {
    background: rgba(56,189,248,0.08) !important; color: #38bdf8 !important;
    border: 1px solid rgba(56,189,248,0.25) !important;
}
div[data-testid="stButton"]:nth-of-type(2) button:hover {
    background: rgba(56,189,248,0.14) !important; border-color: rgba(56,189,248,0.5) !important; transform: translateY(-2px) !important;
}
div[data-testid="stButton"]:nth-of-type(3) button {
    background: rgba(192,132,252,0.08) !important; color: #c084fc !important;
    border: 1px solid rgba(192,132,252,0.25) !important;
}
div[data-testid="stButton"]:nth-of-type(3) button:hover {
    background: rgba(192,132,252,0.14) !important; border-color: rgba(192,132,252,0.5) !important; transform: translateY(-2px) !important;
}

.cs-section { display: flex; align-items: center; gap: 12px; margin: 2.5rem 0 1.2rem; }
.cs-section-line { flex: 1; height: 1px; background: linear-gradient(90deg, rgba(99,102,241,0.3), transparent); }
.cs-section-tag {
    font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 2px;
    text-transform: uppercase; color: #6366f1; background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.2); border-radius: 6px; padding: 4px 10px;
}
.cs-section-title { font-size: 1.25rem; font-weight: 600; color: #e8eaf2; letter-spacing: -0.3px; }

.banner-safe {
    background: linear-gradient(135deg, rgba(34,197,94,0.07), rgba(34,197,94,0.03));
    border: 1px solid rgba(34,197,94,0.25); border-left: 3px solid #22c55e;
    border-radius: 10px; padding: 1rem 1.4rem; display: flex; align-items: center;
    gap: 12px; font-size: 0.9rem; color: #86efac; margin: 0.6rem 0;
}
.banner-crisis {
    background: linear-gradient(135deg, rgba(239,68,68,0.08), rgba(239,68,68,0.03));
    border: 1px solid rgba(239,68,68,0.3); border-left: 3px solid #ef4444;
    border-radius: 10px; padding: 1rem 1.4rem; display: flex; align-items: center;
    gap: 12px; font-size: 0.9rem; color: #fca5a5; margin: 0.6rem 0;
}
.banner-info {
    background: rgba(99,102,241,0.06); border: 1px solid rgba(99,102,241,0.2);
    border-left: 3px solid #6366f1; border-radius: 10px; padding: 0.85rem 1.4rem;
    font-size: 0.85rem; color: #a5b4fc; margin: 0.4rem 0;
}

.rec-card {
    background: rgba(8,10,22,0.8); border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px; padding: 1.4rem 1.6rem; margin: 0.7rem 0;
    position: relative; overflow: hidden; transition: border-color 0.2s, transform 0.2s;
}
.rec-card::before {
    content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 100%;
    background: linear-gradient(180deg, #818cf8, #c084fc);
}
.rec-card:hover { border-color: rgba(99,102,241,0.3); transform: translateX(4px); }
.rec-num { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 2px; color: #3d4168; text-transform: uppercase; margin-bottom: 6px; }
.rec-text { font-size: 0.9rem; color: #c7cadd; line-height: 1.65; white-space: pre-wrap; }

.kpi-block {
    background: rgba(8,10,22,0.8); border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px; padding: 1.1rem 1.4rem; margin: 0.5rem 0;
    display: flex; justify-content: space-between; align-items: center;
}
.kpi-label { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 1.5px; text-transform: uppercase; color: #3d4168; }
.kpi-value { font-size: 1.15rem; font-weight: 600; color: #e8eaf2; font-variant-numeric: tabular-nums; }
.kpi-value.positive { color: #4ade80; }
.kpi-value.negative { color: #f87171; }

.cs-footer { text-align: center; padding: 2.5rem 0 1rem; border-top: 1px solid rgba(255,255,255,0.04); margin-top: 3rem; }
.cs-footer-text { font-family: 'DM Mono', monospace; font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: #2a2d48; }
.cs-footer-text span { color: #3d4168; }

[data-testid="stDataFrame"] { border-radius: 12px !important; overflow: hidden !important; border: 1px solid rgba(255,255,255,0.06) !important; }
[data-testid="stExpander"] { background: rgba(8,10,22,0.6) !important; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 10px !important; }
hr { border-color: rgba(255,255,255,0.05) !important; }
</style>
""", unsafe_allow_html=True)

# ══ HERO ══
st.markdown("""
<div class="cs-hero">
    <div class="cs-eyebrow">Agentic AI · Financial Intelligence</div>
    <h1 class="cs-title">CashSense <span class="accent">AI</span></h1>
    <p class="cs-subtitle">Five autonomous agents monitor your cash flow, forecast 90 days ahead, and surface crises before they happen.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stat-strip">
    <div class="stat-item"><div class="stat-num">5</div><div class="stat-label">AI Agents</div></div>
    <div class="stat-item"><div class="stat-num">90</div><div class="stat-label">Days Forecast</div></div>
    <div class="stat-item"><div class="stat-num">Real-time</div><div class="stat-label">Analysis</div></div>
    <div class="stat-item"><div class="stat-num">MongoDB</div><div class="stat-label">Persistence</div></div>
    <div class="stat-item"><div class="stat-num">LLaMA</div><div class="stat-label">Recommendations</div></div>
</div>
""", unsafe_allow_html=True)

# ══ UPLOAD ══
st.markdown("""
<div class="cs-section">
    <div class="cs-section-tag">Step 01</div>
    <div class="cs-section-title">Load Bank Statement</div>
    <div class="cs-section-line"></div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Drop your CSV here — columns: date, amount, category, description", type=["csv"])

csv_path = "data/sample_transactions.csv"

if uploaded_file is not None:
    os.makedirs("data", exist_ok=True)
    csv_path = "data/uploaded_transactions.csv"
    with open(csv_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✓ {uploaded_file.name}  ·  {uploaded_file.size // 1024} KB loaded")
    try:
        df_preview = pd.read_csv(csv_path)
        with st.expander("Preview data", expanded=False):
            st.dataframe(df_preview.head(10), use_container_width=True)
    except Exception:
        pass
else:
    st.markdown('<div class="banner-info">Using built-in sample_transactions.csv · Upload your own file above to analyse real data.</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ══ BUTTONS ══
st.markdown("""
<div class="cs-section">
    <div class="cs-section-tag">Step 02</div>
    <div class="cs-section-title">Run Agents</div>
    <div class="cs-section-line"></div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1: run_all = st.button("⚡  Run Full Pipeline")
with col2: run_analysis = st.button("◎  Spending Analysis")
with col3: run_predictions = st.button("◈  Forecast Only")

# ══ HELPERS ══
def api_post(endpoint, payload=None, timeout=180):
    try:
        resp = requests.post(f"{API}{endpoint}", json=payload or {}, timeout=timeout)
        resp.raise_for_status()
        return resp.json(), None
    except requests.exceptions.ConnectionError:
        return None, "Cannot connect to API — is FastAPI running?"
    except requests.exceptions.Timeout:
        return None, "Request timed out — try again, Render may be waking up."
    except requests.exceptions.HTTPError as e:
        return None, f"API error {e.response.status_code}: {e.response.text[:300]}"
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"

def api_get(endpoint, timeout=60):
    try:
        resp = requests.get(f"{API}{endpoint}", timeout=timeout)
        resp.raise_for_status()
        return resp.json(), None
    except requests.exceptions.ConnectionError:
        return None, "Cannot connect to API — is FastAPI running?"
    except Exception as e:
        return None, f"Error: {str(e)}"

PLOT_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Space Grotesk, sans-serif", color="#9499be", size=12),
    margin=dict(l=10, r=10, t=40, b=10),
    xaxis=dict(gridcolor="rgba(99,102,241,0.07)", zeroline=False, linecolor="rgba(255,255,255,0.05)"),
    yaxis=dict(gridcolor="rgba(99,102,241,0.07)", zeroline=False, linecolor="rgba(255,255,255,0.05)"),
    colorway=["#818cf8","#38bdf8","#c084fc","#4ade80","#fb923c"],
)

# ══ RENDERERS ══
def render_analysis(analysis: dict):
    st.markdown("""<div class="cs-section"><div class="cs-section-tag">Analysis</div><div class="cs-section-title">Spending Breakdown</div><div class="cs-section-line"></div></div>""", unsafe_allow_html=True)

    monthly = analysis.get("monthly_cash_flow", {})
    categories = analysis.get("spending_by_category", analysis.get("category_breakdown", {}))

    if monthly:
        # filter timestamp keys
        clean = {k: v for k, v in monthly.items() if str(k).count('-') == 1 and len(str(k)) <= 10}
        if not clean: clean = monthly
        months = list(clean.keys())
        values = [float(v) for v in clean.values()]
        bar_colors = ["#818cf8" if v >= 0 else "#f87171" for v in values]
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=months, y=values,
            marker=dict(color=bar_colors, line=dict(width=0), opacity=0.9),
            text=[f"₹{v:,.0f}" for v in values], textposition="outside",
            textfont=dict(size=11, color="#9499be"),
            hovertemplate="<b>%{x}</b><br>₹%{y:,.0f}<extra></extra>"
        ))
        fig.update_layout(**PLOT_BASE, title=dict(text="Monthly Cash Flow", font=dict(size=14, color="#c7cadd"), x=0), height=320, showlegend=False, bargap=0.35)
        st.plotly_chart(fig, use_container_width=True)

    if categories:
        col_chart, col_kpis = st.columns([1.4, 1])
        with col_chart:
            abs_vals = [abs(float(v)) for v in categories.values()]
            fig2 = go.Figure(go.Pie(
                labels=list(categories.keys()), values=abs_vals, hole=0.62,
                textinfo="label+percent", textfont=dict(family="Space Grotesk", size=11),
                marker=dict(colors=["#818cf8","#38bdf8","#c084fc","#4ade80","#fb923c","#f472b6"], line=dict(color="#04060f", width=3)),
                hovertemplate="<b>%{label}</b><br>₹%{value:,.0f}<extra></extra>"
            ))
            fig2.add_annotation(text="Spend Mix", x=0.5, y=0.5, font=dict(size=11, color="#4b5280", family="DM Mono"), showarrow=False)
            fig2.update_layout(**PLOT_BASE, title=dict(text="Category Distribution", font=dict(size=14, color="#c7cadd"), x=0), height=320, showlegend=True, legend=dict(font=dict(size=10, color="#6b7094"), bgcolor="rgba(0,0,0,0)"))
            st.plotly_chart(fig2, use_container_width=True)
        with col_kpis:
            cats = analysis.get("spending_by_category", {})
            total_in  = sum(v for v in cats.values() if v > 0)
            total_out = sum(v for v in cats.values() if v < 0)
            net       = total_in + total_out
            net_cls   = "positive" if net >= 0 else "negative"
            net_sym   = "↑" if net >= 0 else "↓"

            st.markdown(f"""
            <div style="margin-top:2.4rem;">
                <div class="kpi-block"><div class="kpi-label">Total Income</div><div class="kpi-value positive">₹{abs(total_in):,.0f}</div></div>
                <div class="kpi-block"><div class="kpi-label">Total Expenses</div><div class="kpi-value negative">₹{abs(total_out):,.0f}</div></div>
                <div class="kpi-block" style="border-color:rgba(99,102,241,0.2);"><div class="kpi-label">Net Cash Flow</div><div class="kpi-value {net_cls}">{net_sym} ₹{abs(net):,.0f}</div></div>
            </div>""", unsafe_allow_html=True)



def render_predictions(predictions):
    st.markdown("""<div class="cs-section"><div class="cs-section-tag">Forecast</div><div class="cs-section-title">90-Day Cash Flow Projection</div><div class="cs-section-line"></div></div>""", unsafe_allow_html=True)

    pred_list = predictions if isinstance(predictions, list) else predictions.get("predictions", [])
    if not pred_list:
        st.warning("No prediction data returned.")
        return

    # ── Simple 3 cards ──
    cols = st.columns(3)
    horizon_colors = ["#818cf8", "#f59e0b", "#ef4444"]
    labels = ["30 Days", "60 Days", "90 Days"]
    icons  = ["📅", "⚠️", "🚨"]

    for i, (col, pred) in enumerate(zip(cols, pred_list[:3])):
        risk   = pred.get("crisis_risk", False)
        amount = pred.get("predicted_cash", pred.get("predicted_balance", 0))
        days   = pred.get("days_ahead", labels[i])
        c      = horizon_colors[i]
        badge_color = "#f87171" if risk else "#4ade80"
        badge_bg    = "rgba(239,68,68,0.1)" if risk else "rgba(34,197,94,0.1)"
        badge_border= "rgba(239,68,68,0.3)" if risk else "rgba(34,197,94,0.3)"
        badge_txt   = "🚨 CRISIS RISK" if risk else "✅ HEALTHY"
        amount_color= "#f87171" if amount < 0 else "#4ade80"
        arrow       = "↓" if amount < 0 else "↑"

        col.markdown(f"""
        <div style="background:rgba(8,10,22,0.9);border:1px solid rgba(255,255,255,0.08);
                    border-top:3px solid {c};border-radius:16px;padding:2rem 1.5rem;
                    text-align:center;margin:0.5rem 0;">
            <div style="font-size:2rem;margin-bottom:0.5rem;">{icons[i]}</div>
            <div style="font-family:'DM Mono',monospace;font-size:0.65rem;letter-spacing:3px;
                        color:#3d4168;text-transform:uppercase;margin-bottom:0.8rem;">
                In {days} Days
            </div>
            <div style="font-size:2rem;font-weight:700;color:{amount_color};
                        font-variant-numeric:tabular-nums;letter-spacing:-1px;margin-bottom:0.8rem;">
                {arrow} ₹{abs(amount):,.0f}
            </div>
            <div style="display:inline-block;font-family:'DM Mono',monospace;font-size:0.65rem;
                        color:{badge_color};background:{badge_bg};border:1px solid {badge_border};
                        border-radius:20px;padding:4px 12px;letter-spacing:1px;">
                {badge_txt}
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Simple bar chart comparing 30/60/90 ──
    if pred_list:
        days_labels = [f"+{p.get('days_ahead', i*30)} days" for i, p in enumerate(pred_list[:3])]
        amounts     = [p.get("predicted_cash", p.get("predicted_balance", 0)) for p in pred_list[:3]]
        bar_colors  = ["#f87171" if a < 0 else "#818cf8" for a in amounts]

        fig = go.Figure(go.Bar(
            x=days_labels, y=amounts,
            marker=dict(color=bar_colors, line=dict(width=0), opacity=0.9),
            text=[f"₹{a:,.0f}" for a in amounts],
            textposition="outside",
            textfont=dict(size=13, color="#9499be"),
            hovertemplate="<b>%{x}</b><br>₹%{y:,.0f}<extra></extra>"
        ))
        fig.add_hline(y=0, line_color="rgba(239,68,68,0.4)", line_width=1.5, line_dash="dot",
                      annotation_text="₹0 — Bankruptcy Line",
                      annotation_font=dict(color="#ef4444", size=11, family="DM Mono"),
                      annotation_position="bottom right")
        fig.update_layout(
            **PLOT_BASE,
            title=dict(text="Predicted Cash Balance — 30 / 60 / 90 Days", font=dict(size=14, color="#c7cadd"), x=0),
            height=350, showlegend=False, bargap=0.4,
        )
        st.plotly_chart(fig, use_container_width=True)


def render_alerts(alerts):
    st.markdown("""<div class="cs-section"><div class="cs-section-tag">Monitoring</div><div class="cs-section-title">Crisis Alerts</div><div class="cs-section-line"></div></div>""", unsafe_allow_html=True)
    alert_list = alerts if isinstance(alerts, list) else alerts.get("alerts", [])
    if alert_list:
        for alert in alert_list:
            msg = alert.get("message", str(alert))
            st.markdown(f'<div class="banner-crisis">🚨 <strong>{msg}</strong></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="banner-safe"><span style="font-size:1.2rem;">✓</span><div><strong>No crisis detected</strong> &nbsp;·&nbsp; Cash balance is above the ₹25,000 safety threshold.</div></div>', unsafe_allow_html=True)


def render_actions(actions):
    st.markdown("""<div class="cs-section"><div class="cs-section-tag">Groq · LLaMA</div><div class="cs-section-title">AI Recommendations</div><div class="cs-section-line"></div></div>""", unsafe_allow_html=True)

    # Get raw value
    raw = (
        actions if isinstance(actions, list) else
        actions.get("recommendations") or
        actions.get("actions") or
        actions.get("cost_cuts") or
        actions.get("suggestions") or
        ""
    )

    # If it's a single long string — split by numbered points
    if isinstance(raw, str) and raw.strip():
        parts = re.split(r'\n\s*\d+[\.\)]\s+', raw)
        parts = [p.strip() for p in parts if len(p.strip()) > 10]
        rec_list = parts if len(parts) > 1 else [raw.strip()]
    elif isinstance(raw, list):
        rec_list = raw
    else:
        rec_list = []

    if not rec_list:
        st.markdown('<div class="banner-info">No recommendations returned.</div>', unsafe_allow_html=True)
        st.json(actions)
        return

    for i, rec in enumerate(rec_list[:3], 1):
        if isinstance(rec, dict):
            text = rec.get("action") or rec.get("recommendation") or rec.get("text") or str(rec)
        else:
            text = str(rec)
        st.markdown(f"""
        <div class="rec-card">
            <div class="rec-num">Recommendation {i:02d}</div>
            <div class="rec-text">{text}</div>
        </div>""", unsafe_allow_html=True)


# ══ RUN LOGIC ══
if run_all:
    with st.spinner("Running all 5 agents — this takes ~30–60s…"):
        progress = st.progress(0, text="Initialising pipeline…")
        progress.progress(10, text="Data agent reading CSV…")
        result, err = api_post("/run", {"csv_path": csv_path}, timeout=180)
        if err:
            st.error(err)
        else:
            progress.progress(100, text="All agents complete.")
            time.sleep(0.4)
            progress.empty()
            st.success("✅ Pipeline complete — all 5 agents ran successfully.")
            if "analysis" in result: render_analysis(result["analysis"])
            if "predictions" in result: render_predictions(result["predictions"])
            if "alerts" in result: render_alerts(result["alerts"])
            if "actions" in result: render_actions(result["actions"])
            with st.expander("Raw API response", expanded=False):
                st.json(result)

if run_analysis:
    with st.spinner("Running spending analysis agent…"):
        result, err = api_get("/analysis", timeout=60)
        if err: st.error(err)
        else: render_analysis(result)

if run_predictions:
    with st.spinner("Running forecast agent…"):
        result, err = api_get("/predictions", timeout=60)
        if err: st.error(err)
        else:
            render_predictions(result)
            alert_result, _ = api_get("/alerts", timeout=30)
            if alert_result: render_alerts(alert_result)

# ══ FOOTER ══
st.markdown("""
<div class="cs-footer">
    <div class="cs-footer-text">CashSense AI &nbsp;·&nbsp; <span>Google Cloud Rapid Agent Hackathon 2026</span> &nbsp;·&nbsp; MongoDB Track</div>
</div>
""", unsafe_allow_html=True)