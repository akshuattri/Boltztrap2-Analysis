import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt("interpolation.trace")

# Columns
mu = data[:, 0]          # chemical potential
temp = data[:, 1]        # temperature
Sxx = data[:, 4]         # Seebeck xx

# Select one temperature
T = 300

mask = temp == T

plt.figure(figsize=(8,6))
plt.plot(mu[mask], Sxx[mask])

plt.xlabel("Chemical Potential (eV)")
plt.ylabel("Seebeck Coefficient Sxx (µV/K)")
plt.title(f"Seebeck Coefficient at {T} K")

plt.grid(True)

plt.savefig("figures/seebeck_300K.png", dpi=300)
plt.show()
