import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go
from utils.styles import apply_styles
from agents.prediction_model import NetworkAI
from agents.healing_agent import HealingAgent

# Initialize System
st.set_page_config(page_title="Sentinel AI | Global SOC", layout="wide")
apply_styles()
ai_engine = NetworkAI()
healer = HealingAgent()

# Session State for Logs
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 class='neon-blue'>SENTINEL AI</h1>", unsafe_allow_html=True)
    st.write("v4.0.2-Enterprise")
    menu = st.radio("CORE SYSTEMS", ["Global Overview", "Security & Threats", "Digital Twin Simulation", "AI RCA Engine"])
    st.markdown("---")
    st.subheader("System Health Score")
    st.write("🟢 98.2%")
    st.progress(98)

# --- HEADER ---
st.markdown(f"<h2 class='neon-blue'>{menu.upper()}</h2>", unsafe_allow_html=True)

# --- LOGIC: DATA GENERATION ---
cpu, ram, lat, loss = np.random.uniform(20, 40), np.random.uniform(30, 50), 12, 0.01
anomaly_status, conf = ai_engine.predict_failure([cpu/100, ram/100, lat/100, loss])

# --- DASHBOARD: OVERVIEW ---
if menu == "Global Overview":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Total Nodes", "1,240", "12 New")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Bandwidth", "4.2 Gbps", "-0.4%")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        color = "neon-green" if anomaly_status == 1 else "neon-red"
        st.markdown(f"AI Prediction: <span class='{color}'>{'STABLE' if anomaly_status == 1 else 'RISK'}</span>", unsafe_allow_html=True)
        st.write(f"Confidence: {conf:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Uptime", "99.999%", "Stable")
        st.markdown('</div>', unsafe_allow_html=True)

    # Live Topology Graph (Plotly)
    st.subheader("Global Network Topology")
    fig = go.Figure(go.Scattergeo(
        locationmode = 'USA-states',
        lon = [-74, -118, -87, -95], lat = [40, 34, 41, 29],
        mode = 'markers+lines',
        marker = dict(size = 10, color = 'cyan', symbol = 'circle'),
        line = dict(width = 2, color = 'rgba(59, 130, 246, 0.5)')
    ))
    fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', lakecolor='#030712'), 
                      margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Healing Feed
    st.subheader("Autonomous Healing Logs")
    if anomaly_status == -1:
        st.session_state.logs.append({"Time": time.strftime("%H:%M:%S"), "Event": "Latency Spike", "Action": healer.resolve_issue("Latency")})
    
    df_logs = pd.DataFrame(st.session_state.logs).tail(5)
    st.table(df_logs)

# --- DASHBOARD: SECURITY ---
elif menu == "Security & Threats":
    st.markdown('<div class="alarm-red" style="padding:10px; border-radius:10px; background:rgba(239, 68, 68, 0.1); border:1px solid red;">Active Scans: 1,042 | Threats Neutralized: 12</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("Threat Severity Heatmap")
        st.image("https://docs.microsoft.com/en-us/azure/sentinel/media/tutorial-reports-detect-threats/heatmap.png", use_container_width=True) # Mock heatmap
    with col2:
        st.subheader("AI Recommendations")
        st.info("💡 Recommendation: Rotate SSL Certificates for Node-4.")
        st.warning("⚠️ Warning: Unusual SSH attempts from 185.x.x.x")

# --- DASHBOARD: DIGITAL TWIN ---
elif menu == "Digital Twin Simulation":
    st.subheader("Virtual Environment Simulation")
    sim_type = st.selectbox("Select Failure Scenario", ["DDoS Attack", "Hardware Failure", "BGP Misconfiguration"])
    if st.button("RUN SIMULATION"):
        with st.status("Injecting Faults...", expanded=True) as status:
            time.sleep(1)
            st.write("AI Agent Analyzing Root Cause...")
            time.sleep(1)
            st.write(f"Self-Healing Agent: {healer.resolve_issue('DDoS')}")
            time.sleep(1)
            status.update(label="Simulation Success: System Restored", state="complete")
