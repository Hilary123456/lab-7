import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setting up the figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Defining x range, avoiding division by zero near x = 0
x = np.linspace(-np.pi, np.pi, 400)
x = x[x != 0]

# Calculating y and z
y = 1 / x
z = np.sin(x)

# Plotting the data
ax.plot(x, y, z, label='y = 1/x, z = sin(x)')

# Setting labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('трёхмерный график')

# Show plot
plt.legend()
plt.show()