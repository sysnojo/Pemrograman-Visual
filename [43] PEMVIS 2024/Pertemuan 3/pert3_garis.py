import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 1000)
plt.figure(figsize=(4, 15))

plt.plot(x, (0.05 - x**2)**0.5, '-k')
plt.plot(x, -((0.05 - x**2))**0.5, '-k')

y1 = x - x - 0
y2 = 0.5 * x
y3 = x
y4 = 2*x
y5 = -0.5*x
y6 = -x
y7 = -2*x

plt.plot(x, y1, '-k', label='y1')
plt.plot(x, y2, '-r', label='y2')
plt.plot(x, y3, '-g', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-y', label='y5')
plt.plot(x, y6, '-m', label='y6')
plt.plot(x, y7, '-c', label='y7')

plt.legend(loc='upper left')
plt.grid()
plt.show()