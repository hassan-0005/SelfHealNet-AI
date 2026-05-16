from flask import Flask, render_template, jsonify
import random
import time
from threading import Thread
from datetime import datetime

app = Flask(__name__)

# Global variables to store network state
network_logs = []
system_status = "Healthy"
attack_detected = False

# Simulated AI Model Logic
def ai_monitor():
    global system_status, attack_detected
    ips = ["192.168.1.5", "10.0.0.2", "172.16.0.4", "192.168.1.10"]
    
    while True:
        timestamp = datetime.now().strftime("%H:%M:%S")
        src_ip = random.choice(ips)
        packet_count = random.randint(10, 100)
        
        # AI Detection Logic (Threshold based simulation)
        status = "Normal"
        if packet_count > 85:  # Simulation: high packet count = DDoS attack
            status = "ATTACK DETECTED"
            system_status = "Under Attack"
            attack_detected = True
        
        log_entry = {
            "time": timestamp,
            "ip": src_ip,
            "packets": packet_count,
            "status": status
        }
        
        network_logs.append(log_entry)
        if len(network_logs) > 10: network_logs.pop(0) # Keep last 10 logs

        # Self-Healing Action
        if attack_detected:
            time.sleep(2) # System "thinking" time
            system_status = "Healing: Blocking IP " + src_ip
            time.sleep(3)
            system_status = "Healthy"
            attack_detected = False
            network_logs.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "ip": "SYSTEM",
                "packets": 0,
                "status": "HEALED: IP Blocked"
            })

        time.sleep(2) # Monitor every 2 seconds

# Start the background AI monitor
Thread(target=ai_monitor, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    return jsonify({
        "logs": network_logs,
        "status": system_status
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
