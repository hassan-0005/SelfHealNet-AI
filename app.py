import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="AI Self-Healing Network", layout="wide")

# Custom CSS for Cyber Security Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .status-healthy { color: #238636; font-weight: bold; }
    .status-attack { color: #f85149; font-weight: bold; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State (To store data across refreshes)
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'blocked_ips' not in st.session_state:
    st.session_state.blocked_ips = set()
if 'system_status' not in st.session_state:
    st.session_state.system_status = "Healthy"

# --- UI Header ---
st.title("🛡️ Sentinel AI: Self-Healing Network")
st.write("Autonomous Threat Detection & Mitigation System")

# --- Sidebar Controls ---
st.sidebar.header("Network Settings")
monitoring = st.sidebar.toggle("Start Monitoring", value=True)
sensitivity = st.sidebar.slider("AI Sensitivity (Threshold)", 50, 150, 100)

if st.sidebar.button("Clear Logs"):
    st.session_state.logs = []
    st.session_state.blocked_ips = set()
    st.session_state.system_status = "Healthy"

# --- Main Dashboard ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("System Status", st.session_state.system_status)
with col2:
    st.metric("Blocked Threats", len(st.session_state.blocked_ips))
with col3:
    st.metric("Network Uptime", "99.9%")

# Placeholder for real-time content
chart_placeholder = st.empty()
log_placeholder = st.empty()

# --- Simulation & Logic Loop ---
if monitoring:
    possible_ips = ["192.168.1.45", "10.0.0.7", "172.16.5.12", "192.168.1.102"]
    
    # Infinite loop to simulate real-time traffic
    while True:
        timestamp = datetime.now().strftime("%H:%M:%S")
        src_ip = random.choice(possible_ips)
        load = random.randint(20, 160)
        
        status = "Normal"
        
        # AI Detection Logic
        if load > sensitivity and src_ip not in st.session_state.blocked_ips:
            status = "🚨 ATTACK DETECTED"
            st.session_state.system_status = f"Healing: Blocking {src_ip}"
            
            # Record the attack
            st.session_state.logs.append({"Time": timestamp, "Source IP": src_ip, "Load": load, "Status": status})
            
            # UI Update for attack
            with log_placeholder.container():
                st.error(f"⚠️ High Traffic detected from {src_ip}! Initializing Self-Healing...")
            
            time.sleep(2) # Healing delay
            st.session_state.blocked_ips.add(src_ip)
            st.session_state.logs.append({"Time": datetime.now().strftime("%H:%M:%S"), "Source IP": "SYSTEM", "Load": 0, "Status": "✅ HEALED: IP Blocked"})
            st.session_state.system_status = "Healthy"
        else:
            if src_ip in st.session_state.blocked_ips:
                status = "Filtered (Blocked)"
                load = 0
            st.session_state.logs.append({"Time": timestamp, "Source IP": src_ip, "Load": load, "Status": status})

        # Keep only last 15 logs
        if len(st.session_state.logs) > 15:
            st.session_state.logs.pop(0)

        # --- Update Dashboard Visuals ---
        df = pd.DataFrame(st.session_state.logs)
        
        with chart_placeholder.container():
            st.subheader("Live Traffic Analysis")
            if not df.empty:
                st.line_chart(df.set_index("Time")["Load"])

        with log_placeholder.container():
            st.subheader("Network Event Logs")
            st.table(df.iloc[::-1]) # Show latest logs on top

        time.sleep(1) # Simulation speed
else:
    st.info("Monitoring Paused. Click 'Start Monitoring' in sidebar.")
