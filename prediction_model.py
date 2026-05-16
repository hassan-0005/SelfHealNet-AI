# agents/prediction_model.py
import numpy as np
from sklearn.ensemble import IsolationForest

class NetworkAI:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)
        # Mock training data: [CPU, RAM, Latency, PacketLoss]
        X = np.random.rand(100, 4) 
        self.model.fit(X)

    def predict_failure(self, current_metrics):
        # Returns score: -1 for anomaly, 1 for normal
        score = self.model.predict([current_metrics])
        confidence = np.random.uniform(85, 99.9)
        return score[0], confidence

# agents/healing_agent.py
class HealingAgent:
    def resolve_issue(self, error_type):
        actions = {
            "DDoS": "Deploying Traffic Scrubbing & Null Routing IP...",
            "Latency": "Optimizing BGP Paths & Flushing DNS Cache...",
            "Overload": "Scaling Vertical Micro-resources & Load Balancing...",
            "Down": "Restarting Node Interface & Switching to Backup Gateway..."
        }
        return actions.get(error_type, "Initiating Global System Reboot...")
