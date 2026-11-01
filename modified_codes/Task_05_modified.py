"""
Task 5 – Modified real-world case
2-D robot-arm pose transformation:
translate the end-effector by (3,1) then rotate 30 degrees about the origin.
"""
import numpy as np

# End-effector points (simple polyline)
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.5, 0.5],
    [2.0, 0.5]
])

# Homogeneous coordinates for easy composition
ones = np.ones((points.shape[0], 1))
pts_h = np.hstack([points, ones])

theta = np.deg2rad(30)
R = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0,              0,             1]
])

T = np.array([
    [1, 0, 3],
    [0, 1, 1],
    [0, 0, 1]
])

# Translate first, then rotate
transformed = (R @ T @ pts_h.T).T

print("Original points:\n", points)
print("Transformed points:\n", transformed[:, :2])
