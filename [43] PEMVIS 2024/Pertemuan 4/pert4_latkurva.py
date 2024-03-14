# tp
# -1, 0
# 1, 0
# 2, 0
# y = -(x-1)(x+1)(x+2)
# y = -(x-1)(x^2 + 3x + 2)
# y = -(x^3 + 3x^2 + 2x - x^2 - 3x - 2)
# y = -x^3 + 2x^2 - x - 2

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 10000)
plt.figure(figsize=(3,40))

plt.plot(x, (0.01 - x**2)**0.5, '-k')
plt.plot(x, -((0.01 - x**2)**0.5), '-k')

y = x - x - 0
y1 = -(x**3 - 2*x**2 + - x + 2)

plt.plot(x, y, '-k')

plt.plot(x, y1, '-r', label='y1')

plt.legend(loc='upper left')
plt.grid()
plt.show()