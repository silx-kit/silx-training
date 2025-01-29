import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load spectrum
array = np.loadtxt("data/spectrum.txt")

# Step 2: Extract energy and mu
energy = array[:, 0]
mu = array[:, 1]

# Step 3: Plot both sine and cosine curves
plt.plot(energy, mu, label="mu Curve", color="blue")

# Step 4: Add labels, title, and legend
plt.xlabel("energy (keV)")
plt.ylabel("absorption (a.u.)")
plt.legend()

# Show the plot
plt.show()
