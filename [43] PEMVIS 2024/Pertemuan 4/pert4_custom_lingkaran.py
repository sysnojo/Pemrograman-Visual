# Membuat lingkaran OLYMPIC RINGS

import numpy as np
import matplotlib.pyplot as plt

print("\033c")

# titik pusat 0, 0 jari" r | r = x^2 + y^2
x = np.linspace(-7, 7, 10000)
plt.figure(figsize=(8, 6.5))

l = 3

y = x - x - 0
y1 = (4 - x**2)**0.5
y2 = -(4 - x**2)**0.5

# Circle 2
y3 = 0 + (4 - (x-5)**2)**0.5
y4 = 0 - (4 - (x-5)**2)**0.5

# Circle 3
y5 = 0 + (4 - (x+5)**2)**0.5
y6 = 0 - (4 - (x+5)**2)**0.5

# Circle 4
y7 = -0.5 + (4 - (x-2.5)**2)**0.5
y8 = -0.5 - (4 - (x-2.5)**2)**0.5

# Circle 5
y9 = -0.5 + (4 - (x+2.5)**2)**0.5
y10 = -0.5 - (4 - (x+2.5)**2)**0.5

plt.plot(x, y, '-k')
plt.plot(x, y1, '-k', label='y1, y2')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-r', label='y3, y4')
plt.plot(x, y4, '-r')
plt.plot(x, y5, '-b', label='y5, y6')
plt.plot(x, y6, '-b')
plt.plot(x, y7, '-g', label='y7, y8')
plt.plot(x, y8, '-g')
plt.plot(x, y9, '-y', label='y9, y10')
plt.plot(x, y10, '-y')

plt.legend(loc='upper center')
plt.grid()
plt.show()