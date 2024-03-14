import numpy as np
import matplotlib.pyplot as plt

rowmax = 1500
colmax = 1500

num_shapes = 90
max_radius = 300

Gambar = np.zeros(shape=(colmax+1, rowmax+1, 3), dtype=np.int16)

for _ in range(num_shapes):
    center_x = np.random.randint(max_radius, rowmax - max_radius)
    center_y = np.random.randint(max_radius, colmax - max_radius)
    
    radius = np.random.randint(50, max_radius)
    color = np.random.randint(0, 256, size=3)

    for y in range(center_y - radius, center_y + radius):
        for x in range(center_x - radius, center_x + radius):
            if (x - center_x)**2 + (y - center_y)**2 <= radius**2:
                Gambar[y, x] = color

plt.figure(figsize=(8, 8))
plt.imshow(Gambar)
plt.axis('off')
plt.show()
