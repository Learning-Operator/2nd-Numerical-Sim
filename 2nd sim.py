import numpy as np
import matplotlib.pyplot as plt

# Pendulum parameters
theta_initial_degrees = 90  # initial angle in degrees
theta_initial_radians = np.radians(theta_initial_degrees)  # initial angle in radians
g = 9.81  # gravitational acceleration (m/s^2)
L = 1.0  # length of the pendulum (in meters)
v_initial = 1  # initial velocity (m/s)

# Simulation parameters
time_steps = 0.02  
total_time = 100  
num_steps = int(total_time / time_steps) 


Positions = np.zeros(num_steps)
Velocity = np.zeros(num_steps)

Positions[0] = theta_initial_degrees  
Velocity[0] = v_initial  


for i in range(1, num_steps):
    theta = Positions[i - 1]
    Speed = Velocity[i - 1]

    
    k1_theta = time_steps * Speed
    k1_Speed = time_steps * (-g / L) * np.sin(np.radians(theta))

    k2_theta = time_steps * (Speed + 0.5 * k1_Speed)
    k2_Speed = time_steps * (-g / L) * np.sin(np.radians(theta + 0.5 * k1_theta))

    k3_theta = time_steps * (Speed + 0.5 * k2_Speed)
    k3_Speed = time_steps * (-g / L) * np.sin(np.radians(theta + 0.5 * k2_theta))

    k4_theta = time_steps * (Speed + k3_Speed)
    k4_Speed = time_steps * (-g / L) * np.sin(np.radians(theta + k3_theta))

    
    Positions[i] = Positions[i - 1] + (k1_theta + 2 * k2_theta + 2 * k3_theta + k4_theta) / 6
    Velocity[i] = Velocity[i - 1] + (k1_Speed + 2 * k2_Speed + 2 * k3_Speed + k4_Speed) / 6

plt.figure(figsize=(8, 8))
plt.plot(Positions, Velocity, label="Phase Space Trajectory")
plt.title("Phase Space Plot (Position vs. Velocity)")
plt.xlabel("Theta (θ) [degrees]")
plt.ylabel("Velocity (v) [m/s]")
plt.grid()
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.legend()
plt.show()
