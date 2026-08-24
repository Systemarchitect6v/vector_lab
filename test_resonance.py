"""
test_resonance.py - Unit test suite for engine.py
"""

from engine import ContinuousMediumEngine
import numpy as np

def test_engine_convergence():
    engine = ContinuousMediumEngine(coupling_strength=0.85, substrate_noise=0.05)
    trajectory, imbalances = engine.run_trajectory_simulation(steps=1000)
    
    mean_imbalance = np.mean(imbalances)
    print(f"✅ Simulation Complete. Mean Imbalance across 1,000 steps: {mean_imbalance:.4f}")
    
    # Assert that mean pair imbalance remains bounded under resonance envelope (<= 0.35)
    assert mean_imbalance <= 0.35, "Error: Engine failed to maintain substrate balance!"
    print("✅ Unit Test Passed: Substrate phase-locking verified successfully.")

if __name__ == "__main__":
    test_engine_convergence()