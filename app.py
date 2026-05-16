import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="AI Sentinel: Self-Healing Network", layout="wide")

# --- Custom Styling for Red Alarm & UI ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #161b22; border-radius: 5px; color: white; padding: 10px; }
    .stTabs [aria-selected="true"] { background-color: #1f6feb; }
    
    /* Alarm Animation */
    @keyframes blinker { 50% { opacity: 0; } }
    .alarm-red {
        background-color: #7a0000;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid red;
        color: white;
        text-align: center;
        animation: blinker 1.5s linear infinite;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Initialize Global Session State ---
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'blocked_ips' not in st.session_state:
    st.session_state.blocked_ips = set()
if 'is_attack' not in st.session_state:
    st.session_state.is_attack = False
if 'devices' not in st.session_state:
    st.session_state.devices = [
        {"ip": "192.168.1.1", "name": "Main Router", "status": "Secure"},
        {"ip": "192.168.1.15", "name": "Workstation-1", "status": "Secure"},
        {"ip": "10.0.0.5", "name": "Database Server", "status": "Secure"},
        {"ip": "172.16.0.2", "name": "IoT Gateway", "status": "Secure"}
    ]

# --- Sidebar Navigation ---
st.sidebar.title("🛡️ Sentinel AI Admin")
menu = st.sidebar.radio("Navigation", ["Overview Dashboard", "Network Scanner", "Threat Center", "System Logs"])
st.sidebar.markdown("---")
if st.sidebar.button("System Reset"):
    st.session_state.logs = []
    st.session_state.blocked_ips = set()
    st.session_state.is_attack = False
    st.rerun()

# --- Shared Background Logic (Simulation) ---
def simulate_traffic():
    if random.random() > 0.85 and not st.session_state.is_attack:
        st.session_state.is_attack = True
        attacker_ip = random.choice([d['ip'] for d in st.session_state.devices])
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.logs.append({"Time": timestamp, "IP": attacker_ip, "Action": "🚨 DDoS Attack Detected", "Type": "High Traffic"})
        return attacker_ip
    return None

# --- Tab 1: Overview Dashboard ---
if menu == "Overview Dashboard":
    st.header("Network Real-Time Monitor")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Live Traffic", f"{random.randint(15, 45)} Mbps")
    c2.metric("Blocked Threats", len(st.session_state.blocked_ips))
    c3.metric("AI Confidence", "98.4%")

    # Chart
    chart_data = pd.DataFrame(st.session_state.logs[-10:])
    if not chart_data.empty:
        st.subheader("Traffic Flux (Last 10 Events)")
        st.line_chart(random.sample(range(10, 100), 10))
    else:
        st.info("Gathering network packets...")

# --- Tab 2: Network Scanner ---
elif menu == "Network Scanner":
    st.header("🔍 Intelligent Network Discovery")
    if st.button("Start Full Network Scan"):
        with st.status("Scanning ports and devices...", expanded=True) as status:
            time.sleep(1)
            st.write("Checking 192.168.1.0/24...")
            time.sleep(1)
            st.write("Analyzing node vulnerabilities...")
            time.sleep(1)
            status.update(label="Scan Complete!", state="complete", expanded=False)
        
        # Display Scan Table
        st.subheader("Connected Devices")
        df_dev = pd.DataFrame(st.session_state.devices)
        st.table(df_dev)
        st.success("All devices verified. No open vulnerabilities found.")

# --- Tab 3: Threat Center (The Red Alarm Tab) ---
elif menu == "Threat Center":
    st.header("⚡ Threat Response Unit")
    
    if st.session_state.is_attack:
        st.markdown('<div class="alarm-red"><h1>⚠️ CRITICAL ALERT: NETWORK BREACH DETECTED</h1><p>AI Engine is initiating self-healing protocols...</p></div>', unsafe_allow_html=True)
        
        st.warning("Detection Source: Isolation Forest Model (Anomaly Detection)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.error("Under Attack: 10.0.0.5")
            if st.button("Manual Kill Connection"):
                st.session_state.is_attack = False
                st.session_state.blocked_ips.add("10.0.0.5")
                st.rerun()
        with col_b:
            st.info("Auto-Healing Status: 75% Completed")
            st.progress(75)
            
        # Simulation of Auto-Healing
        time.sleep(2)
        st.session_state.is_attack = False
        st.session_state.blocked_ips.add("10.0.0.5")
        st.session_state.logs.append({"Time": datetime.now().strftime("%H:%M:%S"), "IP": "SYSTEM", "Action": "✅ Auto-Healed: IP Blocked", "Type": "Firewall Rule"})
        st.toast("Threat neutralized automatically!")
    else:
        st.balloons()
        st.success("No active threats detected. Network is secure.")
        st.image("https://cdn-icons-png.flaticon.com/512/6863/6863430.png", width=100)

# --- Tab 4: System Logs ---
elif menu == "System Logs":
    st.header("📜 Forensic Logs")
    if st.session_state.logs:
        df_logs = pd.DataFrame(st.session_state.logs)
        st.dataframe(df_logs.iloc[::-1], use_container_width=True)
    else:
        st.write("No logs recorded yet.")

# --- Background Auto-Trigger ---
# Ye part background mein random attacks generate karta hai taake demo dikhaya ja sakay
if not st.session_state.is_attack:
    simulate_traffic()
    time.sleep(0.1)
