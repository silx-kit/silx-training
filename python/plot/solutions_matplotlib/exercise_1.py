import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 100 points between 0 and 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Step 2: Calculate sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Step 3: Plot both sine and cosine curves
plt.plot(x, y_sin, label='Sine Curve', color='b')  # Blue for sine curve
plt.plot(x, y_cos, label='Cosine Curve', color='r')  # Red for cosine curve

# Step 4: Add labels, title, and legend
plt.xlabel('X (radians)')
plt.ylabel('Y (value)')
plt.title('Sine and Cosine Curves')
plt.legend()

# Show the plot
plt.show()
