import matplotlib.pyplot as plt
import numpy as np

# Generate simple data for visualization
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave')
plt.title('Simple CFD Visualization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()