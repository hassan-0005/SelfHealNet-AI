from flask import Flask, render_template, jsonify
import random
import time
from threading import Thread
from datetime import datetime

app = Flask(__name__)

# Global state
network_data = {
    "logs": [],
    "status": "Healthy",
    "is_healing": False,
    "blocked_ips": set()
}

def ai_engine():
    """Background AI Engine that monitors and heals the network"""
    possible_ips = ["192.168.1.15", "10.0.0.5", "172.16.25.10", "192.168.1.100"]
    
    while True:
        if not network_data["is_healing"]:
            src_ip = random.choice(possible_ips)
            # Simulate packet load
            packet_load = random.randint(20, 150)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            status = "Normal"
            # AI Logic: If load > 100 and IP not already blocked
            if packet_load > 100 and src_ip not in network_data["blocked_ips"]:
                status = "⚠️ ATTACK DETECTED"
                network_data["status"] = f"Analyzing Attack from {src_ip}..."
                network_data["is_healing"] = True
                
                # Add attack log
                network_data["logs"].append({"time": timestamp, "ip": src_ip, "packets": packet_load, "status": status})
                
                # Start Healing Process
                time.sleep(3) # AI processing time
                network_data["status"] = f"Healing: Blocking {src_ip} via Firewall..."
                time.sleep(3) # Action time
                
                network_data["blocked_ips"].add(src_ip)
                network_data["logs"].append({
                    "time": datetime.now().strftime("%H:%M:%S"), 
                    "ip": "SYSTEM", 
                    "packets": 0, 
                    "status": "✅ HEALED: IP Restricted"
                })
                network_data["status"] = "Healthy"
                network_data["is_healing"] = False
            else:
                # Normal traffic
                network_data["logs"].append({"time": timestamp, "ip": src_ip, "packets": packet_load, "status": status})

        # Keep only last 12 logs
        if len(network_data["logs"]) > 12:
            network_data["logs"].pop(0)
            
        time.sleep(2)

# Start AI Engine in background
Thread(target=ai_engine, daemon=True).start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify({
        "logs": network_data["logs"],
        "status": network_data["status"],
        "blocked_count": len(network_data["blocked_ips"])
    })

if __name__ == '__main__':
    # Flask ko run karne ka sahi tareeqa
    app.run(debug=True, port=5000)
