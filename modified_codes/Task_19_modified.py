"""
Task 19 – Modified real-world case
Minimise daily food cost subject to minimum protein and calorie requirements.
"""
import numpy as np
from scipy.optimize import minimize

# Variables: x = kg of food A, y = kg of food B
# Cost: 3x + 5y
# Protein: 20x + 10y ≥ 50
# Calories: 100x + 200y ≥ 400

def cost(z):
    return 3*z[0] + 5*z[1]

cons = [
    {"type": "ineq", "fun": lambda z: 20*z[0] + 10*z[1] - 50},
    {"type": "ineq", "fun": lambda z: 100*z[0] + 200*z[1] - 400}
]

bounds = [(0, None), (0, None)]
res = minimize(cost, [1, 1], method="SLSQP", bounds=bounds, constraints=cons)

print("Success:", res.success)
print(f"Food A: {res.x[0]:.3f} kg")
print(f"Food B: {res.x[1]:.3f} kg")
print(f"Minimum cost: {res.fun:.2f}")
