import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x_data = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x_data, np.sin(x_data))

def update(frame):
    line.set_ydata(np.sin(x_data + frame * 0.1))
    return line,

ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.title('Анимированный график функции y = sin(x)')

ani = FuncAnimation(fig, update, frames=range(100), interval=50)

ani.save('sin_animation.gif', writer='pillow', fps=30)

plt.show()

