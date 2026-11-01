"""
Task 8 – Modified real-world case
1-D steady heat conduction with different boundary temperatures
(left = 80 °C, right = 10 °C) solved by Gauss-Seidel.
"""
import numpy as np
import matplotlib.pyplot as plt

n = 7
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 2.0
    if i > 0:
        A[i, i-1] = -1.0
    if i < n-1:
        A[i, i+1] = -1.0

b = np.zeros(n)
b[0]  = 80.0          # left boundary influence
b[-1] = 10.0          # right boundary influence

def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            s1 = A[i, :i] @ x[:i]
            s2 = A[i, i+1:] @ old[i+1:]
            x[i] = (b[i] - s1 - s2) / A[i, i]
        err = np.linalg.norm(x - old, np.inf)
        errors.append(err)
        if err < tol:
            break
    return x, errors

T, errs = gauss_seidel(A, b)
print("Temperatures (°C):", np.round(T, 2))
print("Iterations:", len(errs))

plt.semilogy(errs)
plt.xlabel("Iteration")
plt.ylabel("Max change")
plt.title("Gauss-Seidel convergence – heat conduction")
plt.grid(True)
plt.savefig("Task_08_modified_convergence.png")
plt.show()
