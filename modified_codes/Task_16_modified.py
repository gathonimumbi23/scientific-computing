"""
Task 16 – Modified real-world case
Estimate distance travelled from irregular speedometer readings
using the trapezoidal rule.
"""
import numpy as np
from scipy.integrate import trapezoid

time_min = np.array([0, 5, 12, 20, 28, 35, 45], dtype=float)   # minutes
speed_kmh = np.array([0, 40, 60, 55, 70, 50, 0], dtype=float)

# Convert to hours for consistent units (km)
time_h = time_min / 60.0
distance = trapezoid(speed_kmh, time_h)

print(f"Estimated distance travelled: {distance:.2f} km")
