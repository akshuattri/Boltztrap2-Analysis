import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../examples/interpolation.trace")

mu = data[:,0]
temp = data[:,1]

PFxx = data[:,13]
PFyy = data[:,14]
PFzz = data[:,15]

T = 300
mask = temp == T

plt.figure(figsize=(8,6))

plt.plot(mu[mask], PFxx[mask], label='PFxx')
plt.plot(mu[mask], PFyy[mask], label='PFyy')
plt.plot(mu[mask], PFzz[mask], label='PFzz')

plt.xlabel("Chemical Potential (eV)")
plt.ylabel("Power Factor")

plt.title(f"Power Factor at {T} K")

plt.legend()
plt.grid(True)

plt.savefig("../figures/powerfactor_300K.png", dpi=300)
plt.show()
