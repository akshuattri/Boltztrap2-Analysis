import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt("../examples/interpolation.trace")

# Columns
mu = data[:,0]
temp = data[:,1]

# Adjust indices if needed
Sxx = data[:,4]          # Seebeck coefficient
sigma_xx = data[:,7]     # electrical conductivity
kappa_xx = data[:,10]    # electronic thermal conductivity

# Select temperature
T = 300
mask = temp == T

# Convert Seebeck from microV/K to V/K
S = Sxx[mask] * 1e-6

sigma = sigma_xx[mask]
kappa = kappa_xx[mask]

# Optional lattice thermal conductivity
kappa_lattice = 1.0

# Total thermal conductivity
kappa_total = kappa + kappa_lattice

# ZT calculation
ZT = (S**2 * sigma * T) / kappa_total

# Plot
plt.figure(figsize=(8,6))

plt.plot(mu[mask], ZT)

plt.xlabel("Chemical Potential (eV)")
plt.ylabel("ZT")

plt.title(f"ZT vs Chemical Potential at {T} K")

plt.grid(True)

plt.savefig("../figures/ZT_300K.png", dpi=300)

plt.show()
