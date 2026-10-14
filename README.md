# Lotka-Volterra Numerical Simulation (Euler & RK4)

This repository contains numerical implementations and phase portrait visualizations of the classical **Lotka-Volterra (Predator-Prey)** system using Python and `matplotlib`.

The non-linear differential equations are solved using two distinct numerical methods:
1. **Euler Method** (First-order numerical approximation)
2. **4th-Order Runge-Kutta Method (RK4)** (Higher-order numerical integrator)

---

## 📌 Mathematical Model

The Lotka-Volterra equations model the biological dynamics between prey population $x(t)$ and predator population $y(t)$:

$$\begin{aligned} \frac{dx}{dt} &= \alpha x - \beta x y \\ \frac{dy}{dt} &= \delta x y - \gamma y \end{aligned}$$

### Parameter Settings
- $\alpha = 1.0$ (Prey growth rate)
- $\beta = 1.0$ (Predation rate)
- $\gamma = 1.0$ (Predator mortality rate)
- $\delta = 1.0$ (Predator reproduction per prey eaten)
- Time step: $h = 0.01$
- Time interval: $t \in [0, 40]$

---

## 🧪 Initial Conditions Evaluated

Simulations are executed across four distinct initial population states:
1. $(x_0, y_0) = (1.1, 1.0)$
2. $(x_0, y_0) = (2.0, 1.0)$
3. $(x_0, y_0) = (4.0, 1.0)$
4. $(x_0, y_0) = (4.0, 0.2)$

---

## 🚀 Features

- **Time-Series Plots:** Compares population oscillations over time $t$ for both prey and predator.
- **Numerical Error Comparison:** Highlights numerical dissipation and amplitude drift in the forward Euler approach versus the orbital stability of the RK4 integrator.
- **Phase Portrait Analysis:** Visualizes closed trajectories in the $x-y$ phase space for multiple initial conditions simultaneously using the RK4 method.

---

## 🛠️ Requirements & Setup

### Prerequisites
Make sure you have Python 3 installed along with `matplotlib`:

```bash
pip install matplotlib