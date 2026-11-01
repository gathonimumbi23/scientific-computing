"""
Task 20 – Modified real-world case
Monte-Carlo estimate of the probability that a project finishes late.
Activity durations ~ Normal; critical-path sum compared with deadline.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
N = 50_000
deadline = 45.0          # days

# Three activities on the critical path (mean, std)
means = np.array([12.0, 18.0, 10.0])
stds  = np.array([2.0,  3.0,  1.5])

durations = rng.normal(means, stds, size=(N, 3))
total = durations.sum(axis=1)
late  = total > deadline
prob  = late.mean()

print(f"Estimated P(late) = {prob:.4%}")
print(f"Number of late projects: {late.sum()} / {N}")

running = np.cumsum(late) / np.arange(1, N+1)
idx = np.unique(np.linspace(0, N-1, 400, dtype=int))
plt.plot(idx+1, running[idx])
plt.xlabel("Simulations")
plt.ylabel("Running P(late)")
plt.title("Monte-Carlo project-delay probability")
plt.grid(True)
plt.savefig("Task_20_modified_project.png")
plt.show()
