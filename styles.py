import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        
        .main { background-color: #030712; color: #e5e7eb; }
        .stApp { background: radial-gradient(circle at top right, #1e1b4b, #030712); }
        
        /* Glassmorphism Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            border: 1px solid #3b82f6;
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
        }
        
        /* Neon Text */
        .neon-blue { color: #60a5fa; text-shadow: 0 0 10px #3b82f6; font-family: 'Orbitron', sans-serif; }
        .neon-red { color: #f87171; text-shadow: 0 0 10px #ef4444; font-family: 'Orbitron', sans-serif; }
        .neon-green { color: #4ade80; text-shadow: 0 0 10px #22c55e; font-family: 'Orbitron', sans-serif; }
        
        /* Metrics Sidebar */
        [data-testid="stSidebar"] { background-color: rgba(17, 24, 39, 0.8); border-right: 1px solid #1f2937; }
        </style>
    """, unsafe_allow_html=True)
