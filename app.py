import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils import logistic_growth

st.set_page_config(page_title="Bacterial Growth Simulator", layout="centered")

st.title("🧫 Bacterial Growth Simulator")

st.write("Simulate how bacteria grow under different conditions.")

# User Inputs
st.sidebar.header("⚙️ Parameters")

initial_population = st.sidebar.slider("Initial Population", 10, 1000, 100)
growth_rate = st.sidebar.slider("Growth Rate (r)", 0.1, 1.0, 0.5)
carrying_capacity = st.sidebar.slider("Carrying Capacity (K)", 100, 5000, 1000)
time = st.sidebar.slider("Time (hours)", 1, 50, 24)

# Environmental Factors
temperature = st.sidebar.slider("Temperature (°C)", 10, 50, 37)
pH = st.sidebar.slider("pH Level", 4.0, 9.0, 7.0)

# Adjust growth rate based on conditions
if temperature < 30 or temperature > 40:
    growth_rate *= 0.5

if pH < 6 or pH > 8:
    growth_rate *= 0.7

# Simulation
t = np.linspace(0, time, 100)
population = logistic_growth(t, initial_population, growth_rate, carrying_capacity)

# Plot
fig, ax = plt.subplots()
ax.plot(t, population)
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Population")
ax.set_title("Bacterial Growth Curve")

st.pyplot(fig)

# Output
st.subheader("📊 Final Population")
st.write(f"{int(population[-1])} cells")

# Learning Section
st.subheader("📘 What is happening?")
st.write("""
This simulation follows a logistic growth model:
- Lag Phase: Slow growth
- Log Phase: Rapid growth
- Stationary Phase: Growth stabilizes
""")