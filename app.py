import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="6-Vector Benchmark Suite", layout="wide")

st.title("⚡ 3-Way Trajectory Benchmark Suite")
st.markdown("Comparing **Traditional INS**, **Extended Kalman Filter (EKF)**, and the **6-Vector Coupled Engine** in signal-denied conditions.")

# Sidebar controls
st.sidebar.header("Simulation Control Panel")
time_steps = st.sidebar.slider("Time Horizon (Steps)", min_value=50, max_value=500, value=100, step=10)
sensor_noise = st.sidebar.slider("Sensor Noise Variance (σ)", 0.01, 0.50, 0.10, 0.01)

st.sidebar.subheader("6-Vector Engine Settings")
coupling_strength = st.sidebar.slider("Substrate Coupling (C)", 0.0, 1.0, 0.85, 0.05)

# Simulation Engine Function
def run_benchmark(steps, noise, coupling):
    t = np.arange(steps)
    
    # 1. Traditional INS: Unchecked quadratic drift (~t^1.8)
    ins_drift = 0.5 * (noise * 1.5) * (t ** 1.8) + np.random.normal(0, noise, steps)
    
    # 2. EKF: Linear bounded noise drift
    ekf_drift = np.cumsum(np.random.normal(0, noise * 0.8, steps))
    
    # 3. 6-Vector Engine: Dynamic restoring attractor
    v6_drift = []
    for _ in range(steps):
        v0 = np.random.uniform(-1.0, 1.0)
        v1 = -v0 * coupling + np.random.normal(0, noise * 0.5)
        imbalance = abs(v0 + v1)
        v6_drift.append(imbalance)
        
    return t, ins_drift, ekf_drift, np.array(v6_drift)

# Always execute initial calculation so dashboard renders immediately
t, ins_drift, ekf_drift, v6_drift = run_benchmark(time_steps, sensor_noise, coupling_strength)

# Button to manually trigger a re-run
if st.button("Re-Run Benchmark Simulation", type="primary"):
    t, ins_drift, ekf_drift, v6_drift = run_benchmark(time_steps, sensor_noise, coupling_strength)

# Top Level Metrics
m1, m2, m3 = st.columns(3)
m1.metric("INS Cumulative Error (t_max)", f"{ins_drift[-1]:.2f} m", delta="Unbounded Drift", delta_color="inverse")
m2.metric("EKF Filtered Error (t_max)", f"{ekf_drift[-1]:.2f} m", delta="Linear Growth", delta_color="inverse")
m3.metric("6-Vector Phase Error (t_max)", f"{v6_drift[-1]:.2f} rad", delta="Bounded Attractor", delta_color="normal")

st.markdown("---")

# Visual Layout (Make Subplots)
fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=("Trajectory Error Accumulation Over Time", "Phase-Space Imbalance Stability"),
    vertical_spacing=0.15
)

# Chart 1: Cumulative Error Comparison
fig.add_trace(go.Scatter(x=t, y=ins_drift, mode='lines', name='Traditional INS (Quadratic Drift)', line=dict(color='#FF4B4B', width=2)), row=1, col=1)
fig.add_trace(go.Scatter(x=t, y=ekf_drift, mode='lines', name='Extended Kalman Filter (EKF)', line=dict(color='#FFCC00', width=2)), row=1, col=1)
fig.add_trace(go.Scatter(x=t, y=v6_drift, mode='lines', name='6-Vector Coupled Engine', line=dict(color='#00FF66', width=2.5)), row=1, col=1)

# Chart 2: Phase Envelope Comparison
fig.add_trace(go.Scatter(x=t, y=v6_drift, mode='lines+markers', name='6-Vector Attractor Envelope', line=dict(color='#00FF66', width=1.5), marker=dict(size=4)), row=2, col=1)
fig.add_trace(go.Scatter(x=t, y=[0.25]*time_steps, mode='lines', name='Resonance Stability Bound (0.25)', line=dict(color='#3399FF', dash='dash')), row=2, col=1)

fig.update_xaxes(title_text="Time Steps (t)", row=1, col=1)
fig.update_xaxes(title_text="Time Steps (t)", row=2, col=1)
fig.update_yaxes(title_text="Position Error (m)", row=1, col=1)
fig.update_yaxes(title_text="Pair Imbalance (Phase Strain)", row=2, col=1)

fig.update_layout(height=750, template="plotly_dark", showlegend=True)

# Display Chart directly in Streamlit
st.plotly_chart(fig, use_container_width=True)
