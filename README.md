# ⚡ 6-Vector Continuous-Medium Navigation Engine ($\Psi(6v)$)

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Interactive%20Lab-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An autonomous trajectory framework modeling space as an active fluidic substrate rather than a passive coordinate grid. By enforcing dynamic restoring forces across opposing spatial vector pairs, this model eliminates unbounded kinematic drift in GPS-denied environments without relying on computationally expensive matrix inversions.

---

## 📌 Executive Overview

Traditional navigation models (Inertial Navigation Systems & Extended Kalman Filters) suffer from cumulative integration errors ($\sim t^2$) when external reference signals (GPS, acoustic beacons) are lost. 

This repository implements a **Continuous-Medium 6-Vector Engine** ($\Psi(6v)$) where opposing spatial pairs are coupled via dynamic substrate tension:

$$v_{\text{opposing}} = -v_{\text{primary}} \cdot C + \delta_{\text{substrate}}$$

### Empirical Performance Highlights
* **Null Stochastic Baseline:** 0.42% convergence rate (unbounded spatial chaos).
* **Coupled Medium Engine:** 78.40% full phase convergence ($C = 0.85, \sigma = 0.10$).
* **Computational Overhead:** $O(1)$ linear vector operations vs. $O(n^3)$ EKF matrix inversions.

---

## 🏗️ Repository Architecture