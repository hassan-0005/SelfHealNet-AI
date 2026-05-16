from flask import Flask, render_template, jsonify
import random
import time
import threading
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np

app = Flask(__name__)

# --- NETWORK SIMULATION DATA ---
nodes = ["Router-01", "Router-02", "Router-03", "Server-01"]
network_status = {
    "status": "Healthy",
    "logs": [],
    "metrics": {"latency": 20, "packet_loss": 0, "traffic": 100}
}

# Simulated AI Model Training Data (Normal Traffic)
data = np.random.normal(size=(100, 2))
model = IsolationForest(contamination=0.1)
model.fit(data)

def monitor_network():
    global network_status
    while True:
        # Simulate Network Metrics
        latency = random.randint(15, 25)
        packet_loss = random.randint(0, 1)
        traffic = random.randint(80, 120)

        # AI Detection (Anomaly)
        # Agar latency 100 se upar jaye ya packet loss ho, toh anomaly hai
        current_metric = [[latency, packet_loss]]
        is_anomaly = random.choice([False, False, False, True]) if latency < 50 else True

        if is_anomaly:
            network_status["status"] = "Healing..."
            log_entry = f"⚠️ Alert: High Latency ({latency}ms) detected at {time.strftime('%H:%M:%S')}"
            network_status["logs"].insert(0, log_entry)
            
            # --- SELF-HEALING LOGIC ---
            time.sleep(2) # Healing process simulation
            network_status["status"] = "Recovered ✅"
            network_status["logs"].insert(0, f"✅ Self-Healed: Rerouted traffic to Backup Path at {time.strftime('%H:%M:%S')}")
            latency = 20 # Reset after healing
        else:
            network_status["status"] = "Healthy 🟢"

        network_status["metrics"] = {"latency": latency, "packet_loss": packet_loss, "traffic": traffic}
        time.sleep(3)

# Background thread for monitoring
threading.Thread(target=monitor_network, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    return jsonify(network_status)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
