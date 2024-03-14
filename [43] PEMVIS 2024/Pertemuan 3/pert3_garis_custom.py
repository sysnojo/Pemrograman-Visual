from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time


x = np.linspace(-10, 10, 1000)
plt.figure(figsize=(4,15))

# plt.plot(x, (0.05*-x**2)**0.5, '-k')
# plt.plot(x, -((0.05-x**2)**0.5), '-k')

# y1 = x**2
# y2 = x**2 - 10
# # y3 = x
# # y4 = 2*x
# # y5 = -0.5*x
# # y6 = -x
# # y7 = -2*x

y1 = x**2
y2 = (-x**2) + 200
y3 = (x*0) + 100
y4 = (x**4)/100
y5 = (-x**4)/100 + 200
y6 = (x**3.7*4)/70 - 190
y7 = (x[::-1]**3.7 * 4) / 70 - 190
# y8 = (-x**2) + 200 + 30

plt.plot(x, y1, '-r', label='y1')
plt.plot(x, y2, '-r', label='y2')
plt.plot(x, y3, '-r', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-b', label='y5')
plt.plot(x, y6, '-r', label='y6')
plt.plot(x, y7, '-r', label='y7')
# plt.plot(x, y8, '-c', label='y8')

plt.legend(loc = 'upper left')
plt.grid()
plt.show()
