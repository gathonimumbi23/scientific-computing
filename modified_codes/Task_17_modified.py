"""
Task 17 – Modified real-world case
Radioactive decay of a sample using Euler’s method.
dN/dt = -λ N
"""
import numpy as np
import matplotlib.pyplot as plt

N0 = 1000.0          # initial nuclei
lam = 0.05           # decay constant (1/h)
h = 0.5              # step size (hours)
t_end = 40.0

t = np.arange(0, t_end + h, h)
N = np.zeros_like(t)
N[0] = N0

for i in range(len(t)-1):
    N[i+1] = N[i] + h * (-lam * N[i])

exact = N0 * np.exp(-lam * t)

print(f"Euler remaining after {t_end} h: {N[-1]:.1f}")
print(f"Exact remaining             : {exact[-1]:.1f}")
print(f"Absolute error              : {abs(N[-1]-exact[-1]):.2f}")

plt.plot(t, N, "o-", label="Euler")
plt.plot(t, exact, label="Exact")
plt.xlabel("Time (h)")
plt.ylabel("Number of nuclei")
plt.title("Radioactive decay – Euler method")
plt.legend()
plt.grid(True)
plt.savefig("Task_17_modified_decay.png")
plt.show()
