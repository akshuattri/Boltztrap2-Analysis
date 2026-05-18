import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../examples/interpolation.trace")

mu = data[:,0]
temp = data[:,1]

Lxx = data[:,16]
Lyy = data[:,17]
Lzz = data[:,18]

T = 300
mask = temp == T

plt.figure(figsize=(8,6))

plt.plot(mu[mask], Lxx[mask], label='Lxx')
plt.plot(mu[mask], Lyy[mask], label='Lyy')
plt.plot(mu[mask], Lzz[mask], label='Lzz')

plt.xlabel("Chemical Potential (eV)")
plt.ylabel("Lorenz Number")

plt.title(f"Lorenz Number at {T} K")

plt.legend()
plt.grid(True)

plt.savefig("../figures/lorenz_300K.png", dpi=300)
plt.show()
