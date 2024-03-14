# Membuat lingkaran OLYMPIC RINGS

import numpy as np
import matplotlib.pyplot as plt

print("\033c")

# titik pusat 0, 0 jari" r | r = x^2 + y^2
x = np.linspace(-12, 12, 10000)
plt.figure(figsize=(12, 12))

# kepala mickey
y = x - x - 0
y1 = 5 + (4 - (x-5)**2 + 2.5)**0.5
y2 = 5 -(4 - (x-5)**2 + 2.5)**0.5

# telinga kanan
y3 = 8 + (4 - (x-8)**2 - 1)**0.5
y4 = 8 - (4 - (x-8)**2 - 1)**0.5

# telinga kanan
y5 = 8 + (4 - (x-2)**2 - 1)**0.5
y6 = 8 - (4 - (x-2)**2 - 1)**0.5

# mata kanan
y7 = 6 + (4 - (x-6)**2 - 3.7)**0.5
y8 = 6 - (4 - (x-6)**2 - 3.7)**0.5
# mata kiri
y9 = 6 + (4 - (x-4)**2 - 3.7)**0.5
y10 = 6 - (4 - (x-4)**2 - 3.7)**0.5

# hidung
y11 = 5 + (4 - (x-5)**2 - 3.9)**0.5
y12 = 5 - (4 - (x-5)**2 - 3.9)**0.5

# mata kanan
# y5 = 5 + (4 - (x-2)**2 - 1)**0.5
# y6 = 5 - (4 - (x-2)**2 - 1)**0.5
# # Circle 3
# y5 = 0 + (4 - (x+5)**2)**0.5
# y6 = 0 - (4 - (x+5)**2)**0.5

# # Circle 4
# y7 = -0.5 + (4 - (x-2.5)**2)**0.5
# y8 = -0.5 - (4 - (x-2.5)**2)**0.5

# # Circle 5
# y9 = -0.5 + (4 - (x+2.5)**2)**0.5
# y10 = -0.5 - (4 - (x+2.5)**2)**0.5

plt.fill_between(x, y1, y2, color='black')
plt.fill_between(x, y3, y4, color='black')
plt.fill_between(x, y5, y6, color='black')
plt.fill_between(x, y7, y8, color='white')
plt.fill_between(x, y9, y10, color='white')

plt.plot(x, y, '-k')
plt.plot(x, y1, '-k', label='y1, y2')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-k', label='y3, y4')
plt.plot(x, y4, '-k')
plt.plot(x, y5, '-k', label='y5, y6')
plt.plot(x, y6, '-k')
plt.plot(x, y7, '-k', label='y7, y8')
plt.plot(x, y8, '-k')
plt.plot(x, y9, '-k', label='y9, y10')
plt.plot(x, y10, '-k')
plt.plot(x, y11, '-w', label='y11, y12')
plt.plot(x, y12, '-w')


plt.legend(loc='upper center')
plt.grid()
plt.show()