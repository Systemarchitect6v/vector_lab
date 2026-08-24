"""
engine.py - Continuous-Medium Vector Engine (Psi(6v))
Author: Kevin Bynum
Description: Core computational framework modeling dynamic phase-space equilibrium 
             and 6-vector restoring substrate forces.
"""

import numpy as np

class ContinuousMediumEngine:
    def __init__(self, coupling_strength=0.85, substrate_noise=0.10):
        """
        Initialize the 6-vector continuous-medium engine.
        :param coupling_strength: Coefficient C representing substrate medium tension (0.0 to 1.0).
        :param substrate_noise: Gaussian noise variance sigma representing phase noise.
        """
        self.C = coupling_strength
        self.noise = substrate_noise

    def generate_coupled_state(self):
        """
        Generate a single 6-vector state Ψ(6v) governed by substrate restoring forces.
        """
        # Primary vectors generated across 3 orthogonal axes
        v0 = np.random.uniform(-1.0, 1.0)
        v2 = np.random.uniform(-1.0, 1.0)
        v4 = np.random.uniform(-1.0, 1.0)
        
        # Opposing partners react dynamically via substrate coupling
        v1 = -v0 * self.C + np.random.normal(0, self.noise)
        v3 = -v2 * self.C + np.random.normal(0, self.noise)
        v5 = -v4 * self.C + np.random.normal(0, self.noise)
        
        return np.array([v0, v1, v2, v3, v4, v5])

    def evaluate_resonance(self, state):
        """
        Compute total magnitude and dynamic pair imbalance for a given 6-vector state.
        """
        magnitude = np.sqrt(np.sum(state**2))
        imbalance = np.sqrt((state[0] + state[1])**2 + (state[2] + state[3])**2 + (state[4] + state[5])**2)
        return magnitude, imbalance

    def run_trajectory_simulation(self, steps=100):
        """
        Simulate a time-series trajectory across steps.
        """
        trajectory = []
        imbalances = []
        for _ in range(steps):
            state = self.generate_coupled_state()
            mag, imbal = self.evaluate_resonance(state)
            trajectory.append(state)
            imbalances.append(imbal)
        return np.array(trajectory), np.array(imbalances)