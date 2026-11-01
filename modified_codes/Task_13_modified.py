"""
Task 13 – Modified real-world case
Reconstruct missing hourly PM2.5 air-quality readings with cubic spline.
"""
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
# Some readings are missing (NaN)
pm25  = np.array([35, 42, np.nan, 55, 60, np.nan, 48, 40, 38])

# Use only valid points for interpolation
mask = ~np.isnan(pm25)
cs = CubicSpline(hours[mask], pm25[mask])

fine_hours = np.linspace(0, 8, 100)
reconstructed = cs(fine_hours)

print("Reconstructed values at missing hours:")
print(f"  2 h → {cs(2):.1f} µg/m³")
print(f"  5 h → {cs(5):.1f} µg/m³")

plt.scatter(hours[mask], pm25[mask], label="Measured", zorder=5)
plt.plot(fine_hours, reconstructed, label="Cubic spline")
plt.xlabel("Hour")
plt.ylabel("PM2.5 (µg/m³)")
plt.title("Air-quality data reconstruction")
plt.legend()
plt.grid(True)
plt.savefig("Task_13_modified_pm25.png")
plt.show()
