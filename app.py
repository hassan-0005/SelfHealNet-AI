import streamlit as st
import pandas as pd
import numpy as np
import time
import random
import plotly.graph_objects as go
from datetime import datetime
from sklearn.ensemble import IsolationForest

# ==========================================
# 1. ENTERPRISE UI STYLING (Glassmorphism)
# ==========================================
def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
        
        .main { background-color: #030712; color: #e5e7eb; font-family: 'Inter', sans-serif; }
        .stApp { background: radial-gradient(circle at top right, #1e1b4b, #030712); }
        
        /* Glassmorphism Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        }
        
        /* Neon Effects */
        .neon-blue { color: #60a5fa; text-shadow: 0 0 10px #3b82f6; font-family: 'Orbitron', sans-serif; }
        .neon-red { color: #f87171; text-shadow: 0 0 15px #ef4444; font-family: 'Orbitron', sans-serif; animation: blink 1.5s infinite; }
        .neon-green { color: #4ade80; text-shadow: 0 0 10px #22c55e; font-family: 'Orbitron', sans-serif; }
        
        @keyframes blink { 50% { opacity: 0.3; } }
        
        /* Metrics Styling */
        [data-testid="stMetricValue"] { font-family: 'Orbitron', sans-serif; color: #60a5fa; }
        
        /* Custom Table */
        .stTable { background-color: transparent; border-radius: 10px; overflow: hidden; }
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. AI MULTI-AGENT ARCHITECTURE
# ==========================================
class SentinelAI:
    def __init__(self):
        # AI Anomaly Detection Model
        self.model = IsolationForest(contamination=0.1)
        # Dummy Training: [CPU, RAM, Latency, PacketLoss]
        X_train = np.random.rand(100, 4)
        self.model.fit(X_train)

    def analyze_network(self):
        cpu = random.uniform(20, 95)
        ram = random.uniform(30, 90)
        lat = random.uniform(10, 200)
        loss = random.uniform(0, 5)
        
        # Prediction
        status_code = self.model.predict([[cpu/100, ram/100, lat/100, loss]])[0]
        confidence = random.uniform(92, 99.8)
        
        return {
            "cpu": round(cpu, 1), "ram": round(ram, 1), 
            "lat": round(lat, 1), "loss": round(loss, 2),
            "is_anomaly": status_code == -1,
            "conf": round(confidence, 2)
        }

class HealingAgent:
    def execute_repair(self, issue_type):
        actions = {
            "DDoS": "Initiating Traffic Scrubbing & IP Null-Routing...",
            "Latency": "Flushing DNS & Rerouting via Backup BGP...",
            "Overload": "Scaling Vertical Resources & Load Balancing...",
            "Node Down": "Rebooting Interface & Recovering Failed Gateway..."
        }
        return actions.get(issue_type, "Applying AI-Optimization Patches...")

# ==========================================
# 3. STREAMLIT FRONTEND APP
# ==========================================
def main():
    st.set_page_config(page_title="Sentinel AI | Autonomous SOC", layout="wide")
    apply_custom_styles()
    
    # Session State Initialization
    if 'logs' not in st.session_state: st.session_state.logs = []
    if 'blocked' not in st.session_state: st.session_state.blocked = 0
    if 'is_attack' not in st.session_state: st.session_state.is_attack = False

    ai_engine = SentinelAI()
    healer = HealingAgent()

    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("<h1 class='neon-blue'>SENTINEL AI</h1>", unsafe_allow_html=True)
        st.write("v4.5.0 Enterprise Edition")
        st.markdown("---")
        menu = st.radio("SYSTEM MODULES", ["Global Overview", "Cybersecurity Layer", "Digital Twin Simulation", "Forensic Logs"])
        st.markdown("---")
        st.metric("Global Health Score", "98.4%", "+0.2%")
        if st.button("Emergency System Reset"):
            st.session_state.logs = []
            st.session_state.is_attack = False
            st.rerun()

    # --- TOP METRICS PANEL ---
    st.markdown(f"<h2 class='neon-blue'>{menu.upper()}</h2>", unsafe_allow_html=True)
    
    metrics = ai_engine.analyze_network()
    
    # Auto-Trigger Attack Simulation
    if metrics["is_anomaly"] and not st.session_state.is_attack:
        st.session_state.is_attack = True

    # --- DASHBOARD LOGIC ---
    if menu == "Global Overview":
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("CPU Load", f"{metrics['cpu']}%")
        c2.metric("RAM Usage", f"{metrics['ram']}%")
        c3.metric("Latency", f"{metrics['lat']}ms")
        c4.metric("Packet Loss", f"{metrics['loss']}%")

        # Live Topology Map (Plotly)
        st.subheader("Global Network Topology")
        fig = go.Figure(go.Scattergeo(
            locationmode = 'USA-states',
            lon = [-74, -118, -87, -95, -122], lat = [40, 34, 41, 29, 47],
            mode = 'markers+lines',
            marker = dict(size = 12, color = '#60a5fa', line=dict(width=2, color='white')),
            line = dict(width = 1, color = 'rgba(96, 165, 250, 0.4)')
        ))
        fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', showframe=False, showcoastlines=True, coastlinecolor="#1e293b"),
                          margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', height=450)
        st.plotly_chart(fig, use_container_width=True)

    elif menu == "Cybersecurity Layer":
        if st.session_state.is_attack:
            st.markdown('<div class="glass-card"><h1 class="neon-red">🚨 CRITICAL THREAT DETECTED</h1><p>AI Agent: Isolation Forest Anomaly Detection triggered.</p></div>', unsafe_allow_html=True)
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.error("Attack Source: 185.102.x.x (DDoS Profile)")
                if st.button("Execute Manual Mitigation"):
                    st.session_state.is_attack = False
                    st.session_state.blocked += 1
                    st.session_state.logs.append({"Time": datetime.now().strftime("%H:%M:%S"), "Event": "DDoS Neutralized", "Action": "Firewall Rule Updated"})
                    st.rerun()
            with col_b:
                st.info("Healing Status: In Progress...")
                st.progress(65)
        else:
            st.success("Cybersecurity Layer: All nodes reporting secure.")
            st.info(f"Threats Blocked Today: {st.session_state.blocked}")

    elif menu == "Digital Twin Simulation":
        st.subheader("Predictive Failure Simulation")
        sim_choice = st.selectbox("Inject Network Fault", ["BGP Route Leak", "Packet Flood", "DNS Cache Poisoning"])
        if st.button("Start AI Healing Test"):
            with st.status("Simulating Failure...", expanded=True) as s:
                time.sleep(1)
                st.write("AI Agent Detecting Root Cause...")
                time.sleep(1)
                st.write(f"Healing Agent: {healer.execute_repair('DDoS' if 'Flood' in sim_choice else 'Latency')}")
                time.sleep(1)
                s.update(label="System Recovered via AI Digital Twin", state="complete")

    elif menu == "Forensic Logs":
        st.subheader("System Event History")
        if st.session_state.logs:
            st.table(pd.DataFrame(st.session_state.logs).iloc[::-1])
        else:
            st.write("No critical events recorded.")

    # Footer AI Insights
    st.markdown("---")
    st.write(f"✨ AI Insight: System is currently {metrics['conf']}% stable. Optimization Agent suggests clearing temporary cache on Node-7.")

if __name__ == "__main__":
    main()
