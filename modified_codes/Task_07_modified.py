"""
Task 7 – Modified real-world case
Same power-network admittance matrix, different daily load vectors.
Factor once with LU, then solve for every hour of the day.
"""
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Simplified 3-bus network admittance matrix
Y = np.array([
    [ 4.0, -1.5, -0.5],
    [-1.5,  3.0, -1.0],
    [-0.5, -1.0,  2.5]
])

# 24 hourly load vectors (active-power injections)
rng = np.random.default_rng(0)
loads = [rng.normal([1.0, 0.8, 0.6], 0.1) for _ in range(24)]

lu, piv = lu_factor(Y)

print("Hour | Voltage solution")
for h, P in enumerate(loads, 1):
    V = lu_solve((lu, piv), P)
    print(f"{h:4d} | {np.round(V, 4)}")
