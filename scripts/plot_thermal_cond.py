import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../examples/interpolation.trace")

mu = data[:,0]
temp = data[:,1]

kxx = data[:,10]
kyy = data[:,11]
kzz = data[:,12]

T = 300
mask = temp == T

plt.figure(figsize=(8,6))

plt.plot(mu[mask], kxx[mask], label='kxx')
plt.plot(mu[mask], kyy[mask], label='kyy')
plt.plot(mu[mask], kzz[mask], label='kzz')

plt.xlabel("Chemical Potential (eV)")
plt.ylabel("Electronic Thermal Conductivity")

plt.title(f"Electronic Thermal Conductivity at {T} K")

plt.legend()
plt.grid(True)

plt.savefig("../figures/thermal_cond_300K.png", dpi=300)
plt.show()
