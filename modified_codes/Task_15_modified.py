"""
Task 15 – Modified real-world case
Estimate acceleration from discrete velocity measurements of a vehicle.
"""
import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
vel  = np.array([0, 4, 9, 15, 20, 24, 26], dtype=float)   # m/s

acc = np.zeros_like(vel)
acc[0]  = (vel[1] - vel[0]) / (time[1] - time[0])          # forward
for i in range(1, len(time)-1):
    acc[i] = (vel[i+1] - vel[i-1]) / (time[i+1] - time[i-1])  # central
acc[-1] = (vel[-1] - vel[-2]) / (time[-1] - time[-2])      # backward

for t, v, a in zip(time, vel, acc):
    print(f"t={t:.0f}s  v={v:5.1f} m/s  a={a:5.2f} m/s²")

plt.plot(time, acc, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration estimated from velocity data")
plt.grid(True)
plt.savefig("Task_15_modified_accel.png")
plt.show()
