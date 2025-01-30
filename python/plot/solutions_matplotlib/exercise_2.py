import numpy as np
import matplotlib.pyplot as plt

array = np.loadtxt("data/spectrum.txt")
energy = array[:, 0]
mu = array[:, 1]
normalized_energy = array[:, 2]
pre_edge = array[:, 3]
post_edge = array[:, 4]

ax1, ax2 = plt.subplots(1, 2, figsize=(20, 10))[-1]

ax1.plot(normalized_energy, mu)
ax1.plot(normalized_energy, pre_edge, color="orange", linestyle=":")
ax1.fill_between(normalized_energy, 0, pre_edge, color="orange", alpha=0.5)

ax1.plot(normalized_energy, post_edge, color="green", linestyle=":")
ax1.fill_between(normalized_energy, 4, post_edge, color="green", alpha=0.5)

ax1.set_xlabel("Energy (eV)")
ax1.set_ylabel("absorption")

ax2.plot(normalized_energy, mu, label="mu")
ax2.set_xlabel("Energy (eV)")
ax2.set_ylabel("absorption")

E0 = 8981.1

ax2.axvline(E0, color="red", linestyle="--", linewidth=3)
ax2.text(8900, 1.5, "E0", color="red")


# Show the plot
plt.show()
