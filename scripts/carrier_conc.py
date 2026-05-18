import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../examples/interpolation.trace")

mu = data[:,0]
temp = data[:,1]

carrier = data[:,3]

T = 300
mask = temp == T

plt.figure(figsize=(8,6))

plt.plot(mu[mask], carrier[mask])

plt.xlabel("Chemical Potential (eV)")
plt.ylabel("Carrier Concentration")

plt.title(f"Carrier Concentration at {T} K")

plt.grid(True)

plt.savefig("../figures/carrier_concentration_300K.png", dpi=300)
plt.show()
